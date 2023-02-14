def histo(nums):
    for i in range(len(nums)):
        while nums[i]>0:
            print("*",end='')
            nums[i]-=1
        print()

n = list(map(int,input().split()))
histo(n)
