public class Solution {
    public bool IsAnagram(string s, string t) {
        var dict = new Dictionary<char, int>();
        
        foreach (char c in s) {
            if (!dict.TryAdd(c, 1)) {
                dict[c] = dict[c] + 1;
            }
        }

        foreach (char c in t) {
           if (!dict.TryAdd(c, -1)) {
                dict[c] = dict[c] - 1;
           }
        }

        foreach (var cur in dict) {
            if (cur.Value != 0) {
                return false;
            }
        }

        return true;
    } 
}
