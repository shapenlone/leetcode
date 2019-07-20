
#tow sum

class Solution(object):
    def towSum(self,nums,target):
        sumMap = {}
        for n in range(len(nums)):
            if (target - nums[n]) in sumMap:
                return [sumMap[target-nums[n]],n]
            sumMap[nums[n]] = n
        
if __name__ == "__main__":
    s = Solution()
    print(s.towSum([1,2,3,5,6,7],9))
