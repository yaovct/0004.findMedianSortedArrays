<?php

class Solution {

  /**
   * @param Integer[] $nums1
   * @param Integer[] $nums2
   * @return Float
   */
  function findMedianSortedArrays($nums1, $nums2) {
  	$l1 = count($nums1);
  	$l2 = count($nums2);
  	$start = 0;
  	$end = $l1;
  	while($start <= $end) {
  		$partitionX = floor(($start + $end + 1) / 2);
  		$partitionY = floor(($l1 + $l2 + 1) / 2) - $partitionX;
  		if(!$l1) {
  			if($l2 % 2) {
  				return $nums2[$partitionY-1];
  			} else {
  				return ($nums2[$partitionY-1] + $nums2[$partitionY]) / 2;
  			}
  		} else if(!$l2) {
  			if($l1 % 2) {
  				return $nums1[$partitionX-1];
  			} else {
  				return ($nums1[$partitionX-1] + $nums1[$partitionX]) / 2;
  			}
  		} else if($l1 == 1 && $l2 == 1) {
  			return ($nums1[$partitionX-1] + $nums2[$partitionY]) / 2;
  		} else if($l1 == 1) {
  			if($partitionX > 0) {
  				if($nums1[$partitionX-1] <= $nums2[$partitionY]) {
  					if(($l1 + $l2) % 2) {
  						return max($nums1[$partitionX-1], $nums2[$partitionY-1]);
  					} else {
  						return (max($nums1[$partitionX-1], $nums2[$partitionY-1]) + $nums2[$partitionY]) / 2;
  					}
  				} else {
  					$end -= 1;
  				}
  			} else {
  				if($nums2[$partitionY-1] <= $nums1[$partitionX]) {
  					if(($l1 + $l2) % 2) {
  						return $nums2[$partitionY-1];
  					} else {
  						return ($nums2[$partitionY-1] + min($nums1[$partitionX], $nums2[$partitionY])) / 2;
  					}
  				}
  			}
  		} else if($l2 == 1) {
  			if($partitionY > 0) {
  				if($nums2[$partitionY-1] <= $nums1[$partitionX]) {
  					if(($l1 + $l2) % 2) {
  						return max($nums1[$partitionX-1], $nums2[$partitionY-1]);
  					} else {
  						return (max($nums1[$partitionX-1], $nums2[$partitionY-1]) + $nums1[$partitionX]) / 2;
  					}
  				} else {
  					$start += 1;
  				}
  			} else {
  				if($nums1[$partitionX-1] <= $nums2[$partitionY]) {
  					if(($l1 + $l2) % 2) {
  						return $nums1[$partitionX-1];
  					} else {
  						return ($nums1[$partitionX-1] + min($nums1[$partitionX], $nums2[$partitionY])) / 2;
  					}
  				} else {
  					$end -= 1;
  				}
  			}
  		} else {
	    	if($partitionX > 0 && $partitionX != $l1 && $partitionY > 0 && $partitionY != $l2) {
		    	if($nums1[$partitionX-1] <= $nums2[$partitionY] && $nums2[$partitionY-1] <= $nums1[$partitionX]) {
		    		if(($l1 + $l2) % 2 == 1) {
		    			return max($nums1[$partitionX-1], $nums2[$partitionY-1]);
		    		} else {
		    			return (max($nums1[$partitionX-1], $nums2[$partitionY-1]) + min($nums2[$partitionY], $nums1[$partitionX])) / 2;
		    		}
		    	} else if ($nums1[$partitionX-1] > $nums2[$partitionY]) {
		    		$end -= 1;
		    	} else {
		    		$start += 1;
		    	}
		    } else if($partitionX == $l1) {
		    	if($partitionY > 0 && $partitionY != $l2) {
		    		if(($l1 + $l2) % 2 == 1) {
		    			return max($nums1[$partitionX-1], $nums2[$partitionY-1]);
		    		} else {
		    			return (max($nums1[$partitionX-1], $nums2[$partitionY-1]) + $nums2[$partitionY]) / 2;
		    		}
			    } else {
			    	if(($l1 + $l2) % 2 == 1) {
			    		return $nums1[$partitionX-1];
			    	} else {
			    		return ($nums1[$partitionX-1] + $nums2[$partitionY]) / 2;
			    	}
			    }
		    } else if($partitionY == $l2) {
		    	if($partitionX > 0 && $partitionX != $l1) {
		    		if(($l1 + $l2) % 2 == 1) {
		    			return max($nums1[$partitionX-1], $nums2[$partitionY-1]);
		    		} else {
		    			return (max($nums1[$partitionX-1], $nums2[$partitionY-1]) + $nums1[$partitionX]) / 2;
		    		}
		    	} else {
		    		if(($l1 + $l2) % 2 == 1) {
		    			return $nums2[$partitionY-1];
		    		} else {
		    			return ($nums1[$partitionX] + $nums2[$partitionY-1]) / 2;
		    		}
		    	}
		    } else {
		    	if($partitionY == 0) {
		    		if(($l1 + $l2) % 2 == 1) {
		    			return $nums1[$partitionX-1];
		    		} else {
		    			return ($nums1[$partitionX-1] + min($nums2[$partitionY], $nums1[$partitionX])) / 2;
		    		}
		    	} else { // partitionX == 0
		    		if(($l1 + $l2) % 2 == 1) {
		    			return $nums2[$partitionY-1];
		    		} else {
		    			return ($nums2[$partitionY-1] + min($nums2[$partitionY], $nums1[$partitionX])) / 2;
		    		}
		    	}
		    }
  		}
  	}
  	return 0;
  }
}

?>