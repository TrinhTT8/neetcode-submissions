#include <algorithm>

class Solution {
public:
    int findMin(vector<int> &nums) {

    // So the first element in the original array is always the smallest
    // We need to keep track of the first element

    // If the array rotated n times where n equals to the size of the array then 
    // the minimum is always the first element

    // Binary search
    // Find the pivot which can be the middle value
        int l = 0;
        int r = nums.size() - 1;

        while (l < r){
            int m = (l + r)/2;
            if (nums[m] < nums[r]){
                r = m;
            } else {
                l = m + 1;
            }
        }
        return nums[l];
    }
};
