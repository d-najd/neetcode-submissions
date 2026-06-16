public class Solution {

    public string Encode(IList<string> strs)
    {
        var endStr = "";
        foreach (var str in strs)
        {
            if (endStr != "")
            {
                endStr += '\n';
            }
            endStr += $"{str}";
        }

        if (endStr == "") {
            return null;
        }
        return endStr;
    }

    public List<string> Decode(string s)
    {
        return s.Split('\n').ToList();
    }
}