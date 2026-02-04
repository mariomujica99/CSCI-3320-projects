import random
import time

def gen_rand_nums(length, min, max):
    rand_nums = []
    for i in range(length):
        rand_nums.append(random.randint(min, max))
    return rand_nums


def minSubSum2(a):
    start_time = time.perf_counter_ns()
    minSum = 0
    s_Index = 0
    e_Index = 0
    for i in range(len(a)):
        thisSum = 0
        for j in range(i, len(a)):
            thisSum += a[j]
            if(thisSum < minSum):
                minSum = thisSum
                s_Index = i
                e_Index = j
    end_time = time.perf_counter_ns()
    exe_time = end_time - start_time

    print(f'Algorithm 2: ')
    print(f'MinSum: {minSum}, S_index: {s_Index}, E_index: {e_Index}')
    print(f'Execution Time: {exe_time} nanoseconds')


def minSubSum3(a):
    start_time = time.perf_counter_ns()
    def minSumRec(a, left, right):
        if left == right:
            return min(a[left], 0), left, right

        center = (left + right) // 2
        minLeftSum, leftStart, leftEnd = minSumRec(a, left, center)
        minRightSum, rightStart, rightEnd = minSumRec(a, center + 1, right)

        minLeftBorderSum, leftBorderSum = 0, 0
        leftBorderStart = center
        for i in range(center, left - 1, -1):
            leftBorderSum += a[i]
            if leftBorderSum < minLeftBorderSum:
                minLeftBorderSum = leftBorderSum
                leftBorderStart = i

        minRightBorderSum, rightBorderSum = 0, 0
        rightBorderEnd = center + 1
        for i in range(center + 1, right + 1):
            rightBorderSum += a[i]
            if rightBorderSum < minRightBorderSum:
                minRightBorderSum = rightBorderSum
                rightBorderEnd = i

        if minLeftSum <= minRightSum and minLeftSum <= (minLeftBorderSum + minRightBorderSum):
            return minLeftSum, leftStart, leftEnd
        elif minRightSum <= minLeftSum and minRightSum <= (minLeftBorderSum + minRightBorderSum):
            return minRightSum, rightStart, rightEnd
        else:
            return minLeftBorderSum + minRightBorderSum, leftBorderStart, rightBorderEnd

    minSum, s_Index, e_Index = minSumRec(a, 0, len(a) - 1)

    end_time = time.perf_counter_ns()
    execution_time_ns = end_time - start_time

    print(f'Algorithm 3: ')
    print(f'MinSum: {minSum}, S_index: {s_Index}, E_index: {e_Index}')
    print(f'Execution time: {execution_time_ns} nanoseconds')


def minSubSum4(a):
    start_time = time.perf_counter_ns()

    minSum, thisSum = 0, 0
    s_Index, e_Index, tempStart = 0, 0, 0

    for j in range(len(a)):
        thisSum += a[j]
        if thisSum < minSum:
            minSum = thisSum
            s_Index = tempStart
            e_Index = j
        if thisSum > 0:
            thisSum = 0
            tempStart = j+1

    end_time = time.perf_counter_ns()
    execution_time_ns = end_time - start_time

    print(f'Algorithm 4: ')
    print(f'MinSum: {minSum}, S_index: {s_Index}, E_index: {e_Index}')
    print(f'Execution time: {execution_time_ns} nanoseconds')


if __name__ == "__main__":
    while True:
        try:
            size = int(input("Please enter the size of the problem (N): "))
            if size <= 0:
                raise ValueError
            elif size < 50:
                rand_nums = gen_rand_nums(size, -9999, 9999)
                for i in rand_nums:
                    print(i, end=' ')
                print('\n')
                minSubSum2(rand_nums)
                print()
                minSubSum3(rand_nums)
                print()
                minSubSum4(rand_nums)
                print()
                break
            elif size >= 50:
                rand_nums = gen_rand_nums(size, -9999, 9999)
                print()
                minSubSum2(rand_nums)
                print()
                minSubSum3(rand_nums)
                print()
                minSubSum4(rand_nums)
                print()
                break
        except ValueError:
            print("Invalid input. Please enter a positive number.")