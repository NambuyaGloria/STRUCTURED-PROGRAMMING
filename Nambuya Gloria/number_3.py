def findLargest(numbers):
    if not numbers:
        return None
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
largest_number = findLargest(numbers)
print("Largest number:", largest_number)