class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumArray = 0
        count = 0
        hashmap = {0:1}
        for i in range(len(nums)):
            sumArray +=nums[i]
            if (sumArray-k) in hashmap:
                count += hashmap[sumArray-k]
            if sumArray in hashmap:
                hashmap[sumArray]+= 1
            else:
                hashmap[sumArray] = 1        
        return count