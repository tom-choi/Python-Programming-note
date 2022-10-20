def Fib(N:int):
    if N == 0 or N == 1:
        return 1
    else:
        return Fib(N-1) + Fib(N-2)

def main_1():
    N = int(input("Please input N = "))
    print(Fib(N))
    
arr = [1,2,3,4,5,6,7,8,9]
def binary_search(arr,target:int):
    a = 0
    b = len(arr)
    times = 0
    while (a != b):
        times += 1
        print(f"Run times: {times}")
        mid = (a + b) // 2
        if arr[mid] < target:
            a = mid + 1
        elif arr[mid] > target:
            b = mid - 1
        else:
            return mid
    return -1
times = -1

true_arr = [1,2,3,4,5,6,7,8,9]
def binary_search_recu(arr,target:int,a,b):
    mid = (a + b) // 2
    if mid == len(arr):
        return -1
    if arr[mid] < target:
        return binary_search_recu(arr,target,mid+1,b)
    elif arr[mid] > target:
        return binary_search_recu(arr,target,mid-1,b)
    else:
        return mid

def main_2():
    print(binary_search_recu(arr,10,0,len(arr)))
    
main_2()