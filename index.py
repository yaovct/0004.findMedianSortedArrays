# the simplest method
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = nums1 + nums2
        n = sorted(n)
        print(n)
        if len(n) % 2:
        	return n[len(n)/2]
        else:
        	return (n[len(n)/2-1] + n[len(n)/2]) / 2.0

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
