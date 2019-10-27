def longestPalindrome(s):
    # dynamic programming
        """
        :type s: str
        :rtype: str
        """
        max_len = -1
        n = len(s)
        max_str = ""
        L = [[0 for i in range(n)] for i in range(n)]
        
        # single character
        for i in range(n):
            L[i][i] = 1
            max_len = 1
            max_str = s[i]
        
        # two characters
        for i in range(n - 1):
            if s[i] == s[i+1]:
                L[i][i+1] = 1
                max_len = 2
                max_str = s[i:i+2]
        # more than 2 characters
        k = 3
        
        while k <= n:
            i = 0
            while i+k-1 < n:
                j = i+k-1
                if s[i] == s[j] and L[i+1][j-1] == 1:
                    L[i][j] = 1
                    if k > max_len:
                        max_len = k
                        max_str = s[i: i+k]
                i+=1
            k +=1

        return max_str