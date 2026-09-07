class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        add = 0

        for i in range(len(operations)):

            if operations[i] == "+":
                n = len(ans)
                ans1 = ans[n - 1] + ans[n - 2]
                ans.append(ans1)

            elif operations[i] == "C":
                ans.pop()

            elif operations[i] == "D":
                n = len(ans)
                ans2 = ans[n - 1] * 2
                ans.append(ans2)

            else:
                ans.append(int(operations[i]))

        for num in ans:
            add = add + num

        return add