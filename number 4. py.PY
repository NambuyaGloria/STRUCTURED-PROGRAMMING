def main():
     print("This program generates the Syracuse sequence for a given starting value.") 
     n = int(input("Enter a starting value: ")) 
     while n != 1: 
         print(n, end=", ") 
         if n % 2 == 0: 
            n = n // 2 
         else: n = 3 * n + 1 
     print(n)
main()