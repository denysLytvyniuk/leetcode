class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        n = len(s)
        words_l = len(words)
        word_l = len(words[0])
        if word_l * words_l > n:
            return []
        if words_l * word_l == n:
            if ''.join(words) == s:
                return [0]
        if len(set(words)) == 1 and len(set(s)) == 1:
            if words[0] == s[0]:
                res = [0]
                for i in range(n - words_l * word_l):
                    res.append(i+1)
                return res
            else:
                return [0]
        res = []
        i = 0
        while i < (n - words_l * word_l) + 1:
            nextt = s[i:i+word_l]
            if nextt in words:
                temp_arr = list(words)
                temp_arr.remove(nextt)
                full = s[i+word_l:i+word_l*words_l]
                for idx in range(len(temp_arr)):
                    next2 = full[idx*word_l:idx*word_l+word_l]
                    if next2 in temp_arr:
                        temp_arr.remove(next2)
                if not temp_arr:
                    res.append(i)
            i += 1
        return res


print(Solution().findSubstring("aaaaaaaaaaaaa",
                               words=[["aa", "aa"]]))
print(Solution().findSubstring("wordgoodgoodgoodbestword", words=["word", "good", "best", "word"]))
print(Solution().findSubstring("barfoofoobarthefoobarman", words=["bar", "foo", "the"]))
