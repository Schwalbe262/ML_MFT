# python DL.py --csv Data_2021_08_12_v1_m.csv

import torch
from torch.functional import split
import torch.nn as nn
from torch.nn.modules.activation import ReLU
from torch.utils.data import Dataset, DataLoader
import numpy as np
import pandas as pd
import argparse
import tqdm
import matplotlib.pyplot as plt


parser = argparse.ArgumentParser(description='DL Predictor for Transformer')
parser.add_argument('--csv',required=True)

args = parser.parse_args()


class HFTRDataset(Dataset):
    def __init__(self,csv_path) -> None:
        super().__init__()
        self.raw_csv = pd.read_csv(csv_path)
        self.raw_csv = self.raw_csv.dropna(axis=0).reset_index(drop=True)#drop NaN
        self.raw_csv = self.raw_csv[self.raw_csv['Lmt']>0.1].reset_index(drop=True)
        self.raw_csv = self.raw_csv[self.raw_csv['Lmr']>0.1].reset_index(drop=True)

        self.raw_csv = self.raw_csv[self.raw_csv['Llt']>0.3].reset_index(drop=True)
        self.raw_csv = self.raw_csv[self.raw_csv['Llt']<100].reset_index(drop=True)

        #pd.to_numeric(self.raw_csv['I1'])
        #pd.to_numeric(self.raw_csv['I2'])

    def __len__(self):
        return len(self.raw_csv)

    def __getitem__(self, idx):
        if torch.is_tensor(idx):
            idx = idx.tolist()
        xs = torch.from_numpy(
            self.raw_csv.iloc[idx,:22].to_numpy(dtype=np.float32)
            )
        ys = torch.from_numpy(
            self.raw_csv.iloc[idx,25:26].to_numpy(dtype=np.float32) # 22:23 <- Y 지정  23 : Lmt 24 : Lmr 
            ) #FIXME 20~25 
        return xs, ys

    def summary(self):
        print(self.raw_csv.describe())

dataset = HFTRDataset(args.csv)
split_factor = 0.8 #<- Train Test 비율 
train_set, test_set = torch.utils.data.random_split(
    dataset,
    [int(len(dataset)*split_factor), len(dataset) - int(len(dataset)*split_factor)]
    )
dataset.summary()
print(len(dataset))

trainloader = DataLoader(train_set,batch_size = 256) #<-Batch size : 한번에 연산할 데이터 수 (64~512)
testloader = DataLoader(test_set,batch_size = 256)

###--- MODEL --- ###

input_size = 22 #X개수
output_size = 1 #Y개수
#lr = 0.001 #Learning Rate : MOST important Hyper parameter
lr = 0.001

# Linear regression model
#Set of Linear -> Multi Layer Perceptron(MLP) Model
#Hyperparemter -> # layer, layer dim , activation func, ..
model = nn.Sequential(
    nn.BatchNorm1d(num_features=input_size),
    nn.Linear(input_size, 2048),
    nn.ReLU(),
    nn.Linear(2048, 2048),
    nn.ReLU(),
    #nn.Dropout(),
    nn.Linear(2048, 2048),
    nn.ReLU(),
    nn.Linear(2048, 2048),
    nn.ReLU(),
    #nn.SELU()
    nn.Linear(2048,output_size)
).cuda()

# Loss and optimizer
criterion = nn.MSELoss().cuda() # <- LOSS : Mean Squared Error(MSE) 
optimizer = torch.optim.SGD(model.parameters(), lr=lr) # SGD = Stochastic Gradient Descent 
lr_scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer=optimizer,T_max=100) #Learning Rate Scheduler.
#Try Exponent Decay , Cosine, Linear Decay ..

loss_log = []

def train(model, trainloader, criterion, optimizer):
    model.train()
    train_loss = 0
    for i, (xs, ys) in tqdm.tqdm(enumerate(trainloader)):
        xs = xs.cuda()
        ys = ys.cuda()
        #Fwd
        ys_hat = model(xs)
        loss = criterion(ys,ys_hat)
        train_loss += loss.item()
        #Bwd
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        lr_scheduler.step()
    
    print("train set length ", len(trainloader.dataset))
    print("Trainloss", float(train_loss)/len(trainloader.dataset)) #<- Trainset 전체에 대한 평균 Loss print


def test(model, testloader, criterion, plot_residual=False,epoch=0):
    model.eval()
    test_loss = 0
    if plot_residual:
        xss = []
        yss = []
    with torch.no_grad():
        for i, (xs, ys) in tqdm.tqdm(enumerate(testloader)):
            xs = xs.cuda()
            ys = ys.cuda()
            ys_hat = model(xs)
            test_loss += criterion(ys,ys_hat)
            if plot_residual:
                residual = ys_hat - ys
                xss += torch.squeeze(ys_hat).cpu().tolist()
                yss += torch.squeeze(residual).cpu().tolist()

    print("Test set length ", len(trainloader.dataset))
    print("Testloss", float(test_loss)/len(testloader.dataset)) #<- Test 전체에 대한 평균 loss print
    if plot_residual:
        print(xss[0])
        plt.clf()
        plt.scatter(xss,yss)
        plt.grid()
        plt.savefig(f'test_{epoch}.png')

for epoch in range(20): #<- 100 : epoch
    print("EPOCH" , epoch)
    #Train
    train(model,trainloader,criterion, optimizer)
    
    #Test
    test(model,testloader=testloader,criterion=criterion,plot_residual=True,epoch=epoch)


