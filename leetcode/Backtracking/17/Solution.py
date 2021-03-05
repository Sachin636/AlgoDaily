class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        res = []
        alpha = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                 '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        def rec(inp, ans):
            if len(inp) == 0:
                res.append(ans)
                return

            digit = inp[0]
            for i in alpha[digit]:
                c = ''
                c = ans + i
                rec(inp[1:], c)

        rec(digits, '')
        return res
