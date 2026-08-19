class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix)-1
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        while low <= high :
            mid = (low + high) // 2
            if matrix[mid][-1] == target:
                return True
            elif matrix[mid][-1] < target:
                low = mid + 1
            else:
                high = mid -1
        if low == len(matrix):
            return False
        low_1 = 0
        high_1 = len(matrix[low])-1
        while low_1 <= high_1 :
            mid_1 = (low_1 + high_1) // 2
            if matrix[low][mid_1] == target:
                return True
            elif matrix[low][mid_1] < target:
                low_1 = mid_1 + 1
            else:
                high_1 = mid_1 - 1
        return False