from typing import List


class Solution:
    '''
    leetcode -53
    '''
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = nums[0]
        max_sum = nums[0]

        for n in nums[1:]:
            if curr_sum < 0:
                curr_sum = n
            else:
                curr_sum += n
                max_sum = max(curr_sum, max_sum)

        return max_sum


if __name__ == "__main__" :
    s = Solution()
    print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
