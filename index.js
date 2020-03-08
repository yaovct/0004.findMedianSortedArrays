function Index() {
}
// node index.js
/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */
Index.prototype.findMedianSortedArrays = function(nums1, nums2) {
	var l1 = nums1.length;
	var l2 = nums2.length;
	var start = 0;
	var end = l1;
	while (start <= end) {
		var partitionX = Math.floor((start + end + 1) / 2);
		var partitionY = Math.floor((l1 + l2 + 1) / 2) - partitionX;
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
};

//var nums1 = [3, 4, 5];
//var nums2 = [-2, -1];
//
//console.log("The median is " + findMedianSortedArrays(nums1, nums2));

module.exports = Index;
