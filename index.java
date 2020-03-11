//package test;
import java.lang.*;
import java.util.*;

// interative method
class Solution {
  public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    int start = 0, end = nums1.length;
    while(start <= end) {
	    int partitionX = (start + end + 1) / 2;
	    int partitionY = (nums1.length + nums2.length + 1) / 2 - partitionX;
	    //System.out.printf("partitionX = %d, partitionY = %d, start = %d, end = %d\n",partitionX, partitionY, start, end);
	
	    if(partitionX > 0 && partitionX != nums1.length && partitionY > 0 && partitionY != nums2.length) {
		    //System.out.printf("nums1[%d] = %d <= nums2[%d] = %d && nums2[%d] = %d <= nums1[%d] = %d\n",partitionX-1, nums1[partitionX-1], partitionY, nums2[partitionY], partitionY-1, nums2[partitionY-1], partitionX, nums1[partitionX]);
		    if(nums1[partitionX-1] <= nums2[partitionY] && nums2[partitionY-1] <= nums1[partitionX]) {
		    	//System.out.printf("a\n");
		    	if((nums1.length + nums2.length) % 2 == 1) {
		    		return Math.max(nums1[partitionX-1], nums2[partitionY-1]);
		    	} else {
		    		return (Math.max(nums1[partitionX-1], nums2[partitionY-1]) + Math.min(nums2[partitionY], nums1[partitionX])) / 2.0;
		    	}
		    } else if (nums1[partitionX-1] > nums2[partitionY]) {
		    	end = end - 1;
		    } else {
		    	start = start + 1; // binary search
		    }
	    } else if(partitionX == nums1.length) {
	    	//System.out.printf("1 partitionX = %d, partitionY = %d\n",partitionX, partitionY);
	    	if(nums2.length > 0) {
		    	if(partitionX > 0) {
		    		if(nums1[partitionX-1] <= nums2[partitionY]) {
				    	if((nums1.length + nums2.length) % 2 == 1) {
				    		if(partitionY == 0 || nums2.length == 1) {
				    			//System.out.printf("c\n");
				    			return nums1[partitionX-1];
				    		} else {
				    			//System.out.printf("k\n");
				    			return Math.max(nums1[partitionX-1], nums2[partitionY-1]);
				    		}
				    	} else {
				    		//System.out.printf("b\n");
				    		if((nums1.length + nums2.length) % 2 == 1) {
				    			return Math.max(nums1[partitionX-1], nums2[partitionY-1]);
				    		} else {
				    			if(partitionY > 0) {
				    				return (Math.max(nums1[partitionX-1], nums2[partitionY-1]) + nums2[partitionY]) / 2.0;
				    			} else {
				    				return (nums1[partitionX-1] + nums2[partitionY]) / 2.0;
				    			}
				    		}
				    	}
				    } else {
				    	if(end > 0) {
				    		//System.out.print("eeee\n");
				    		end = end - 1;
				    	} else {
				    		//System.out.print("ffff\n");
				    	}
				    }
				  } else {
				  	if(nums2.length % 2 == 1) {
				  		return nums2[partitionY-1];
				  	} else {
				  		return (nums2[partitionY-1] + nums2[partitionY]) / 2.0;
				  	}
				  }
				} else {
					return nums1[partitionX-1];
				}
	    } else {
	    	//System.out.printf("2 partitionX = %d, partitionY = %d\n",partitionX, partitionY);
	    	if(partitionY > 0) {
		    	if(nums2[partitionY-1] <= nums1[partitionX]) {
			    	if((nums1.length + nums2.length) % 2 == 1) {
			    		if(partitionX == 0 || nums1.length == 1) {
			    			//System.out.printf("d\n");
			    			return nums2[partitionY-1];
			    		} else {
			    			//System.out.printf("e\n");
			    			return Math.max(nums1[partitionX-1], nums2[partitionY-1]);
			    		}
			    	} else {
			    		if(partitionX == 0 || nums1.length == 1) {
			    			//System.out.printf("f\n");
			    			if(nums2.length > 1 && partitionY < nums2.length) {
			    				return (nums2[partitionY-1] + Math.min(nums2[partitionY], nums1[partitionX])) / 2.0;
			    			} else {
			    				return (nums2[partitionY-1] + nums1[partitionX]) / 2.0;
			    			}
			    		} else {
			    			//System.out.printf("h\n");
			    			if(nums2.length > 1 && partitionY < nums2.length) {
			    				return (Math.max(nums1[partitionX-1],nums2[partitionY-1]) + Math.min(nums2[partitionY], nums1[partitionX])) / 2.0;
			    			} else {
			    				return (Math.max(nums1[partitionX-1],nums2[partitionY-1]) + nums1[partitionX]) / 2.0;
			    			}
			    		}
			    	}
			    } else {
			    	//System.out.printf("gggg\n");
			    	start += 1;
			    }
			  } else {
			  	if(nums2.length > 0) {
				  	if(nums1[partitionX-1] <= nums2[partitionY]) {
					  	if((nums1.length + nums2.length) % 2 == 1) {
					  		//System.out.printf("i\n");
					  		return nums1[partitionX-1];
					  	} else {
					  		//System.out.printf("j\n");
					  		return (nums1[partitionX-1] + Math.min(nums2[partitionY], nums1[partitionX])) / 2.0;
					  	}
					  } else {
					  	end = end - 1;
					  }
					} else {
				  	if((nums1.length + nums2.length) % 2 == 1) {
				  		//System.out.printf("k\n");
				  		return nums1[partitionX-1];
				  	} else {
				  		//System.out.printf("l\n");
				  		return (nums1[partitionX-1] + nums1[partitionX]) / 2.0;
				  	}
					}
			  }
	    }
  	}
    return 0;
  }
}

public class index {

	public static void main(String[] args) {
    Solution demo = new Solution();
    // a
		int[] nums1 = {1, 3, 5, 7, 9};
		int[] nums2 = {2, 4, 6, 8, 10};
    System.out.printf("1\tMid = %.2f\n", demo.findMedianSortedArrays(nums1, nums2));
    //System.exit(1);

		// cccc, b
		int[] nums3 = {1, 2, 3, 4};
		int[] nums4 = {5, 6, 7, 8};
    System.out.printf("2\tMid = %.2f\n", demo.findMedianSortedArrays(nums3, nums4));

		// cccc, c
		int[] nums5 = {1, 2, 3, 4};
		int[] nums6 = {5, 6, 7};
    System.out.printf("3\tMid = %.2f\n", demo.findMedianSortedArrays(nums5, nums6));

		// cccc, eeee, a
		int[] nums7 = {1, 2, 3, 5};
		int[] nums8 = {4, 6, 7};
    System.out.printf("4\tMid = %.2f\n", demo.findMedianSortedArrays(nums7, nums8));

		// aaaa, a
		int[] nums9 = {4, 6, 7, 8};
		int[] nums10 = {1, 2, 3, 5};
    System.out.printf("5\tMid = %.2f\n", demo.findMedianSortedArrays(nums9, nums10));

		// aaaa, e
		int[] nums11 = {3, 4, 5, 6, 7, 8, 9};
		int[] nums12 = {1, 2};
    System.out.printf("6\tMid = %.2f\n", demo.findMedianSortedArrays(nums11, nums12));    

		// j, 6.5
		int[] nums13 = {1, 3, 4, 6, 7, 8, 9};
		int[] nums14 = {9};
    System.out.printf("7\tMid = %.2f\n", demo.findMedianSortedArrays(nums13, nums14));

		// k
		int[] nums15 = {5};
		int[] nums16 = {1, 3, 4, 6, 7, 8};
    System.out.printf("8\tMid = %.2f\n", demo.findMedianSortedArrays(nums15, nums16));

		// d, 6
		int[] nums17 = {9};
		int[] nums18 = {1, 3, 4, 6, 7, 8};
    System.out.printf("9\tMid = %.2f\n", demo.findMedianSortedArrays(nums17, nums18));

		// eeee, f, 5
		int[] nums19 = {9};
		int[] nums20 = {1, 3, 4, 6, 7};
    System.out.printf("10\tMid = %.2f\n", demo.findMedianSortedArrays(nums19, nums20));

		// eeee, f, 4.5
		int[] nums21 = {5};
		int[] nums22 = {1, 3, 4, 8, 9};
    System.out.printf("11\tMid = %.2f\n", demo.findMedianSortedArrays(nums21, nums22));

		int[] nums23 = {};
		int[] nums24 = {3, 3, 4, 8, 9, 10};
    System.out.printf("12\tMid = %.2f\n", demo.findMedianSortedArrays(nums23, nums24));

		int[] nums25 = {1, 3, 5};
		int[] nums26 = {};
    System.out.printf("13\tMid = %.2f\n", demo.findMedianSortedArrays(nums25, nums26));

		int[] nums27 = {1};
		int[] nums28 = {};
    System.out.printf("14\tMid = %.2f\n", demo.findMedianSortedArrays(nums27, nums28));

		int[] nums29 = {100001};
		int[] nums30 = {100000};
    System.out.printf("15\tMid = %.2f\n", demo.findMedianSortedArrays(nums29, nums30));

		int[] nums31 = {1};
		int[] nums32 = {2,3,4};
    System.out.printf("16\tMid = %.2f\n", demo.findMedianSortedArrays(nums31, nums32));

		// 2.5
		int[] nums33 = {2, 3, 4};
		int[] nums34 = {1};
    System.out.printf("17\tMid = %.2f\n", demo.findMedianSortedArrays(nums33, nums34));

		// 2.5
		int[] nums35 = {1, 2, 4};
		int[] nums36 = {3};
    System.out.printf("18\tMid = %.2f\n", demo.findMedianSortedArrays(nums35, nums36));

		// 2.5
		int[] nums37 = {3, 4};
		int[] nums38 = {1, 2};
    System.out.printf("19\tMid = %.2f\n", demo.findMedianSortedArrays(nums37, nums38));

		// 2.5
		int[] nums39 = {3, 4, 5, 6};
		int[] nums40 = {1, 2};
    System.out.printf("20\tMid = %.2f\n", demo.findMedianSortedArrays(nums39, nums40));

		// 2.5
		int[] nums41 = {1, 2, 3, 6};
		int[] nums42 = {4, 5};
    System.out.printf("21\tMid = %.2f\n", demo.findMedianSortedArrays(nums41, nums42));

		// 2.5
		int[] nums43 = {4, 5};
		int[] nums44 = {1, 2, 3};
    System.out.printf("22\tMid = %.2f\n", demo.findMedianSortedArrays(nums43, nums44));

		// 2.5
		int[] nums45 = {4, 5};
		int[] nums46 = {1, 2, 3, 6};
    System.out.printf("23\tMid = %.2f\n", demo.findMedianSortedArrays(nums45, nums46));
	}
}