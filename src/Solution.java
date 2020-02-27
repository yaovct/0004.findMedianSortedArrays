// javac src/Solution.java
package src;
import java.lang.*;
import java.util.*;

// interative method
public class Solution {
  public double findMedianSortedArrays(int[] nums1, int[] nums2) {
    int start = 0, end = nums1.length;
    while(start <= end) {
	    int partitionX = (start + end + 1) / 2;
	    int partitionY = (nums1.length + nums2.length + 1) / 2 - partitionX;
	    if(nums1.length == 0) {
	    	if(nums2.length % 2 == 1) {
	    		return nums2[partitionY-1];
	    	} else {
	    		return (nums2[partitionY-1] + nums2[partitionY]) / 2.0;
	    	}
	    }
	    if(nums2.length == 0) {
	    	if(nums1.length % 2 == 1) {
	    		return nums1[partitionX-1];
	    	} else {
	    		return (nums1[partitionX-1] + nums1[partitionX]) / 2.0;
	    	}
	    }
	    if(nums1.length == 1 && nums2.length == 1) {
	    	return (nums1[partitionX-1] + nums2[partitionY]) / 2.0;
	    } else if(nums1.length == 1) {
	    	//System.out.printf("%d %d %d %d\n",start, end, partitionX, partitionY);
	    	if(partitionX > 0) {
		    	if(nums1[partitionX-1] <= nums2[partitionY]) {
		    		if((nums1.length + nums2.length) % 2 == 1) {
				  		return Math.max(nums1[partitionX-1], nums2[partitionY-1]);
				  	} else {
				  		return (Math.max(nums1[partitionX-1], nums2[partitionY-1]) + nums2[partitionY]) / 2.0;
				  	}
		    	} else {
		    		end -= 1;
		    	}
		    } else { // X == 0
		    	//System.out.printf("%d %d %d %d\n",start, end, partitionX, partitionY);
		    	if(nums2[partitionY-1] <= nums1[partitionX]) {
		    		if((nums1.length + nums2.length) % 2 == 1) {
		    			return nums2[partitionY-1];
		    		} else {
		    			return (nums2[partitionY-1] + Math.min(nums1[partitionX], nums2[partitionY])) / 2.0;
		    		}
		    	}
		    }
	    } else if(nums2.length == 1) {
	    	if(partitionY > 0) {
		    	if(nums2[partitionY-1] <= nums1[partitionX]) {
		    		if((nums1.length + nums2.length) % 2 == 1) {
		    			return Math.max(nums1[partitionX-1], nums2[partitionY-1]);
		    		} else {
		    			return (Math.max(nums1[partitionX-1], nums2[partitionY-1]) + nums1[partitionX]) / 2.0;
		    		}
		    	} else {
		    		start += 1;
		    	}
		    } else {
		    	//System.out.printf("%d %d %d %d\n",start, end, partitionX, partitionY);
		    	if(nums1[partitionX-1] <= nums2[partitionY]) {
		    		if((nums1.length + nums2.length) % 2 == 1) {
		    			return nums1[partitionX-1];
		    		} else {
		    			return (nums1[partitionX-1] + Math.min(nums2[partitionY], nums1[partitionX])) / 2.0;
		    		}
		    	} else {
		    		end -= 1;
		    	}
		    }
	    } else { // nums1.length > 1 && nums2.length > 1
	    	//System.out.printf("%d %d %d %d\n",start, end, partitionX, partitionY);
	    	if(partitionX > 0 && partitionX != nums1.length && partitionY > 0 && partitionY != nums2.length) {
		    	if(nums1[partitionX-1] <= nums2[partitionY] && nums2[partitionY-1] <= nums1[partitionX]) {
		    		if((nums1.length + nums2.length) % 2 == 1) {
		    			return Math.max(nums1[partitionX-1], nums2[partitionY-1]);
		    		} else {
		    			return (Math.max(nums1[partitionX-1], nums2[partitionY-1]) + Math.min(nums2[partitionY], nums1[partitionX])) / 2.0;
		    		}
		    	} else if (nums1[partitionX-1] > nums2[partitionY]) {
		    		end -= 1;
		    	} else {
		    		start += 1;
		    	}
		    } else if(partitionX == nums1.length) {
		    	if(partitionY > 0 && partitionY != nums2.length) {
		    		if((nums1.length + nums2.length) % 2 == 1) {
		    			return Math.max(nums1[partitionX-1], nums2[partitionY-1]);
		    		} else {
		    			return (Math.max(nums1[partitionX-1], nums2[partitionY-1]) + nums2[partitionY]) / 2.0;
		    		}
			    } else {
			    	if((nums1.length + nums2.length) % 2 == 1) {
			    		return nums1[partitionX-1];
			    	} else {
			    		return (nums1[partitionX-1] + nums2[partitionY]) / 2.0;
			    	}
			    }
		    } else if(partitionY == nums2.length) {
		    	if(partitionX > 0 && partitionX != nums1.length) {
		    		if((nums1.length + nums2.length) % 2 == 1) {
		    			return Math.max(nums1[partitionX-1], nums2[partitionY-1]);
		    		} else {
		    			return (Math.max(nums1[partitionX-1], nums2[partitionY-1]) + nums1[partitionX]) / 2.0;
		    		}
		    	} else {
		    		if((nums1.length + nums2.length) % 2 == 1) {
		    			return nums2[partitionY-1];
		    		} else {
		    			return (nums1[partitionX] + nums2[partitionY-1]) / 2.0;
		    		}
		    	}
		    } else { // Y == 0
		    	if(partitionY == 0) {
		    		if((nums1.length + nums2.length) % 2 == 1) {
		    			return nums1[partitionX-1];
		    		} else {
		    			return (nums1[partitionX-1] + Math.min(nums2[partitionY], nums1[partitionX])) / 2.0;
		    		}
		    	} else { // partitionX == 0
		    		if((nums1.length + nums2.length) % 2 == 1) {
		    			return nums2[partitionY-1];
		    		} else {
		    			return (nums2[partitionY-1] + Math.min(nums2[partitionY], nums1[partitionX])) / 2.0;
		    		}
		    	}
		    }
		  }
  	}
    return 0;
  }
}
