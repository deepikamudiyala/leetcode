class Solution:
    def numberOfSubarrays(self, nums, k):
        count = 0
        odd_count = 0
        freq = {0: 1}

        for num in nums:
            if num % 2 == 1:
                odd_count += 1
            count += freq.get(odd_count - k, 0)
            freq[odd_count] = freq.get(odd_count, 0) + 1

        return count