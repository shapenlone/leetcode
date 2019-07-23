#_*_ coding:utf-8 _*_

#[]三数之和，双指针法
class Solution1(object):
    def threeSum(self,nums):
        result = []
        length = len(nums)
        nums.sort()
        for i in range(length):
            if nums[i] > 0:
                break
            if i ==0 or nums[i] > nums[i-1]:
                l = i+1
                r = length-1
                while l<r:
                    s = nums[i]+nums[l] +nums[r]
                    if s ==0:
                        result.append([nums[i],nums[l],nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while r > l and nums[r] == nums[r+1]:
                            r -= 1
                    elif s > 0:
                        r -= 1
                    else:
                        l += 1
        return result

if __name__ == "__main__":
    s = Solution1()
    print(s.threeSum([-1,0,1,2,3,-2,1,-1,5,-3,-2,-1,0,3,0]))
