class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # want to loops through nums at index 0 and then loop for index 0 + 1
        # locate the target then return it in a list format
        # want two for loops
        # and return NONE if not the target...
        for i in range(len(nums) + 1):
            # for j in range(i + 1, len(nums)):
            if nums[i - 1 ] + nums[i + 1] == target:
                print(nums[i])
                print(i)
                return [i - 1, i + 1]
        return 0




# test block for testing
if __name__ == '__main__':
    solution = Solution()
    rq = solution.twoSum([3,2,3], 6)
    print(rq)
    # q1 = solution.twoSum([2, 7, 11, 15], 9)
    # print(q1)  # Output: [0, 1]
    # q2 = solution.twoSum([3, 2, 4], 6)
    # print(q2)  # Output: [1, 2]
    # q3 = solution.twoSum([3, 3], 6)
    # print(q3)  # Output: [0, 1]
