from collections import defaultdict


def get_initial(words):
    splits = defaultdict(list)
    vocabs_dict = defaultdict(int)

    for word in words:
        for c in word:
            splits[word].append(c)
            vocabs_dict[c] += 1
    
    vocabs = [{c: f} for c, f in vocabs_dict.items()]

    return vocabs, splits


def get_maxpair(splits):
    pair_stats = defaultdict(int)

    # get pair stats
    for split in splits.values():
        for i in range(len(split) - 1):
            pair = (split[i], split[i+1])
            pair_stats[pair] += 1
    
    # get max_pair & max_freq
    max_pair = tuple()
    max_freq = 0
    for pair, freq in pair_stats.items():
        if max_freq < freq:
            max_freq = freq
            max_pair = pair

    return max_pair, max_freq


def merge_pair(splits, max_pair):
    a, b = max_pair
    
    for word, split in splits.items():
        new_split = []
        if len(split) <= 1: continue
        i = 0
        while i < len(split):
            if i+1 < len(split) and split[i] == a and split[i+1] == b:
                new_split.append(a + b)
                i += 2
            else:
                new_split.append(split[i])
                i += 1
        # update the splits object
        splits[word] = new_split


def tokenizer(text, max_size):
    words = text.split()
    # iniitialize the vocabs and split the words
    vocabs, splits = get_initial(words)

    while len(vocabs) < max_size:
        max_pair, max_freq = get_maxpair(splits)

        # update the splits with the max_pair
        merge_pair(splits, max_pair)

        # update the the vocabs
        merged_pair = max_pair[0] + max_pair[1]
        vocabs.append({merged_pair: max_freq})

    return vocabs


max_size = 8
text = "add sad mad lad dad"
print(tokenizer(text, max_size))
        
            
result = [{'a': 5}, {'d': 7}, {'s': 1}, {'m': 1}, {'l': 1}, {'ad': 5}, {'add': 1}, {'sad': 1}]
print(result)
