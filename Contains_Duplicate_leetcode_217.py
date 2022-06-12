from typing import List


class solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        Blind 75, leet code 217
        '''
        num_set = set()
        for n in nums:
            if n in num_set:
                return True
            num_set.add(n)
        return False


if __name__ == "__main__":
    s = solution()
    print(s.containsDuplicate([1, 2, 3, 4, 5, 1]))
    print(s.containsDuplicate([10, 3, 2]))