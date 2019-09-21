'''
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
'''

def encodeString(stri):
    if len(stri) == 0:
        return ''
    c = res = ''
    count = 0
    for s in stri:
        if c != s:
            if count != 0: res = res + (str(count)+c)
            c = s
            count = 1
        else:
            count += 1
    if count != 0: res = res + (str(count)+c)
    return res

print(encodeString("AAAABBBCCDAA"))

def decodeString(s):
    if s == '': return ''
    res = ''
    for i in range(0, len(s), 2):
        item = s[i:i+2]
        res = res + item[1]*int(item[0])
    return res
print(decodeString(encodeString("AAAABBBCCDAA")))
