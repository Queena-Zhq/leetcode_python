#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#
# https://leetcode.com/problems/house-robber/description/
#
# algorithms
# Easy (41.37%)
# Likes:    4048
# Dislikes: 124
# Total Accepted:    464.2K
# Total Submissions: 1.1M
# Testcase Example:  '[1,2,3,1]'
#
# You are a professional robber planning to rob houses along a street. Each
# house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security system
# connected and it will automatically contact the police if two adjacent houses
# were broken into on the same night.
# 
# Given a list of non-negative integers representing the amount of money of
# each house, determine the maximum amount of money you can rob tonight without
# alerting the police.
# 
# Example 1:
# 
# 
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money =
# 3).
# Total amount you can rob = 1 + 3 = 4.
# 
# Example 2:
# 
# 
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5
# (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
# 
# 
#

# @lc code=start
class Solution:
    def rob(self, nums: [int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])
        elif len(nums) == 3:
            return max(nums[0]+nums[2],nums[1])
        else:
            

# @lc code=end
if __name__ == "__main__":
    Test = Solution()
    print(Test.rob([1,2,3,1]))
