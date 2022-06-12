from typing import List


class solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Leetcode 238
        :param nums:
        :return:
        '''
        lr = [1]*len(nums)
        rl = [1]*len(nums)

        for i in range(1, len(nums)):
            lr[i] = lr[i-1]*nums[i-1]

        for i in range(len(nums)-2, -1,-1):
            rl[i] = rl[i+1]*nums[i+1]

        result = []
        for i in range(0, len(nums)):
            result.append(lr[i]*rl[i])

        print(result)
        return result

if __name__ == "__main__":
    s = solution()
    print(s.productExceptSelf([1, 2, 3, 4]))

