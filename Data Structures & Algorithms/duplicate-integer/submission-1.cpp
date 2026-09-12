#include <unordered_set>

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> myset;

        // Iterate through the vector
        for (int i=0; i<nums.size(); i++){
            // Check if the hash set has the number or not
            if (!myset.count(nums[i])){
                myset.insert(nums[i]);
            }
            else {
                return true;
            }
        }
        return false;
    }
};