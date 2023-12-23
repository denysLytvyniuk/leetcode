import re


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        temp = [words[0]]
        for i in range(1, len(words)):
            if len(temp[-1]) + len(words[i]) + 1 <= maxWidth:
                temp[-1] += ' ' + words[i]
            else:
                if not temp[-1].__contains__(' '):
                    temp[-1] += ' ' * (maxWidth - len(temp[-1]))
                else:
                    pr = maxWidth - len(temp[-1])
                    spaces = len(re.findall(' ', temp[-1]))
                    curr = 1
                    while pr > 0:
                        if pr > spaces:
                            temp[-1] = temp[-1].replace(' '*curr, ' '*(curr+1))
                            curr += 1
                            pr -= spaces
                        else:
                            temp[-1] = temp[-1].replace(' ' * curr, ' ' * (curr + 1), pr)
                            break

                temp.append(words[i])

        temp[-1] += ' ' * (maxWidth - len(temp[-1]))
        return temp


p = Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
print(Solution().fullJustify(["What","must","be","acknowledgment","shall","be"], 16))