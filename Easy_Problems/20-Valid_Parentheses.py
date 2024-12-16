class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
        # An input string is valid iff:
            # Open brackets must be closed by the same type of brackets.
            # Open brackets must be closed in the correct order.
            # Every close bracket has a corresponding open bracket of the same type.
            #
        my_list = ["()", "[]", "{}"]

        while True:
            replaced = False
            for i in my_list:
                if i in s:
                    s = s.replace(i, "")
                    replaced = True
            # stop the loops if no replacement occured
            if not replaced:
                break

        # If the string is empty, it's -> valid;
        # otherwise/else it's -> invalid
        if s == "":
            return True
        return False

        # another way of solving it
        # while "()" in s or "{}" in s or "[]" in s:
        #     # getting rid of the valid parentheses by replacing it with empty space
        #     s = s.replace("()", "").replace("{}", "").replace("[]", "")

        # # If the string is empty, it's -> valid;
        # # otherwise/else it's -> invalid
        # if s == "":
        #     return True
        # return False


if __name__ == '__main__':
    solution = Solution()
    q1 = solution.isValid("()")
    print(q1) # -> True
    q2 = solution.isValid("()[]{}")
    print(q2) # -> True
    q3 = solution.isValid("(]")
    print(q3) # -> False
    q4 = solution.isValid("([])")
    print(q4) # -> True
