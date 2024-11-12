#a)
def multiplication_table(num):
  for i in range(1, 13):
    print(num, "x", i, "=", num * i)

number = int(input("Hey Max, Enter the number: "))

multiplication_table(number)