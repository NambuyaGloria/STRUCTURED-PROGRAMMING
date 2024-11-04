def main():
     print("This program calculates the Greatest Common Divisor (GCD) of two numbers using Euclid's algorithm.")
     m = int(input("Enter the first number (m): ")) 
     n = int(input("Enter the second number (n): "))
     while m != 0: m, n = n % m, m 
     print(f"The GCD of the entered numbers is: {n}")
main()