class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def func():
            s = 0
            for i in range(n+1):
                if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
                    s += i
                yield s

        f = func()
        return list(f)
                        #     for i in range(n+1):
                        #         if i % 3 == 0 or i % 5 ==0 or i % 7 == 0:
                        #           s += i
                        #     return s
            
            


a = Solution()
print(a.sumOfMultiples(n = 7))