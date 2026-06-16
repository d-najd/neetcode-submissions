public class Solution {

    private int hashUnique;
    
    public string Encode(IList<string> strs)
    {
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
        return s.Split(hashUnique.ToString()).ToList();
    }
}