"""Question 1:
Given a string s containing just the characters &#39;(&#39;, &#39;)&#39;, &#39;{&#39;, &#39;}&#39;, &#39;[&#39; and &#39;]&#39;, determine if the input
string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()";
Output: true
Example 2:
Input: s = "()[]{}";
Output: true
Example 3:
Input: s = "(]"
Output: false

Constraints:
• 1 &lt;= s.length &lt;= 10 4
• s consists of parentheses only &#39;()[]{}’ """

def stringWithParentesis(string):
    brackets = ['()', '{}', '[]']
    while any(ch in string for ch in brackets):
        for br in brackets:
            string = string.replace(br, '')
    return not string


if __name__ == '__main__':
    strings = ["()", "()[]{}", "(]", "{([])}", "{{[]}()}", "{[]}()}"]
    for string in strings:
        print(True if stringWithParentesis(string) else False)
