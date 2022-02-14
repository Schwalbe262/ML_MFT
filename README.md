# ML_MFT
medium frequency transformer optimization using ML

N001_lightgbm.ipynb : lightgbm 모델 생성 및 튜닝

N002_lightgbm_plot.ipynb : lightgbm 모델 튜닝 및 하이퍼파라미터 시각화


C002_lightgbm_plot.py : N002코드 클러스터 실행용 코드

## lightgbm.ipynb
###### 1. import module
###### 2. data import & remove output data except target parameter & drop NaN
###### 3. data info check
###### 4. check outlier
###### 5. check data distribution
###### 6. show corelation between each parameter
###### 7. define outlier search function
###### 8. data pre-processing
###### 9. check outlier (after removing outlier)
###### 10. check data distribution (after pre-processing)
###### 11. show corelation between each parameter (after pre-processing)
###### 12. split input/output & data minmax normalize
###### 13. check data distribution (after normalize)
###### 14. lgbm setting
###### 15. K-fold validation
###### 16. parameter tuning
###### 17. parameter tuning result
###### 18. tuned-lgbm setting
###### 19. K-fold validation (tuned model)
