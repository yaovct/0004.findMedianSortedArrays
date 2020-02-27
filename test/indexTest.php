<?php
// cd ../; phpunit -c phpunit.xml
require_once('index.php');

class SolutionTest extends \PHPUnit_Framework_TestCase
{
  function testFindMedian1()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array(1, 3, 5, 7, 9);
    $nums2 = array(2, 4, 6, 8, 10);
    $this->assertEquals(5.5, $f->findMedianSortedArrays($nums1, $nums2));
  }
  function testFindMedian2()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array(1, 2, 3, 4);
    $nums2 = array(5, 6, 7, 8);
    $this->assertEquals(4.5, $f->findMedianSortedArrays($nums1, $nums2));
  }
  function testFindMedian3()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array(1, 2, 3, 4);
    $nums2 = array(5, 6, 7);
    $this->assertEquals(4, $f->findMedianSortedArrays($nums1, $nums2));
  }
  function testFindMedian4()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array(1, 2, 3, 5);
    $nums2 = array(4, 6, 7);
    $this->assertEquals(4, $f->findMedianSortedArrays($nums1, $nums2));
  }
  function testFindMedian5()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array(4, 6, 7, 8);
    $nums2 = array(1, 2, 3, 5);
    $this->assertEquals(4.5, $f->findMedianSortedArrays($nums1, $nums2));
  }
  function testFindMedian6()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array(3, 4, 5, 6, 7, 8, 9);
    $nums2 = array(1, 2);
    $this->assertEquals(5, $f->findMedianSortedArrays($nums1, $nums2));
  }
  function testFindMedian7()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array(1, 3, 4, 6, 7, 8, 9);
    $nums2 = array(9);
    $this->assertEquals(6.5, $f->findMedianSortedArrays($nums1, $nums2));
  }
  function testFindMedian8()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array(5);
    $nums2 = array(1, 3, 4, 6, 7, 8);
    $this->assertEquals(5, $f->findMedianSortedArrays($nums1, $nums2));
  }
  function testFindMedian9()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array(9);
    $nums2 = array(1, 3, 4, 6, 7, 8);
    $this->assertEquals(6, $f->findMedianSortedArrays($nums1, $nums2));
  }
  function testFindMedian10()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array(9);
    $nums2 = array(1, 3, 4, 6, 7);
    $this->assertEquals(5, $f->findMedianSortedArrays($nums1, $nums2));
  }
  function testFindMedian11()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array(5);
    $nums2 = array(1, 3, 4, 8, 9);
    $this->assertEquals(4.5, $f->findMedianSortedArrays($nums1, $nums2));
  }
  function testFindMedian12()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array();
    $nums2 = array(3, 3, 4, 5, 9, 10);
    $this->assertEquals(4.5, $f->findMedianSortedArrays($nums1, $nums2));
  }
  function testFindMedian13()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array();
    $nums2 = array(3, 3, 4, 9, 10);
    $this->assertEquals(4, $f->findMedianSortedArrays($nums1, $nums2));
  }
  function testFindMedian14()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array(1);
    $nums2 = array();
    $this->assertEquals(1, $f->findMedianSortedArrays($nums1, $nums2));
  }
  function testFindMedian15()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array(1, 2);
    $nums2 = array();
    $this->assertEquals(1.5, $f->findMedianSortedArrays($nums1, $nums2));
  }
  function testFindMedian16()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array(1);
    $nums2 = array(2);
    $this->assertEquals(1.5, $f->findMedianSortedArrays($nums1, $nums2));
  }
  function testFindMedian17()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array(2);
    $nums2 = array(1);
    $this->assertEquals(1.5, $f->findMedianSortedArrays($nums1, $nums2));
  }
  function testFindMedian18()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array(2);
    $nums2 = array(2);
    $this->assertEquals(2, $f->findMedianSortedArrays($nums1, $nums2));
  }
  function testFindMedian19()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array(1);
    $nums2 = array(2, 3, 4);
    $this->assertEquals(2.5, $f->findMedianSortedArrays($nums1, $nums2));
  }
  function testFindMedian20()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array(2, 3, 4);
    $nums2 = array(1);
    $this->assertEquals(2.5, $f->findMedianSortedArrays($nums1, $nums2));
  }
  function testFindMedian21()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array(1, 2, 4);
    $nums2 = array(3);
    $this->assertEquals(2.5, $f->findMedianSortedArrays($nums1, $nums2));
  }
  function testFindMedian22()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array(3, 4);
    $nums2 = array(1, 2);
    $this->assertEquals(2.5, $f->findMedianSortedArrays($nums1, $nums2));
  }
  function testFindMedian23()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array(3, 4, 5, 6);
    $nums2 = array(1, 2);
    $this->assertEquals(3.5, $f->findMedianSortedArrays($nums1, $nums2));
  }
  function testFindMedian24()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array(1, 2, 3, 6);
    $nums2 = array(4, 5);
    $this->assertEquals(3.5, $f->findMedianSortedArrays($nums1, $nums2));
  }
  function testFindMedian25()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array(4, 5);
    $nums2 = array(1, 2, 3);
    $this->assertEquals(3, $f->findMedianSortedArrays($nums1, $nums2));
  }
  function testFindMedian26()
  {
    $f = new Solution;
    /** 這是斷言，就像是 IF 中的等於，左邊必須等於右邊的值，否則就讓 PHPUnit 報錯 */
    $nums1 = array(4, 5);
    $nums2 = array(1, 2, 3, 6);
    $this->assertEquals(3.5, $f->findMedianSortedArrays($nums1, $nums2));
  }
}
?>