def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    i = j = ans = 0
    hashset = set()
    n = len(s)
    while i < n and j < n:
        if s[j] not in hashset:

            hashset.add(s[j])
            j += 1
            ans = max(ans, j-i)

        else:
            hashset.remove(s[i])
            i += 1
    return ans