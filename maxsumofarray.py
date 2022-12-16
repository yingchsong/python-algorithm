nums = [-2,1,-3,4,-1,2,1,-5,4]
def maxSubArray(nums):
        max=nums[0]
        for i in range(1,len(nums)):
            s = nums[i]+nums[i-1] # calculate the sum of elements before ist
            if nums[i]<s:
                nums[i]=s #update ist element as the max sum before ist
            if nums[i]>max:
                max=nums[i] # update max sum include ist
        return max

print(maxSubArray(nums))