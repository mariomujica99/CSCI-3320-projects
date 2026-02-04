import random

def gen_rand_nums(length, min, max):
    """
    FUNCTION gen_rand_nums:
        Generate a list of random integers within a specified range.

    INPUT_Parameters:
        length (int): Number of random integers to generate.
        min (int): Minimum possible value (inclusive).
        max (int): Maximum possible value (inclusive).

    Returns:
        List[int]: List of randomly generated integers.
    """
    rand_nums = []
    for i in range(length):
        rand_nums.append(random.randint(min, max))
    return rand_nums

# BRUTE FORCE VERSION
'''
def Alg1_brute(arr):
    """
    FUNCTION Alg1_brute:
        Brute-force method to find a continuous subarray with a sum of zero.
    
    INPUT_Parameters:
        arr (List[int]): The input list of integers.
    
    Returns:
        bool: True if a zero-sum subarray exists, False otherwise.
    """
    n = len(arr)
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += arr[j]
            if sum == 0:
                print("Yes, there is a sequence where the sum of the elements equals zero.")
                print(f"Starting index: {i}")
                print(f"Ending index: {j}")
                print("Sum: ", end="")
                for k in range(i, j + 1):
                    if k < j:
                        if arr[k] <= 0:
                            print("(" + str(arr[k]) + ")", end=" + ")
                        else:
                            print(arr[k], end=" + ")
                    else:
                        if arr[k] <= 0:
                            print("(" + str(arr[k]) + ")", end=" = 0")
                        else:
                            print(arr[k], end=" = 0")
                print()
                return True
    print("No, there is no sequence where the sum of the elements equals zero.")
    return False
'''

# HASH VERSION
def Alg2_hash(arr):
    """
    FUNCTION Alg2_hash:
        Find a continuous subarray with a sum of zero using a hash map for O(n) time complexity.

    INPUT_Parameters:
        arr (List[int]): The input list of integers.

    Returns:
        bool: True if a zero-sum subarray exists, False otherwise.
    """
    prefix_sum_dict = {}
    current_sum = 0

    for i, num in enumerate(arr):
        current_sum += num

        if current_sum == 0:
            print("Yes, there is a sequence where the sum of the elements equals zero.")
            print(f"Starting index: 0")
            print(f"Ending index: {i}")
            print("Sum: ", end="")

            formatted_numbers = []

            for k in range(i + 1):
                if arr[k] < 0:
                    formatted_numbers.append(f"({arr[k]})")
                else:
                    formatted_numbers.append(str(arr[k]))
            print(" + ".join(formatted_numbers), end=" = 0\n")

            return True

        if current_sum in prefix_sum_dict:
            start_index = prefix_sum_dict[current_sum] + 1
            end_index = i
            print("Yes, there is a sequence where the sum of the elements equals zero.")
            print(f"Starting index: {start_index}")
            print(f"Ending index: {end_index}")
            print("Sum: ", end="")

            formatted_numbers = []

            for k in range(start_index, end_index + 1):
                if arr[k] < 0:
                    formatted_numbers.append(f"({arr[k]})")
                else:
                    formatted_numbers.append(str(arr[k]))
            print(" + ".join(formatted_numbers), end=" = 0\n")

            return True

        prefix_sum_dict[current_sum] = i

    print("No, there is no sequence where the sum of the elements equals zero.")
    return False


def menu():
    """
    FUNCTION menu:
        Prompt the user for the problem size and generate a random list of integers accordingly.
        If the list size is less than 50, use smaller integer ranges and print all values.
        Check for zero-sum subarrays using the hash algorithm.

    INPUT_Parameters:
        None (user input handled within the function).

    Returns:
        None (prints result directly).
    """
    while True:
        try:
            size = int(input("Please enter the size of the problem (N): "))
            print()
            if size <= 0:
                raise ValueError
            elif size < 50:
                rand_nums = gen_rand_nums(size, -99, 99)
                print("Generated Random Numbers:")
                for i in rand_nums:
                    print(i, end=' ')
                print('\n')
                '''
                Alg1_brute(rand_nums)
                '''
                Alg2_hash(rand_nums)
                break
            elif size >= 50:
                rand_nums = gen_rand_nums(size, -9999, 9999)
                '''
                Alg1_brute(rand_nums)
                '''
                Alg2_hash(rand_nums)
                break
        except ValueError:
            print("Invalid input. Please enter a positive number.")


if __name__ == "__main__":
    menu()