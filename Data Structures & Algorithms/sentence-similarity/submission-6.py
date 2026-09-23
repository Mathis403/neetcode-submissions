from collections import defaultdict

class Solution:
    def areSentencesSimilar(self, sentence1, sentence2, similarPairs):

        if len(sentence1) != len(sentence2):
            return False

        d = defaultdict(set)

        for a, b in similarPairs:
            d[a].add(b)
            d[b].add(a)

        for a, b in zip(sentence1, sentence2):
            if a != b and b not in d[a]:
                return False

        return True