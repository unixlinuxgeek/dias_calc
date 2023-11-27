import sys
# def calc(a,oper,b):
#    if oper == "+":
#         a = int(a)
#         b = int(b)
#         sum = a + b
#         print(sum)

def minus():
   a = int(sys.argv[1])
   b = int(sys.argv[3])
   res = a-b
   print(res)

def plus():
   a = int(sys.argv[1])
   b = int(sys.argv[3])
   res = a+b
   print(res)

def div():
   a = int(sys.argv[1])
   b = int(sys.argv[3])
   res = a/b
   print(res)
def calc():
  if sys.argv[2] == "-":
     minus()

  if sys.argv[2] == "+":
      plus()


  if sys.argv[2] == "/":
     div()

calc()