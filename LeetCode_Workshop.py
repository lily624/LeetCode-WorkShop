# LeetCode Day1 - Exercise 3 三数之和
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # 排序
        res = []
        i = 0
        while i < len(nums) - 2:   # i,j,k的位置[i, j,...,k]，jk可以相等，所以-2
            if i == 0 or nums[i] != nums[i - 1]:
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1     # <0要放大一点，所以j + 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        res.append([nums[i], nums[j], nums[k]])
                        j += 1     # 只改一个数一定会不等于0
                        k -= 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1  # 避免nums中的数重复，res中有想同的结果
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
            i += 1
        return res

# LeetCode Day1 - Exercise 2 Remove Elements
# 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
class Solution:
    def removeElement(self, nums:List[int], val:int) -> int:
        n = len(nums)
        while val in nums:
            nums.remove(val)
        return (len(nums))


# LeetCode Day1 - Exercise 1 Remove duplicate
# 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，
# 返回删除后数组的新长度。
# 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

class Solution:
    def removeDuplicates(self, nums:List[int]) -> int:
        n = len(nums):
        index = 0
        for i in range(1,n):
            if nums[index] == nums[i]:
                continue
            nums[index+1] = nums[i]
            index += 1
        return index + 1
