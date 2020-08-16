'''
This problem was asked by Microsoft.

Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
'''
# Look up every substring in the dict: O(N*logk)... does not work
# We might be initially tempted to take a greedy approach to this problem, by for example, iterating over the string and checking if our current string matches so far. However, you should immediately find that that can't work: consider the dictionary {'the', 'theremin'} and the string 'theremin': we would find 'the' first, and then we wouldn't be able to match 'remin'.
# This gives us a clue that we might want to use backtracking to help us solve this problem. We also have the following idea for a recurrence: If we split up the string into a prefix and suffix, then we can return the prefix extended with a list of the rest of the sentence, but only if they're both valid. So what we can do is the following:

#    -  Iterate over the string and split it into a prefix and suffix
#    -  If the prefix is valid (appears in the dictionary), then recursively call on the suffix
#    -  If that's valid, then return. Otherwise, continue searching.
#    -  If we've gone over the entire sentence and haven't found anything, then return empty.

# We'll need a helper function to tell us whether the string can actually be broken up into a sentence as well, so let's define find_sentence_helper that also returns whether or not the sentence is valid.

# Recursion runs in O(2^N) time
'''
1 2
12

1 23
12 3
123
1 2 3

1 234
12 34
123 4
1234
1 23 4
1 2 34
12 3 4
1 2 3 4
'''
def split_sentence(dict, s):
    sentence, valid = find_sentence_helper(dict, s)
    return sentence if valid else []

def find_sentence_helper(dict, s):
    if s == '':
        return [], True
    for i in range(len(s)+1):
        prefix = s[:i]
        suffix = s[i:]
        print(prefix+" "+suffix)
        if prefix in dict:
            sentence, valid = find_sentence_helper(dict, suffix)
            if valid: return [prefix] + sentence, True
    return [], False

# DP: We'll keep a dictionary that maps from indices to the last word that can be made up to that index. We'll call these starts. Then, we just need to do two nested for loops, one that iterates over the whole string and tries to find a start at that index, and a loop that checks each start to see if a new word can be made from that start to the current index.

def split_sentence_dp(dict, s):
    starts = {0: ''}
    for i in range(len(s)+1):
        newstarts = starts.copy()
        for start, _ in starts.items():
            if s[start:i] in dict:
                newstarts[i] = s[start:i]
        starts = newstarts.copy()
    res = []
    cur_start = len(s)
    if cur_start not in starts:
        return None
    while cur_start != 0:
        res.append(starts[cur_start])
        cur_start -= len(starts[cur_start])
    return list(reversed(res))

dict = ["the", "theremin"]
s = "theremin"
print(split_sentence_dp(dict, s))

def split_sentence_findAll(dict, s):
    starts = {0: []}
    for i in range(len(s)+1):
        newstarts = starts.copy()
        for start, _ in starts.items():
            if s[start:i] in dict:
                if i in newstarts:
                    newstarts[i].append(s[start:i])
                else:
                    newstarts[i] = [s[start:i]]
        starts = newstarts.copy()
    print(starts)
    if len(s) not in starts: return []
    items = []
    res = []
    def make_sense(book, s, index, items, res):
        if index <= 0:
            res.append(' '.join(reversed(items)))
            return
        for word in book[index]:
            items.append(word)
            make_sense(book, s, index - len(word), items, res)
            items.pop()
    make_sense(starts, s, len(s), items, res)
    return res 

dict = ["apple", "pen", "applepen", "pine", "pineapple"]
s = "pineapplepenapple"
print(split_sentence_findAll(dict, s))
