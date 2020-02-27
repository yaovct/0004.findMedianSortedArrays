// https://stackoverflow.com/questions/42430188/junit-error-initializationerrororg-junit-runner-junitcommandlineparseresult
// javac src/Solution.java;javac -cp "junit-4.13.jar; hamcrest-core-1.3.jar;src/Solution.class;." test/SolutionTest.java;java -cp "junit-4.13.jar;hamcrest-core-1.3.jar;src/Solution.class;test/SolutionTest.class;." org.junit.runner.JUnitCore test.SolutionTest
package test;
import static org.junit.Assert.*;
import org.junit.*;
import src.Solution;

public class SolutionTest {

 Solution myClass = new Solution();

	@Test
	public void findMedian1() { 
		int[] nums1 = {1, 3, 5, 7, 9};
		int[] nums2 = {2, 4, 6, 8, 10};
		assertEquals(5.50, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
	@Test
	public void findMedian2() { 
		int[] nums1 = {1, 2, 3, 4};
		int[] nums2 = {5, 6, 7, 8};
		assertEquals(4.50, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
	@Test
	public void findMedian3() { 
		int[] nums1 = {1, 2, 3, 4};
		int[] nums2 = {5, 6, 7};
		assertEquals(4.00, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
	@Test
	public void findMedian4() { 
		int[] nums1 = {1, 2, 3, 5};
		int[] nums2 = {4, 6, 7};
		assertEquals(4.00, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
	@Test
	public void findMedian5() { 
		int[] nums1 = {4, 6, 7, 8};
		int[] nums2 = {1, 2, 3, 5};
		assertEquals(4.50, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
	@Test
	public void findMedian6() { 
		int[] nums1 = {3, 4, 5, 6, 7, 8, 9};
		int[] nums2 = {1, 2};
		assertEquals(5.00, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
	@Test
	public void findMedian7() { 
		int[] nums1 = {1, 3, 4, 6, 7, 8, 9};
		int[] nums2 = {9};
		assertEquals(6.50, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
	@Test
	public void findMedian8() { 
		int[] nums1 = {5};
		int[] nums2 = {1, 3, 4, 6, 7, 8};
		assertEquals(5.00, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
	@Test
	public void findMedian9() { 
		int[] nums1 = {9};
		int[] nums2 = {1, 3, 4, 6, 7, 8};
		assertEquals(6.00, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
	@Test
	public void findMedian10() { 
		int[] nums1 = {9};
		int[] nums2 = {1, 3, 4, 6, 7};
		assertEquals(5.00, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
	@Test
	public void findMedian11() { 
		int[] nums1 = {5};
		int[] nums2 = {1, 3, 4, 8, 9};
		assertEquals(4.50, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
	@Test
	public void findMedian12() { 
		int[] nums1 = {};
		int[] nums2 = {3, 3, 4, 5, 9, 10};
		assertEquals(4.50, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
	@Test
	public void findMedian13() { 
		int[] nums1 = {};
		int[] nums2 = {3, 3, 4, 9, 10};
		assertEquals(4.00, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
	@Test
	public void findMedian14() { 
		int[] nums1 = {1};
		int[] nums2 = {};
		assertEquals(1.00, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
	@Test
	public void findMedian15() { 
		int[] nums1 = {1, 2};
		int[] nums2 = {};
		assertEquals(1.50, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
	@Test
	public void findMedian16() { 
		int[] nums1 = {1};
		int[] nums2 = {2};
		assertEquals(1.50, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
	@Test
	public void findMedian17() { 
		int[] nums1 = {2};
		int[] nums2 = {1};
		assertEquals(1.50, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
	@Test
	public void findMedian18() { 
		int[] nums1 = {2};
		int[] nums2 = {2};
		assertEquals(2.00, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
	@Test
	public void findMedian19() { 
		int[] nums1 = {1};
		int[] nums2 = {2, 3, 4};
		assertEquals(2.50, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
	@Test
	public void findMedian20() { 
		int[] nums1 = {2, 3, 4};
		int[] nums2 = {1};
		assertEquals(2.50, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
	@Test
	public void findMedian21() { 
		int[] nums1 = {1, 2, 4};
		int[] nums2 = {3};
		assertEquals(2.50, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
	@Test
	public void findMedian22() { 
		int[] nums1 = {3, 4};
		int[] nums2 = {1, 2};
		assertEquals(2.50, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
	@Test
	public void findMedian23() { 
		int[] nums1 = {3, 4, 5, 6};
		int[] nums2 = {1, 2};
		assertEquals(3.50, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
	@Test
	public void findMedian24() { 
		int[] nums1 = {1, 2, 3, 6};
		int[] nums2 = {4, 5};
		assertEquals(3.50, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
	@Test
	public void findMedian25() { 
		int[] nums1 = {4, 5};
		int[] nums2 = {1, 2, 3};
		assertEquals(3.00, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
	@Test
	public void findMedian26() { 
		int[] nums1 = {4, 5};
		int[] nums2 = {1, 2, 3, 6};
		assertEquals(3.50, myClass.findMedianSortedArrays(nums1, nums2), 0.01);
	}
}