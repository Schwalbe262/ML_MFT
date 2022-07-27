
def find_element(A,B):
# A에 B element가 하나라도 포함 되어 있는지 검색
  for a in A :
    for b in B:
      if b == a : return True
  return False