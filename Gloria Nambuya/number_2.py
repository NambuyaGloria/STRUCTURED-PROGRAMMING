# b)
def evens(numbers):
    return [num for num in numbers if num % 2 == 0]

numbers = list(map(int, input("Hello gloria,Enter a list of integers separated by spaces: ").split()))
even = evens(numbers)
print("Even numbers are as follows", even)
