# the fastest method
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)
        start = 0
        end = l1
        while start <= end:
        	partitionX = (start + end + 1) / 2
        	partitionY = (l1 + l2 + 1) / 2 - partitionX
        	if l1 == 0:
        		if l2 % 2:
        			return nums2[partitionY-1]
        		else:
        			return (nums2[partitionY-1] + nums2[partitionY]) / 2.0
        	elif l2 == 0:
        		if l1 % 2:
        			return nums1[partitionX-1]
        		else:
        			return (nums1[partitionX-1] + nums1[partitionX]) / 2.0
        	elif l1 == 1 and l2 == 1:
        		return (nums1[partitionX-1] + nums2[partitionY]) / 2.0
        	elif l1 == 1:
        		if partitionX > 0:
        			if nums1[partitionX-1] <= nums2[partitionY]:
        				if (l1 + l2) % 2:
        					return max(nums1[partitionX-1], nums2[partitionY-1])
        				else:
        					return (max(nums1[partitionX-1], nums2[partitionY-1]) + nums2[partitionY]) / 2.0
        			else:
        				end -= 1
        		else:
        			if nums2[partitionY-1] <= nums1[partitionX]:
        				if (l1 + l2) % 2:
        					return nums2[partitionY-1]
        				else:
        					return (nums2[partitionY-1] + min(nums1[partitionX], nums2[partitionY])) / 2.0
        	elif l2 == 1:
        		if partitionY > 0:
        			if nums2[partitionY-1] <= nums1[partitionX]:
        				if (l1 + l2) % 2:
        					return max(nums1[partitionX-1], nums2[partitionY-1])
        				else:
        					return (max(nums1[partitionX-1], nums2[partitionY-1]) + nums1[partitionX]) / 2.0
        			else:
        				start += 1
        		else:
        			if nums1[partitionX-1] <= nums2[partitionY]:
        				if (l1 + l2) % 2:
        					return nums1[partitionX-1]
        				else:
        					return (nums1[partitionX-1] + min(nums2[partitionY], nums1[partitionX])) / 2.0
        			else:
        				end -= 1
        	else:
        		if partitionX > 0 and partitionX != l1 and partitionY > 0 and partitionY != l2:
        			if nums1[partitionX-1] <= nums2[partitionY] and nums2[partitionY-1] <= nums1[partitionX]:
        				if (l1 + l2) % 2:
        					return max(nums1[partitionX-1], nums2[partitionY-1])
        				else:
        					return (max(nums1[partitionX-1], nums2[partitionY-1]) + min(nums2[partitionY], nums1[partitionX])) / 2.0
        			elif nums1[partitionX-1] > nums2[partitionY]:
        				end -= 1
        			else:
        				start += 1
        		elif partitionX == l1:
        			if partitionY > 0 and partitionY != l2:
        				if (l1 + l2) % 2:
        					return max(nums1[partitionX-1], nums2[partitionY-1])
        				else:
        					return (max(nums1[partitionX-1], nums2[partitionY-1]) + nums2[partitionY]) / 2.0
        			else:
        				if (l1 + l2) % 2:
        					return nums1[partitionX-1]
        				else:
        					return (nums1[partitionX-1] + nums2[partitionY]) / 2.0
        		elif partitionY == l2:
        			if partitionX > 0 and partitionX != l1:
        				if (l1 + l2) % 2:
        					return max(nums1[partitionX-1], nums2[partitionY-1])
        				else:
        					return (max(nums1[partitionX-1], nums2[partitionY-1]) + nums1[partitionX]) / 2.0
        			else:
        				if (l1 + l2) % 2:
        					return nums2[partitionY-1]
        				else:
        					return (nums1[partitionX] + nums2[partitionY-1]) / 2.0
        		else:
        			if partitionY == 0:
        				if (l1 + l2) % 2:
        					return nums1[partitionX-1]
        				else:
        					return (nums1[partitionX-1] + min(nums2[partitionY], nums1[partitionX])) / 2.0
        			else:
        				if (l1 + l2) % 2:
        					return nums2[partitionY-1]
        				else:
        					return (nums2[partitionY-1] + min(nums2[partitionY], nums1[partitionX])) / 2.0
        return 0
#
#my_test = Solution()
#nums1 = [1, 2]
#nums2 = []
#print("nums1 = %s" % nums1)
#print("nums2 = %s" % nums2)
#print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))
#
#nums1 = [1, 2, 3]
#nums2 = []
#print("nums1 = %s" % nums1)
#print("nums2 = %s" % nums2)
#print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))
#
#nums1 = [1, 2, 3, 4]
#nums2 = []
#print("nums1 = %s" % nums1)
#print("nums2 = %s" % nums2)
#print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))
#
#nums1 = [1, 2, 3, 3, 3, 4]
#nums2 = []
#print("nums1 = %s" % nums1)
#print("nums2 = %s" % nums2)
#print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))
#
#nums1 = [1]
#nums2 = [2]
#print("nums1 = %s" % nums1)
#print("nums2 = %s" % nums2)
#print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))
#
#nums1 = [1, 3]
#nums2 = [2]
#print("nums1 = %s" % nums1)
#print("nums2 = %s" % nums2)
#print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))
#
#nums1 = [2, 3]
#nums2 = [1]
#print("nums1 = %s" % nums1)
#print("nums2 = %s" % nums2)
#print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))
#
#nums1 = [2]
#nums2 = [1, 3]
#print("nums1 = %s" % nums1)
#print("nums2 = %s" % nums2)
#print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))
#
#nums1 = [1]
#nums2 = [2, 3]
#print("nums1 = %s" % nums1)
#print("nums2 = %s" % nums2)
#print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))
#
#nums1 = [1, 2]
#nums2 = [3, 4]
#print("nums1 = %s" % nums1)
#print("nums2 = %s" % nums2)
#print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))
#
#nums1 = [1, 3]
#nums2 = [2, 4]
#print("nums1 = %s" % nums1)
#print("nums2 = %s" % nums2)
#print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))
#
#nums1 = [1, 4]
#nums2 = [2, 3]
#print("nums1 = %s" % nums1)
#print("nums2 = %s" % nums2)
#print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))
#
#nums1 = [2, 3]
#nums2 = [1, 4]
#print("nums1 = %s" % nums1)
#print("nums2 = %s" % nums2)
#print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))
#
#nums1 = [2, 4]
#nums2 = [1, 3]
#print("nums1 = %s" % nums1)
#print("nums2 = %s" % nums2)
#print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))
#
#nums1 = [1, 2, 2]
#nums2 = [3, 4, 6]
#print("nums1 = %s" % nums1)
#print("nums2 = %s" % nums2)
#print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))
#
#nums1 = [1, 2, 7]
#nums2 = [3, 4]
#print("nums1 = %s" % nums1)
#print("nums2 = %s" % nums2)
#print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))
#
#nums1 = [1, 2, 2, 2, 2, 2, 3, 6]
#nums2 = [3, 4, 6, 7, 7, 8, 9, 9]
#print("nums1 = %s" % nums1)
#print("nums2 = %s" % nums2)
#print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))
#
#nums1 = [1, 2, 2, 2, 2, 2, 3, 3]
#nums2 = [3, 4, 6, 7, 7, 8, 9, 9]
#print("nums1 = %s" % nums1)
#print("nums2 = %s" % nums2)
#print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))
#
#nums1 = [1, 2, 2, 2, 2, 2, 3]
#nums2 = [3, 4, 6, 7, 7, 8, 9, 9]
#print("nums1 = %s" % nums1)
#print("nums2 = %s" % nums2)
#print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))
#
#nums1 = [1, 2, 2, 2, 2, 2, 2, 9]
#nums2 = [3, 4, 6, 7, 7, 8, 9, 9]
#print("nums1 = %s" % nums1)
#print("nums2 = %s" % nums2)
#print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))
#
#nums1 = [100000]
#nums2 = [100001]
#print("nums1 = %s" % nums1)
#print("nums2 = %s" % nums2)
#print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))
#
#nums1 = [1]
#nums2 = [2, 3, 4]
#print("nums1 = %s" % nums1)
#print("nums2 = %s" % nums2)
#print("Mid = %.2f" % (my_test.findMedianSortedArrays(nums1, nums2)))
