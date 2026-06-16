public class Solution {

    public string Encode(IList<string> strs)
    {
        if (strs.Length == 0) {
            return null;
        }
        var endStr = "";
        foreach (var str in strs)
        {
            if (endStr != "")
            {
                endStr += '\n';
            }
            endStr += $"{str}";
        }

        return endStr;
    }

    public List<string> Decode(string s)
    {
        return s.Split('\n').ToList();
    }
}