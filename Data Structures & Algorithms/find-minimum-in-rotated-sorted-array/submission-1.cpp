#include <algorithm>

class Solution {
public:
    int findMin(vector<int> &nums) {

      // So the first element in the original array is always the smallest
      // We need to keep track of the first element

      // If the array rotated n times where n equals to the size of the array then 
      // the minimum is always the first element

      int min = *min_element(nums.begin(), nums.end());
      return min;
    }
};
