class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # must read the same number from left to right, and right to left -> return True
        # if not -> return False
        # want to account for the negative sign? always will be -> False
        string_x = str(x)

        if string_x[0] == '-':
            return False

        reverse_string_x = string_x[::-1]
        return reverse_string_x == string_x



if __name__ == '__main__':
    solution = Solution()
    q1 = solution.isPalindrome(121)
    print(q1) # -> True
    q2 = solution.isPalindrome(-121)
    print(q2) # -> False
    q3 = solution.isPalindrome(10)
    print(q3) # -> False
