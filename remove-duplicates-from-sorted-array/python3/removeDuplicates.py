class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nums = list(sorted(set(nums)))
        print(nums)
        return len(nums)
    
    # def removeDuplicates(self, nums: list[int]) -> int:
    #     unique_nums = sorted(set(nums))
    #       
    #     return len(unique_nums)
# a = [1,1,2]
# b = Solution()
# print(b.removeDuplicates(nums=a))

# class Solution:
#     def removeDuplicates(self, nums: list[int]) -> int:
#         if not nums:
#             return 0

#         # Start with the first unique element
#         k = 1

#         # Loop through the array starting from the second element
#         for i in range(1, len(nums)):
#             # If the current element is not the same as the previous one
#             if nums[i] != nums[i - 1]:
#                 # Place the unique element at the next position
#                 nums[k] = nums[i]
#                 print(f'k = {k} i = {i} nums = {nums}')
#                 k += 1
#         # print(nums)
#         # The array is now updated in-place, and k is the number of unique elements
#         """
#         nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
#         k = 1 i = 2 nums = [0, 1, 1, 1, 1, 2, 2, 3, 3, 4]
#         k = 2 i = 5 nums = [0, 1, 2, 1, 1, 2, 2, 3, 3, 4]
#         k = 3 i = 7 nums = [0, 1, 2, 3, 1, 2, 2, 3, 3, 4]
#         k = 4 i = 9 nums = [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
#         k = 5
#         nums[:k] = [0, 1, 2, 3, 4]
#         """
#         return k

nums = [0,0,1,1,1,2,2,3,3,4]
print(f'nums = {nums}')
solution = Solution()
k = solution.removeDuplicates(nums)
print(k)  # 5
print(nums[:k])  # [0, 1, 2, 3, 4]
