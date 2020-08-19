class Solution:
    def balancedStringSplit(self, s):
        check = {'R': 0, 'L': 0}
        count = 0
        for c in s:
            check[c] += 1
            if check['R'] == check['L']:
                count += 1
                check['R'] = 0
                check['L'] = 0
        return count
            

            

sol1 = Solution()
sol1.balancedStringSplit("RLRRLLRLRL")