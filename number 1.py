def main():
     print("This program calculates the nth Fibonacci number.") 
     n = int(input("Enter the position of the Fibonacci number you want (starting from 1): ")) 
     
     if n <= 0: 
        print("Please enter a positive integer.") 
        return
     elif n == 1 or n == 2:
        print("The Fibonacci number at position", n, "is 1") 
        return 
     fib1, fib2 = 1, 1 
     for i in range(3, n+1): 
      fib = fib1 + fib2 
      fib1, fib2 = fib2, fib 
      
      print(f"The Fibonacci number at position {n} is {fib}")
main()