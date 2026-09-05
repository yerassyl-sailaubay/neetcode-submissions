class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(0, len(nums)):
            left = i + 1
            right = len(nums) - 1 

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                current = nums[left] + nums[right]
                target = -nums[i]

                if current == target:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1


                elif current < target:
                    left += 1

                else:
                    right -= 1

            
        return result
        