describe('findMedianSortedArrays', () => {
	var Index = require('../../index.js');
	var index;
  
  beforeEach(function() {
    index = new Index();
  });

  it("Ex1", function() {
  	var nums1 = [1, 3, 5, 7, 9];
  	var nums2 = [2, 4, 6, 8, 10];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(5.5);
  });

  it("Ex2", function() {
  	var nums1 = [1, 2, 3, 4];
  	var nums2 = [5, 6, 7, 8];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(4.5);
  });

  it("Ex3", function() {
  	var nums1 = [1, 2, 3, 4];
  	var nums2 = [5, 6, 7];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(4);
  });
  
  it("Ex4", function() {
  	var nums1 = [1, 2, 3, 5];
  	var nums2 = [4, 6, 7];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(4);
  });
  
  it("Ex5", function() {
  	var nums1 = [4, 6, 7, 8];
  	var nums2 = [1, 2, 3, 5];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(4.5);
  });
  
  it("Ex6", function() {
  	var nums1 = [3, 4, 5, 6, 7, 8, 9];
  	var nums2 = [1, 2];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(5);
  });
  
  it("Ex7", function() {
  	var nums1 = [1, 3, 4, 6, 7, 8, 9];
  	var nums2 = [9];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(6.5);
  });
  
  it("Ex8", function() {
  	var nums1 = [5];
  	var nums2 = [1, 3, 4, 6, 7, 8];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(5);
  });
  
  it("Ex9", function() {
  	var nums1 = [9];
  	var nums2 = [1, 3, 4, 6, 7, 8];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(6);
  });
  
  it("Ex10", function() {
  	var nums1 = [9];
  	var nums2 = [1, 3, 4, 6, 7];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(5);
  });
  
  it("Ex11", function() {
  	var nums1 = [5];
  	var nums2 = [1, 3, 4, 8, 9];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(4.5);
  });
  
  it("Ex12", function() {
  	var nums1 = [];
  	var nums2 = [3, 3, 4, 5, 9, 10];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(4.5);
  });
  
  it("Ex13", function() {
  	var nums1 = [];
  	var nums2 = [3, 3, 4, 9, 10];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(4);
  });
  
  it("Ex14", function() {
  	var nums1 = [1];
  	var nums2 = [];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(1);
  });
  
  it("Ex15", function() {
  	var nums1 = [1, 2];
  	var nums2 = [];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(1.5);
  });
  
  it("Ex16", function() {
  	var nums1 = [1];
  	var nums2 = [2];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(1.5);
  });
  
  it("Ex17", function() {
  	var nums1 = [2];
  	var nums2 = [1];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(1.5);
  });
  
  it("Ex18", function() {
  	var nums1 = [2];
  	var nums2 = [2];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(2);
  });
  
  it("Ex19", function() {
  	var nums1 = [1];
  	var nums2 = [2, 3, 4];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(2.5);
  });
  
  it("Ex20", function() {
  	var nums1 = [2, 3, 4];
  	var nums2 = [1];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(2.5);
  });
  
  it("Ex21", function() {
  	var nums1 = [1, 2, 4];
  	var nums2 = [3];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(2.5);
  });
  
  it("Ex22", function() {
  	var nums1 = [3, 4];
  	var nums2 = [1, 2];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(2.5);
  });
  
  it("Ex23", function() {
  	var nums1 = [3, 4, 5, 6];
  	var nums2 = [1, 2];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(3.5);
  });
  
  it("Ex24", function() {
  	var nums1 = [1, 2, 3, 6];
  	var nums2 = [4, 5];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(3.5);
  });
  
  it("Ex25", function() {
  	var nums1 = [4, 5];
  	var nums2 = [1, 2, 3];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(3);
  });
  
  it("Ex26", function() {
  	var nums1 = [4, 5];
  	var nums2 = [1, 2, 3, 6];
    expect(index.findMedianSortedArrays(nums1, nums2)).toEqual(3.5);
  });

});