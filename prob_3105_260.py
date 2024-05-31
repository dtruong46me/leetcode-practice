class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        results = []

        for num in nums:
            if num not in results:
                results.append(num)
            else:
                results.remove(num)
        
        return results[:2]
