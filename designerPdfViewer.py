from string import ascii_lowercase

def designerPdfViewer(h, word):
    alphabets = list(string.ascii_lowercase)
    height_dict = {alpha:height for alpha, height in zip(alphabets, h)}
    result = []
    for w in word:
        result.append(height_dict[w])
        max_h = max(result)
    return max_h * len(word)