class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        number_dict = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in number_dict:
                return [number_dict[complement], i]

            number_dict[num] = i

        return[]

    nums = [2,7,11,15]
    target = 9
    result = twosums(nums, target)
    print(result)