#_*_ coding:utf-8 _*_

#[]三数之和，暴力贪婪法

class Solution(object):
    def threeSum(self,nums):
        result = []
        length = len(nums)
        key = {}
        nums.sort()
        for i in range(length):
            if i > 0:
                break
            for j in range(i+1,length):
                for z in range(j+1,length):
                    # print(i,j,z)
                    if nums[z] + nums[j] + nums[i] == 0 :
                        a = [nums[i],nums[j],nums[z]]
                        a.sort()
                        if a not in result:
                            result.append(a)
                        # print("find.....",i,j,z)

        return result
                

if __name__ == "__main__":
    s = Solution()
    # a = [-1,-1,2]
    # b = [-1,2,-1]
    # b.sort()
    # print(a,b)
    # print (a == b)
    print(s.threeSum([-1,0,1,2,3,-2,1,-1,5,-3,-2,-1]))

