def find_smallest(arr):
    if not arr:
        raise ValueError("Array is empty")
    smallest = arr[0]
    for num in arr[1:]:
        if num < smallest:
            smallest = num
    return smallest


if __name__ == "__main__":
    numbers = [42, 7, 19, 3, 88, 14, 5]
    print(f"Array: {numbers}")
    print(f"Smallest: {find_smallest(numbers)}")
