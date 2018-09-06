class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev = 0
        n = x
        while x > 0:
            mdig = x % 10
            rev = rev * 10 + mdig
            x = x // 10

        return n == rev


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(10))
