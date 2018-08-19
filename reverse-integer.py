class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        try:
            int(x)
        except ValueError:
            print("Integer expected!")
            return 0

        str_x = str(x)
        if x < 0:
            str_x = '-' + str_x[::-1][:-1]
            reverse = int(str_x)
        else:
            str_x = str_x[::-1]
            reverse = int(str_x)

        neg_limit = -0x80000000
        pos_limit = 0x7fffffff

        if reverse < 0:
            val = reverse & neg_limit
            if val != neg_limit:
                return 0
        elif reverse == 0:
            return reverse
        else:
            val = reverse & pos_limit
            if val != reverse:
                return 0

        return reverse


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(1534236469))