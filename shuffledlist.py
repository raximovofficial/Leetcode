class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        def func():
            ans = "" 
            for i in range(len(indices)): 
                ans += s[indices.index(i)]
            yield ans
        f = func()
        return list(f)


a = Solution()
print(a.restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))