public class Solution {
    public bool IsAnagram(string s, string t) {
        int hashFirst = 1;
        int hashSecond = 1;

/*
        foreach (char c in s) {
            if (!sDict.TryAdd(c, 1)) {
                sDict[c] = sDict[c] + 1;
            }
        }

        foreach (char c in t) {
            if (!tDict.TryAdd(c, 1)) {
                tDict[c] = tDict[c] + 1;
            }
        }

        if (sDict.Equals(tDict)) {
            return true;
        }
        */

        foreach (char c in s) {
            hashFirst *= c - 'a' * 31;
        }

        foreach (char c in t) {
            hashSecond *= c - 'a' * 31;
        }

        if (hashFirst == hashSecond) {
            return true;
        }
        return false;
    } 
}
