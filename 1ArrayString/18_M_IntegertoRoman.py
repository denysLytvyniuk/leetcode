class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        arr = {'1': 'I',
               '4': 'IV',
               '5': 'V',
               '9': 'IX',
               '10': 'X',
               '40': 'XL',
               '50': 'L',
               '90': 'XC',
               '100': 'C',
               '400': 'CD',
               '500': 'D',
               '900': 'CM',
               '1000': 'M',
        }
        num_str = str(num)
        result = ''
        for idx, n in enumerate(num_str):
            if n != '0':

                if n + '0' * (len(num_str) - 1 - idx) in arr:
                    result += arr[n + '0' * (len(num_str) - 1 - idx)]
                else:
                    if n == '2' or n == '3':
                        result += arr['1' + '0' * (len(num_str) - 1 - idx)] * int(n)
                    else:
                        result += arr['5' + '0' * (len(num_str) - 1 - idx)]
                        result += arr['1' + '0' * (len(num_str) - 1 - idx)] * (int(n) - 5)

        return result


print(Solution().intToRoman(101))
