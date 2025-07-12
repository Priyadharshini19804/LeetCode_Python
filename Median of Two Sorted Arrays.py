"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

"""
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            i = (low + high) // 2
            j = (m + n + 1) // 2 - i

            maxLeftA = float('-inf') if i == 0 else nums1[i - 1]
            minRightA = float('inf') if i == m else nums1[i]

            maxLeftB = float('-inf') if j == 0 else nums2[j - 1]
            minRightB = float('inf') if j == n else nums2[j]

            # Correct partition found
            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (m + n) % 2 == 0:
                    return (max(maxLeftA, maxLeftB) + min(minRightA, minRightB)) / 2.0
                else:
                    return max(maxLeftA, maxLeftB)
            elif maxLeftA > minRightB:
                high = i - 1
            else:
                low = i + 1
