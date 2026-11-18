import random
answer=random.randint(1,100)
count=0


while True:
  a=int(input("请输入一个数字"))
  count=count+1
  if a>answer:
    print("你猜大了")
  elif a<answer:
      print("你猜小了")
  else:
     print("恭喜你猜对了")
     print(f"你一共猜了{count}次")
     break
29