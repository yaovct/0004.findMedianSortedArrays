#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
  double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
  	vector<int> n(nums1);
  	if(nums2.size() > 0) {
  		n.insert(n.end(), nums2.begin(), nums2.end());
  	}
  	sort(n.begin(), n.end());
  	for(int i=0; i<n.size(); i++) {
  		cout << n[i] << " ";
  	}
  	cout << '\n';
  	if(n.size() % 2) {
  		return n[n.size()/2];
  	} else {
  		return (n[n.size()/2-1] + n[n.size()/2]) / 2.0;
  	}
 	}
};

int main(int argc, char *argv[]) {
	int nums1[8] = {1, 2, 2, 2, 2, 2, 3};
	int nums2[8] = {3, 4, 6, 7, 7, 8, 9, 9};
	//int nums1[8] = {3, 4, 6, 7, 7, 8, 9, 9};
	//int nums2[8] = {1, 2, 2, 2, 2, 2, 3, 6};
	vector<int> arr1(nums1, nums1+8); // convert array to vector
	vector<int> arr2(nums2, nums2+8); // convert array to vector
	for(int j=1; j<=8; j*=2) {
		arr1.resize(8/j);
		for(int i=0; i<arr1.size(); i++) {
			cout << arr1[i] << " ";
		}
		cout << ", ";
		arr2.resize(8/j);
		for(int i=0; i<arr2.size(); i++) {
			cout << arr2[i] << " ";
		}
		cout << endl;
		Solution mySolution;
		cout << "The median is " << mySolution.findMedianSortedArrays(arr1, arr2) << endl;
	}
}