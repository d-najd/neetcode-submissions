public class Solution {

    private int hashUnique;
    
    public string Encode(IList<string> strs)
    {
        if (strs.Count == 0) {
            return null;
        }
        hashUnique = strs.GetHashCode();
        var endStr = "";
        foreach (var str in strs)
        {
            if (endStr != "")
            {
                endStr += hashUnique;
            }
            endStr += $"{str}";
        }

        return endStr;
    }

    public List<string> Decode(string s)
    {
        if (s == null) {
            new List<string>();
        }
        return s.Split(hashUnique.ToString()).ToList();
    }
}