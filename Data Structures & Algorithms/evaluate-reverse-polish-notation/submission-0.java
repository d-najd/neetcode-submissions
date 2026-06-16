class Solution {
    Stack<Integer> stack = new Stack<>();

    public int evalRPN(String[] tokens) {

        for (String token : tokens) {
            switch (token) {
                case "+":
                case "-":
                case "*":
                case "/":
                    processExpression(token);
                    break;
                default:
                    stack.push(Integer.parseInt(token));
                    break;
            }
        }

        return stack.pop();
    }

    void processExpression(String token) {
        Integer left = stack.pop();
        Integer right = stack.pop();
        Integer result = 0;

        if (token.equals("+")) {
            result = left + right;
        } else if (token.equals("-")) {
            result = left - right;
        } else if (token.equals("*")) {
            result = left * right;
        } else if (token.equals("/")) {
            result = left / right;
        } 
        stack.push(result);
    }
}
