import java.util.Stack;

public class validParenthesis {

    /**
     * Given a string s containing just the characters '(', ')', '{', '}', '[' and
     * ']', determine if the input string is valid.
     * 
     * An input string is valid if:
     * 
     * Open brackets must be closed by the same type of brackets. Open brackets must
     * be closed in the correct order.
     * 
     * Example 1:
     * 
     * Input: s = "()" 
     * Output: true 
     * 
     * Example 2:
     * Input: s = "()[]{}" Output: true
     * 
     * 
     */
    public static void main(String[] args) {

        final String test = "([])";
        final String test2 = "[{[(])]}";
        System.out.println(isValid(test2));

    }

    public static boolean isValid(String s) {

        // error checking
        if (s == "" || s == null) {
            return false;
        }

        Stack<Character> stack = new Stack<>();

        char[] ch = s.toCharArray();

        for (int i = 0; i < ch.length; i++) {
            // if one of opening parenthesis we add to stack
            if (ch[i] == '{' || ch[i] == '[' || ch[i] == '(') {
                stack.push(ch[i]);
            } else {
                // check first if stack is not empty to avoid null pointer
                if (!stack.isEmpty()) {
                    // get the character from the stack
                    char popped = stack.pop();
                    // helper returns true or false immediately
                    if (!helper(popped, ch[i]))
                        return false;
                } else {
                    return false;
                }
            }

        }

        return stack.isEmpty();

    }

    private static boolean helper(char charFromStack, char currentChar) {
        return (charFromStack == '(' && currentChar == ')' || charFromStack == '[' && currentChar == ']'
                || charFromStack == '{' && currentChar == '}');
    }
}