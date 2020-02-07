<?php

class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer[] $nums2
     * @return Float
     */
    function findMedianSortedArrays($nums1, $nums2) {
        $a = array_merge($nums1, $nums2);
        sort($a);
        //print_r($a);
        //print(count($a)/2|0);
        $idx = count($a)/2|0;
        if(count($a) % 2) {
        	return $a[$idx];
        } else {
        	return ($a[$idx-1] + $a[$idx]) / 2;
        }
    }
}

$nums1 = array(1, 2);
$nums2 = array(4, 5, 6);
$testSolution = new Solution();
printf("The median is ".$testSolution->findMedianSortedArrays($nums1, $nums2));


?>