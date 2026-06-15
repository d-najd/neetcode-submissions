class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        char[] sArr = s.toCharArray();

        for(char cur : sArr) {
            switch (cur) {
                case '(':
                case '{':
                case '[':
                    stack.push(cur);
                    break;
                case ')':
                    if (stack.isEmpty() || stack.pop() != '(') return false;
                    break;
                case '}':
                    if (stack.isEmpty() || stack.pop() != '{') return false;
                    break;
                case ']':
                    if (stack.isEmpty() || stack.pop() != '[') return false;
                    break;
            }
        }

        if (!stack.isEmpty()) return false;

        return true;
    }
}
