#include "index.h"

double Solution::findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
	int l1 = nums1.size();
	int l2 = nums2.size();
	int start = 0, end = l1;
	while(start <= end) {
		int partitionX = (start + end + 1) / 2;
    int partitionY = (l1 + l2 + 1) / 2 - partitionX;
    if(partitionX > 0 && partitionX != l1 && partitionY > 0 && partitionY != l2) {
	    //printf("nums1[%d] = %d <= nums2[%d] = %d && nums2[%d] = %d <= nums1[%d] = %d\n",partitionX-1, nums1[partitionX-1], partitionY, nums2[partitionY], partitionY-1, nums2[partitionY-1], partitionX, nums1[partitionX]);
	    if(nums1[partitionX-1] <= nums2[partitionY] && nums2[partitionY-1] <= nums1[partitionX]) {
	    	//printf("a\n");
	    	if((l1 + l2) % 2 == 1) {
	    		return std::max(nums1[partitionX-1], nums2[partitionY-1]);
	    	} else {
	    		return (std::max(nums1[partitionX-1], nums2[partitionY-1]) + std::min(nums2[partitionY], nums1[partitionX])) / 2.0;
	    	}
	    } else if (nums1[partitionX-1] > nums2[partitionY]) {
	    	end = end - 1;
	    } else {
	    	start = start + 1; // binary search
	    }
    } else if(partitionX == l1) {
    	//printf("1 partitionX = %d, partitionY = %d\n",partitionX, partitionY);
    	if(l2 > 0) {
	    	if(partitionX > 0) {
	    		if(nums1[partitionX-1] <= nums2[partitionY]) {
			    	if((l1 + l2) % 2 == 1) {
			    		if(partitionY == 0 || l2 == 1) {
			    			//printf("c\n");
			    			return nums1[partitionX-1];
			    		} else {
			    			//printf("k\n");
			    			return std::max(nums1[partitionX-1], nums2[partitionY-1]);
			    		}
			    	} else {
			    		//printf("b\n");
			    		if((l1 + l2) % 2 == 1) {
			    			return std::max(nums1[partitionX-1], nums2[partitionY-1]);
			    		} else {
			    			if(partitionY > 0) {
			    				return (std::max(nums1[partitionX-1], nums2[partitionY-1]) + nums2[partitionY]) / 2.0;
			    			} else {
			    				return (nums1[partitionX-1] + nums2[partitionY]) / 2.0;
			    			}
			    		}
			    	}
			    } else {
			    	if(end > 0) {
			    		//printf("eeee\n");
			    		end = end - 1;
			    	} else {
			    		//printf("ffff\n");
			    	}
			    }
			  } else {
			  	if(l2 % 2 == 1) {
			  		return nums2[partitionY-1];
			  	} else {
			  		return (nums2[partitionY-1] + nums2[partitionY]) / 2.0;
			  	}
			  }
			} else {
				return nums1[partitionX-1];
			}
    } else {
    	//printf("2 partitionX = %d, partitionY = %d\n",partitionX, partitionY);
    	if(partitionY > 0) {
	    	if(nums2[partitionY-1] <= nums1[partitionX]) {
		    	if((l1 + l2) % 2 == 1) {
		    		if(partitionX == 0 || l1 == 1) {
		    			//printf("d\n");
		    			return nums2[partitionY-1];
		    		} else {
		    			//printf("e\n");
		    			return std::max(nums1[partitionX-1], nums2[partitionY-1]);
		    		}
		    	} else {
		    		if(partitionX == 0 || l1 == 1) {
		    			//printf("f\n");
		    			if(l2 > 1 && partitionY < l2) {
		    				return (nums2[partitionY-1] + std::min(nums2[partitionY], nums1[partitionX])) / 2.0;
		    			} else {
		    				return (nums2[partitionY-1] + nums1[partitionX]) / 2.0;
		    			}
		    		} else {
		    			//printf("h\n");
		    			if(l2 > 1 && partitionY < l2) {
		    				return (std::max(nums1[partitionX-1],nums2[partitionY-1]) + std::min(nums2[partitionY], nums1[partitionX])) / 2.0;
		    			} else {
		    				return (std::max(nums1[partitionX-1],nums2[partitionY-1]) + nums1[partitionX]) / 2.0;
		    			}
		    		}
		    	}
		    } else {
		    	//printf("gggg\n");
		    	start += 1;
		    }
		  } else {
		  	if(l2 > 0) {
			  	if(nums1[partitionX-1] <= nums2[partitionY]) {
				  	if((l1 + l2) % 2 == 1) {
				  		//printf("i\n");
				  		return nums1[partitionX-1];
				  	} else {
				  		//printf("j\n");
				  		return (nums1[partitionX-1] + std::min(nums2[partitionY], nums1[partitionX])) / 2.0;
				  	}
				  } else {
				  	end = end - 1;
				  }
				} else {
			  	if((l1 + l2) % 2 == 1) {
			  		//printf("k\n");
			  		return nums1[partitionX-1];
			  	} else {
			  		//printf("l\n");
			  		return (nums1[partitionX-1] + nums1[partitionX]) / 2.0;
			  	}
				}
		  }
    }
	}
  return 0;
}