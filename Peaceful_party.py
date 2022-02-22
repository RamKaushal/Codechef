class peaceful:
  def __init__(self,testcases):
    self.testcases = testcases
  def peace(self):
    l = []
    for i in range(self.testcases):
      a,b,c = map(int,input().split())
      if a+c <= b:
        #print(b)
        l.append(b)
        #return b
      else:
        l.append(a+c)
    return l
      
      
if __name__ == "__main__":
  peaceful = peaceful(3)
  final = peaceful.peace()
  print(final)
