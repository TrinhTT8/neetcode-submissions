#include <unordered_map>
class Solution {
public:
    bool isAnagram(string s, string t) {

        // If the two strings are not equal in size, we know it is not an anagram
        if (s.length() != t.length()){
            return false;
        }

        // Let use hash map to store the occurence of each character
        unordered_map<char,int> countS;
        unordered_map<char,int> countT;

        for (int i=0; i < s.length(); i++){
            // If the character does not exist, we add them to the map
            if (countS.find(s[i]) == countS.end()){
                countS.insert({s[i],1});
            }
            else {
                countS[s[i]] = countS[s[i]] + 1;
            }

            if (countT.find(t[i]) == countT.end()){
                countT.insert({t[i],1});
            }
            else {
                countT[t[i]] = countT[t[i]] + 1;
            }
        }

        if (countS == countT){
            return true;
        }
        return false;
    }
};
