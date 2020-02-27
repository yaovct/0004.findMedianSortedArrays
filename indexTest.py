from index import Solution
import unittest

class SolutionTest(unittest.TestCase):

	def test_findMedian1(self):
		my_test = Solution()
		nums1 = [1, 3, 5, 7, 9]
		nums2 = [2, 4, 6, 8, 10]
		self.assertEqual(5.50, my_test.findMedianSortedArrays(nums1, nums2), 0.01)
	
	def test_findMedian2(self):
		my_test = Solution()
		nums1 = [1, 2, 3, 4]
		nums2 = [5, 6, 7, 8]
		self.assertEqual(4.50, my_test.findMedianSortedArrays(nums1, nums2), 0.01)
	
	def test_findMedian3(self):
		my_test = Solution()
		nums1 = [1, 2, 3, 4]
		nums2 = [5, 6, 7]
		self.assertEqual(4.00, my_test.findMedianSortedArrays(nums1, nums2), 0.01)
	
	def test_findMedian4(self):
		my_test = Solution()
		nums1 = [1, 2, 3, 5]
		nums2 = [4, 6, 7]
		self.assertEqual(4.00, my_test.findMedianSortedArrays(nums1, nums2), 0.01)
	
	def test_findMedian5(self):
		my_test = Solution()
		nums1 = [4, 6, 7, 8]
		nums2 = [1, 2, 3, 5]
		self.assertEqual(4.50, my_test.findMedianSortedArrays(nums1, nums2), 0.01)
	
	def test_findMedian6(self):
		my_test = Solution()
		nums1 = [3, 4, 5, 6, 7, 8, 9]
		nums2 = [1, 2]
		self.assertEqual(5.00, my_test.findMedianSortedArrays(nums1, nums2), 0.01)
	
	def test_findMedian7(self):
		my_test = Solution()
		nums1 = [1, 3, 4, 6, 7, 8, 9]
		nums2 = [9]
		self.assertEqual(6.50, my_test.findMedianSortedArrays(nums1, nums2), 0.01)
	
	def test_findMedian8(self):
		my_test = Solution()
		nums1 = [5]
		nums2 = [1, 3, 4, 6, 7, 8]
		self.assertEqual(5.00, my_test.findMedianSortedArrays(nums1, nums2), 0.01)
	
	def test_findMedian9(self):
		my_test = Solution()
		nums1 = [9]
		nums2 = [1, 3, 4, 6, 7, 8]
		self.assertEqual(6.00, my_test.findMedianSortedArrays(nums1, nums2), 0.01)
	
	def test_findMedian10(self):
		my_test = Solution()
		nums1 = [9]
		nums2 = [1, 3, 4, 6, 7]
		self.assertEqual(5.00, my_test.findMedianSortedArrays(nums1, nums2), 0.01);
	
	def test_findMedian11(self):
		my_test = Solution()
		nums1 = [5]
		nums2 = [1, 3, 4, 8, 9]
		self.assertEqual(4.50, my_test.findMedianSortedArrays(nums1, nums2), 0.01)
	
	def test_findMedian12(self):
		my_test = Solution()
		nums1 = []
		nums2 = [3, 3, 4, 5, 9, 10]
		self.assertEqual(4.50, my_test.findMedianSortedArrays(nums1, nums2), 0.01)
	
	def test_findMedian13(self):
		my_test = Solution()
		nums1 = []
		nums2 = [3, 3, 4, 9, 10]
		self.assertEqual(4.00, my_test.findMedianSortedArrays(nums1, nums2), 0.01)
	
	def test_findMedian14(self):
		my_test = Solution()
		nums1 = [1]
		nums2 = []
		self.assertEqual(1.00, my_test.findMedianSortedArrays(nums1, nums2), 0.01)
	
	def test_findMedian15(self):
		my_test = Solution()
		nums1 = [1, 2]
		nums2 = []
		self.assertEqual(1.50, my_test.findMedianSortedArrays(nums1, nums2), 0.01)
	
	def test_findMedian16(self):
		my_test = Solution()
		nums1 = [1]
		nums2 = [2]
		self.assertEqual(1.50, my_test.findMedianSortedArrays(nums1, nums2), 0.01)
	
	def test_findMedian17(self):
		my_test = Solution()
		nums1 = [2]
		nums2 = [1]
		self.assertEqual(1.50, my_test.findMedianSortedArrays(nums1, nums2), 0.01)
	
	def test_findMedian18(self):
		my_test = Solution()
		nums1 = [2]
		nums2 = [2]
		self.assertEqual(2.00, my_test.findMedianSortedArrays(nums1, nums2), 0.01)
	
	def test_findMedian19(self):
		my_test = Solution()
		nums1 = [1]
		nums2 = [2, 3, 4]
		self.assertEqual(2.50, my_test.findMedianSortedArrays(nums1, nums2), 0.01)
	
	def test_findMedian20(self):
		my_test = Solution()
		nums1 = [2, 3, 4]
		nums2 = [1]
		self.assertEqual(2.50, my_test.findMedianSortedArrays(nums1, nums2), 0.01)
	
	def test_findMedian21(self):
		my_test = Solution()
		nums1 = [1, 2, 4]
		nums2 = [3]
		self.assertEqual(2.50, my_test.findMedianSortedArrays(nums1, nums2), 0.01)
	
	def test_findMedian22(self):
		my_test = Solution()
		nums1 = [3, 4]
		nums2 = [1, 2]
		self.assertEqual(2.50, my_test.findMedianSortedArrays(nums1, nums2), 0.01)
	
	def test_findMedian23(self):
		my_test = Solution()
		nums1 = [3, 4, 5, 6]
		nums2 = [1, 2]
		self.assertEqual(3.50, my_test.findMedianSortedArrays(nums1, nums2), 0.01)
	
	def test_findMedian24(self):
		my_test = Solution()
		nums1 = [1, 2, 3, 6]
		nums2 = [4, 5]
		self.assertEqual(3.50, my_test.findMedianSortedArrays(nums1, nums2), 0.01)
	
	def test_findMedian25(self):
		my_test = Solution()
		nums1 = [4, 5]
		nums2 = [1, 2, 3]
		self.assertEqual(3.00, my_test.findMedianSortedArrays(nums1, nums2), 0.01)
	
	def test_findMedian26(self):
		my_test = Solution()
		nums1 = [4, 5]
		nums2 = [1, 2, 3, 6]
		self.assertEqual(3.50, my_test.findMedianSortedArrays(nums1, nums2), 0.01)
	
if __name__ == '__main__':
    unittest.main()