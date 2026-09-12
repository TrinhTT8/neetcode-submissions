#include <stack>
#include <unordered_map>
#include <string>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        //Stack: FIFO
        //Stack can only be push and pop on top

        //Initiate a stack and push in each opening bracket
        //If we met with a closing bracket, we pop the stack but if the closing
        //bracket does not match with the opening bracket, we know the string is not valid
        unordered_map<char, char> openAndClose = {
            {')', '('},
            {']', '['},
            {'}', '{'},
        };

        stack<char> brackets;

        for (char c : s){
            // Check if the character is a valid closing bracket (or a key)
            if (openAndClose.count(c)) {
                if( !brackets.empty() && brackets.top() == openAndClose[c]){
                    brackets.pop();
                } else {
                    return false;
                }
            } else {
                brackets.push(c);
            }
        }
        return brackets.empty();
    }
};
