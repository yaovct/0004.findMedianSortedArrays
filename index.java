import java.lang.*;
import java.util.*;

class Solution {
  public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    int[] n = new int[nums1.length + nums2.length];
    for(int i = 0; i  < nums1.length; i++) {
    	n[i] = nums1[i];
    }
    for(int j = 0; j  < nums2.length; j++) {
    	n[nums1.length + j] = nums2[j];
    }
    Arrays.sort(n);
    if(n.length % 2 == 1) {
    	return n[n.length/2];
    } else {
    	return (n[n.length/2-1] + n[n.length/2]) / 2.0;
    }
  }
}

public class index {

	public static void main(String[] args) {
		int[] nums1 = {1, 2, 3};
		int[] nums2 = {4, 5, 6};

    Solution demo = new Solution();
    System.out.printf("Mid = %.2f\n", demo.findMedianSortedArrays(nums1, nums2));

		int[] nums3 = {1, 3, 5};
		int[] nums4 = {2, 4, 6};
    System.out.printf("Mid = %.2f\n", demo.findMedianSortedArrays(nums3, nums4));

		int[] nums5 = {1, 2, 6};
		int[] nums6 = {3, 4, 5};
    System.out.printf("Mid = %.2f\n", demo.findMedianSortedArrays(nums5, nums6));

		int[] nums7 = {};
		int[] nums8 = {4, 5, 6};
    System.out.printf("Mid = %.2f\n", demo.findMedianSortedArrays(nums7, nums8));
	}
}