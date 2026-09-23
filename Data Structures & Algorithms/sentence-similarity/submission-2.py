from collections import defaultdict

class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        d = defaultdict(set)

        if len(sentence1) != len(sentence2):
            return False

        for element in similarPairs:

            d[element[0]].add(element[1])
            d[element[1]].add(element[0])

        for i in range(len(sentence1)):
            if sentence2[i] not in d[sentence1[i]] and sentence2[i] != sentence1[i]:
                return False
        
        return True
        




        