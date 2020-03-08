#include<stdio.h>
#include<stdlib.h>

#define MAX_STRING_SIZE 40

/**
 * Find maximum between two numbers.
 */
int max(int num1, int num2) {
  return (num1 > num2 ) ? num1 : num2;
}

/**
 * Find minimum between two numbers.
 */
int min(int num1, int num2) {
  return (num1 > num2 ) ? num2 : num1;
}

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size){
	int start = 0, end = nums1Size;
	while(start <= end) {
		int partitionX = (start + end + 1) / 2;
    int partitionY = (nums1Size + nums2Size + 1) / 2 - partitionX;
    printf("%d %d %d %d\n",partitionX, partitionY, nums1Size, nums2Size);
    if(partitionX > 0 && partitionX != nums1Size && partitionY > 0 && partitionY != nums2Size) {
	    //printf("nums1[%d] = %d <= nums2[%d] = %d && nums2[%d] = %d <= nums1[%d] = %d\n",partitionX-1, nums1[partitionX-1], partitionY, nums2[partitionY], partitionY-1, nums2[partitionY-1], partitionX, nums1[partitionX]);
	    if(nums1[partitionX-1] <= nums2[partitionY] && nums2[partitionY-1] <= nums1[partitionX]) {
	    	//printf("a\n");
	    	if((nums1Size + nums2Size) % 2 == 1) {
	    		return max(nums1[partitionX-1], nums2[partitionY-1]);
	    	} else {
	    		return (max(nums1[partitionX-1], nums2[partitionY-1]) + min(nums2[partitionY], nums1[partitionX])) / 2.0;
	    	}
	    } else if (nums1[partitionX-1] > nums2[partitionY]) {
	    	end = end - 1;
	    } else {
	    	start = start + 1; // binary search
	    }
    } else if(partitionX == nums1Size) {
    	//printf("1 partitionX = %d, partitionY = %d\n",partitionX, partitionY);
    	if(nums2Size > 0) {
	    	if(partitionX > 0) {
	    		if(nums1[partitionX-1] <= nums2[partitionY]) {
			    	if((nums1Size + nums2Size) % 2 == 1) {
			    		if(partitionY == 0 || nums2Size == 1) {
			    			//printf("c\n");
			    			return nums1[partitionX-1];
			    		} else {
			    			//printf("k\n");
			    			return max(nums1[partitionX-1], nums2[partitionY-1]);
			    		}
			    	} else {
			    		//printf("b\n");
			    		if((nums1Size + nums2Size) % 2 == 1) {
			    			return max(nums1[partitionX-1], nums2[partitionY-1]);
			    		} else {
			    			if(partitionY > 0) {
			    				return (max(nums1[partitionX-1], nums2[partitionY-1]) + nums2[partitionY]) / 2.0;
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
			  	if(nums2Size % 2 == 1) {
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
		    	if((nums1Size + nums2Size) % 2 == 1) {
		    		if(partitionX == 0 || nums1Size == 1) {
		    			//printf("d\n");
		    			return nums2[partitionY-1];
		    		} else {
		    			//printf("e\n");
		    			return max(nums1[partitionX-1], nums2[partitionY-1]);
		    		}
		    	} else {
		    		if(partitionX == 0 || nums1Size == 1) {
		    			//printf("f\n");
		    			if(nums2Size > 1 && partitionY < nums2Size) {
		    				return (nums2[partitionY-1] + min(nums2[partitionY], nums1[partitionX])) / 2.0;
		    			} else {
		    				return (nums2[partitionY-1] + nums1[partitionX]) / 2.0;
		    			}
		    		} else {
		    			//printf("h\n");
		    			if(nums2Size > 1 && partitionY < nums2Size) {
		    				return (max(nums1[partitionX-1],nums2[partitionY-1]) + min(nums2[partitionY], nums1[partitionX])) / 2.0;
		    			} else {
		    				return (max(nums1[partitionX-1],nums2[partitionY-1]) + nums1[partitionX]) / 2.0;
		    			}
		    		}
		    	}
		    } else {
		    	//printf("gggg\n");
		    	start += 1;
		    }
		  } else {
		  	if(nums2Size > 0) {
			  	if(nums1[partitionX-1] <= nums2[partitionY]) {
				  	if((nums1Size + nums2Size) % 2 == 1) {
				  		//printf("i\n");
				  		return nums1[partitionX-1];
				  	} else {
				  		//printf("j\n");
				  		return (nums1[partitionX-1] + min(nums2[partitionY], nums1[partitionX])) / 2.0;
				  	}
				  } else {
				  	end = end - 1;
				  }
				} else {
			  	if((nums1Size + nums2Size) % 2 == 1) {
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

int main(int argc, char *argv[]) {
	int nums1[] = {1, 2, 2, 2, 2, 2, 3};
	int nums2[] = {3, 4, 6, 7, 7, 8, 9, 9};
	printf("The median is %.2f\n", findMedianSortedArrays(nums1, sizeof(nums1)/sizeof(int), nums2, sizeof(nums2)/sizeof(int)));
}