class MinStack {
    Stack<Integer> stack;
    Integer minElement = null;


    public MinStack() {
        stack = new Stack<Integer>();
    }
    
    public void push(int val) {
        if (minElement == null || minElement > val) {
            minElement = val;
        }
        stack.push(val);
    }
    
    public void pop() {
        Integer cur = stack.pop();
        if (minElement != null && minElement.equals(cur)) {
            minElement = null;
        }
    }
    
    public int top() {
        return stack.peek();
    }
    
    public int getMin() {
        if (minElement == null) {
            System.out.println("HELLO");
            minElement = Integer.MAX_VALUE;
            for (Integer cur : stack) {
                if (minElement > cur) {
                    minElement = cur;
                }
            }
        }
        return minElement;
    }
}
