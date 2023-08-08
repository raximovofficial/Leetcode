class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        def gets():
        # ya = []
            for i in nums:
                yield len([x for x in nums if x < i])
        s = gets()
        return list(s)   
        # return ya
    


a = Solution()
print(a.smallerNumbersThanCurrent(nums = [8,1,2,2,3]))