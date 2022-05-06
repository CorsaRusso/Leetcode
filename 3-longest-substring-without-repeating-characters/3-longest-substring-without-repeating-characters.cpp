class Solution
{
    public:
        int lengthOfLongestSubstring(string s)
        {
            int retval = 0;
            int cur_max = 0;
            int ptnr = 0;
            map<char, int> map1;
            for (int i = 0; i < s.size(); i++)
            {
                if (map1.count(s[i]) > 0) {
                    ptnr = max(ptnr, map1[s[i]] + 1);
                    map1[s[i]] = i;
                    cur_max = i - ptnr;
                    cur_max++;
                    /*cout << "cur_max: " << cur_max << "\n";
                    cout << "i: " << i << "\n";
                    cout << "PTNR: " << ptnr << "\n"; */
                    
                }
                else {
                    map1[s[i]] = i;
                    cur_max++;
                }
                /* map<char, int>::iterator it;

                for (it = map1.begin(); it != map1.end(); it++)
                {
                    cout << "key = " << it->first << " value = " << it->second << endl;
                }
                cout << cur_max << "\n";
                cout << "-----\n"; */
                retval = max(retval, cur_max);
            }
            return retval;
        }
};