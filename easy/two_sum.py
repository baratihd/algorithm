"""Two sum algorithm"""


class Solution:
    """
    This class gets list of numbers and target number
    and returns index of two number in list that equals
    target number.
    """
    @staticmethod
    def two_sum(nums: list[int], target: int):
        for first in range(0, len(nums)):
            for second in range(first + 1, len(nums)):
                if nums[first] + nums[second] == target:
                    return [first, second]
        return 'target not found!'


if __name__ == '__main__':
    nums: list[int] = [1, 15, 9, 13, 25]
    target: int = 40
    two_sum = Solution()
    print(two_sum.two_sum(nums, target))
