# class solution():
#
#     def twosum(self, nums:list[int], target:int) -> list[int]:
#
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return[i, j]
#
# input_list = [2,3,4,5,7,8,9]
# x = solution()
# print(x.twosum(input_list,14 ))

# class solution():
#
#     def twosum(self, nums:list[int], target:int ) -> int:
#
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return[i, j]
#
# input_list = [12,23,34,45,67]
# x = solution()
# print(x.twosum(input_list, 68))

# class solution:
#
#     def twosum(self, nums:list[int], target:int) -> list[int]:
#         numshashtable = {}
#         for i,num in enumerate (nums):
#             compliment = target - num
#             if compliment in numshashtable:
#                 return[numshashtable[compliment],]
#
#             else:numshashtable[num] = i


# class solution:
#
#     def twoSum(self, nums:list[int], target:int) -> list[int]:
#
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return[i, j]
#
# input_list = [2,4,5,6,7,8,9,10]
# x = solution()
# print(x.twoSum(input_list, 12))

# class solution:
#
#     def twosum(self, nums:list[int], target:int) -> list[int]:
#
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return[i, j]
#
# input_list = [2,3,4,5,6,8,9]
# x = solution()
# print(x.twosum(input_list, 10))
#




