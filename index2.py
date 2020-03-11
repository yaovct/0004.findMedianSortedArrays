# the fastest method
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        A, B, m, n = nums1, nums2, len(nums1), len(nums2)
        if m > n:
            A, B, m, n = B, A, n, m
        imin, imax, half_len = 0, m, (m + n + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect
		
                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else: max_of_left = max(A[i-1], B[j-1])
		
                if (m + n) % 2 == 1:
                    return max_of_left
		
                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else: min_of_right = min(A[i], B[j])
		                return (max_of_left + min_of_right) / 2.0

my_test = Solution()
nums1 = [1, 2]
nums2 = []
print("nums1 = %s" % nums1)
print("nums2 = %s" % nums2)
print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))

nums1 = [1, 2, 3]
nums2 = []
print("nums1 = %s" % nums1)
print("nums2 = %s" % nums2)
print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))

nums1 = [1, 2, 3, 4]
nums2 = []
print("nums1 = %s" % nums1)
print("nums2 = %s" % nums2)
print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))

nums1 = [1, 2, 3, 3, 3, 4]
nums2 = []
print("nums1 = %s" % nums1)
print("nums2 = %s" % nums2)
print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))

nums1 = [1]
nums2 = [2]
print("nums1 = %s" % nums1)
print("nums2 = %s" % nums2)
print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))

nums1 = [1, 3]
nums2 = [2]
print("nums1 = %s" % nums1)
print("nums2 = %s" % nums2)
print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))

nums1 = [2, 3]
nums2 = [1]
print("nums1 = %s" % nums1)
print("nums2 = %s" % nums2)
print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))

nums1 = [2]
nums2 = [1, 3]
print("nums1 = %s" % nums1)
print("nums2 = %s" % nums2)
print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))

nums1 = [1]
nums2 = [2, 3]
print("nums1 = %s" % nums1)
print("nums2 = %s" % nums2)
print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))

nums1 = [1, 2]
nums2 = [3, 4]
print("nums1 = %s" % nums1)
print("nums2 = %s" % nums2)
print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))

nums1 = [1, 3]
nums2 = [2, 4]
print("nums1 = %s" % nums1)
print("nums2 = %s" % nums2)
print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))

nums1 = [1, 4]
nums2 = [2, 3]
print("nums1 = %s" % nums1)
print("nums2 = %s" % nums2)
print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))

nums1 = [2, 3]
nums2 = [1, 4]
print("nums1 = %s" % nums1)
print("nums2 = %s" % nums2)
print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))

nums1 = [2, 4]
nums2 = [1, 3]
print("nums1 = %s" % nums1)
print("nums2 = %s" % nums2)
print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))

nums1 = [1, 2, 2]
nums2 = [3, 4, 6]
print("nums1 = %s" % nums1)
print("nums2 = %s" % nums2)
print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))

nums1 = [1, 2, 7]
nums2 = [3, 4]
print("nums1 = %s" % nums1)
print("nums2 = %s" % nums2)
print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))

nums1 = [1, 2, 2, 2, 2, 2, 3, 6]
nums2 = [3, 4, 6, 7, 7, 8, 9, 9]
print("nums1 = %s" % nums1)
print("nums2 = %s" % nums2)
print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))

nums1 = [1, 2, 2, 2, 2, 2, 3, 3]
nums2 = [3, 4, 6, 7, 7, 8, 9, 9]
print("nums1 = %s" % nums1)
print("nums2 = %s" % nums2)
print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))

nums1 = [1, 2, 2, 2, 2, 2, 3]
nums2 = [3, 4, 6, 7, 7, 8, 9, 9]
print("nums1 = %s" % nums1)
print("nums2 = %s" % nums2)
print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))

nums1 = [1, 2, 2, 2, 2, 2, 2, 9]
nums2 = [3, 4, 6, 7, 7, 8, 9, 9]
print("nums1 = %s" % nums1)
print("nums2 = %s" % nums2)
print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))

nums1 = [100000]
nums2 = [100001]
print("nums1 = %s" % nums1)
print("nums2 = %s" % nums2)
print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))

nums1 = [1]
nums2 = [2, 3, 4]
print("nums1 = %s" % nums1)
print("nums2 = %s" % nums2)
print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))
