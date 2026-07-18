class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBound(isFirst):
            l, u = 0, len(nums) - 1
            res = -1
            while l <= u:
                mid = (l + u) // 2
                if nums[mid] == target:
                    res = mid
                    if isFirst:
                        u = mid - 1  
                    else:
                        l = mid + 1  
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    u = mid - 1
            return res

        return [findBound(True), findBound(False)]