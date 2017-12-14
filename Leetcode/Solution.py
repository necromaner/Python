class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # tmp_num = {}
        # for i in range(len(nums)):
        #     if target - nums[i] in tmp_num:
        #         # here do not need to deal with the condition i = target-i
        #         return (tmp_num[target-nums[i]]+1, i+1)
        #     else:
        #         tmp_num[nums[i]] = i
        # return (-1, -1)
        answer=[-1,-1]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j]==target):
                    answer=[i,j]
                    return answer
        return answer

