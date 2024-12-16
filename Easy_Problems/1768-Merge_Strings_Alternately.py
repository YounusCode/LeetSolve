class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = []
        i = 0
        j = 0

        # use of AND operator to not lead to out of index error
        while i < len(word1) and j < len(word2):
            result.append(word1[i])
            result.append(word2[j])
            i += 1
            j += 1

        # this is after the loop if any characters left in the word1 or word2
        if i < len(word1):
          result.extend(word1[i:])

        if j < len(word2):
          result.extend(word2[j:])

        # join the result list to return a string format result
        return ''.join(result)

# create a main block for testing
if __name__ == '__main__':
    solution = Solution()
    q1 = solution.mergeAlternately("abc", "pqr")
    print(q1)  # Output: "apbqcr"
    q2 = solution.mergeAlternately("ab", "pqrs")
    print(q2)  # Output: "apbqrs"
    q3 = solution.mergeAlternately("abcd", "pq")
    print(q3)  # Output: "apbqcd"
