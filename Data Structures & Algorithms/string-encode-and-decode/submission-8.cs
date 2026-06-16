public class Solution {

    public string Encode(IList<string> strs)
    {
        if (strs.Count == 0) {
            return null;
        }

        var endStr = "";
        foreach (var str in strs)
        {
            if (endStr != "")
            {
                endStr += "\\n";
            }
            endStr += $"{str}";
        }

        return endStr;
    }

    public List<string> Decode(string s)
    {
        if (s == null) {
            return new List<string>();
        }
        return s.Split("\\n").ToList();
    }
}