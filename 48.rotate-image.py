#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
# https://leetcode.com/problems/rotate-image/description/
#
# algorithms
# Medium (55.02%)
# Likes:    2771
# Dislikes: 216
# Total Accepted:    387K
# Total Submissions: 701.6K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# You are given an n x n 2D matrix representing an image.
# 
# Rotate the image by 90 degrees (clockwise).
# 
# Note:
# 
# You have to rotate the image in-place, which means you have to modify the
# input 2D matrix directly. DO NOT allocate another 2D matrix and do the
# rotation.
# 
# Example 1:
# 
# 
# Given input matrix = 
# [
# ⁠ [1,2,3],
# ⁠ [4,5,6],
# ⁠ [7,8,9]
# ],
# 
# rotate the input matrix in-place such that it becomes:
# [
# ⁠ [7,4,1],
# ⁠ [8,5,2],
# ⁠ [9,6,3]
# ]
# 
# 
# Example 2:
# 
# 
# Given input matrix =
# [
# ⁠ [ 5, 1, 9,11],
# ⁠ [ 2, 4, 8,10],
# ⁠ [13, 3, 6, 7],
# ⁠ [15,14,12,16]
# ], 
# 
# rotate the input matrix in-place such that it becomes:
# [
# ⁠ [15,13, 2, 5],
# ⁠ [14, 3, 4, 1],
# ⁠ [12, 6, 8, 9],
# ⁠ [16, 7,10,11]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def rotate(self, matrix: [[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        first reserse the up and down
        and then swap the symmetry through the diagonal
        """
        n = len(matrix)
        my_list = []
        for i in range(int(n/2)):
            my_list = matrix[i]
            matrix[i] = matrix[n-i-1]
            matrix[n-i-1] = my_list
        for i in range(n):
            for j in range(i):
                m = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = m

                
# @lc code=end
if __name__ == "__main__":
    test = Solution()
    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    matrix2 = [[ 5, 1, 9,11],[ 2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]]
    test.rotate(matrix1)
    test.rotate(matrix2)
    for i in matrix1:
        print(i)
    for i in matrix2:
        print(i)
    
