def workbook(n, k, arr):
    """
    return the number of special problems in Lisa's workbook.
    n: total chapters
    k: max problems per page
    arr[i]: total problems in chapter i+1
    """
    current_page = 1
    special_prob = 0
    for i, probs_in_chapter in enumerate(arr):
        num_full_pages, leftover_probs = divmod(probs_in_chapter, k)
            #print(num_full_pages, leftover_probs)
        total_pages = num_full_pages + (1 if leftover_probs else 0)
        problems_in_chapter = iter(range(1, probs_in_chapter+1))
        
        for _ in range(total_pages):
            probs_on_page = [next(problems_in_chapter, None) for _ in range(k)]
            if current_page in probs_on_page:
                special_prob+=1
            current_page+=1
    return special_prob