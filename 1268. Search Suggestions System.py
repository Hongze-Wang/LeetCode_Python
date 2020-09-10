# 1268. Search Suggestions System

# brute force
# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         res = []
#         products.sort()
#         for i in range(len(searchWord)):
#             temp = []
#             for j in range(len(products)):
#                 if searchWord[:i+1] == products[j][:i+1] and len(temp) < 3:
#                     temp.append(products[j])
#             res.append(temp)
#         return res

import heapq

class TrieNode:
    def __init__(self):
        self.children = {}
        self.values = []

class Solution:
    def build_trie_tree(self, products):
        root = TrieNode()
        for prod in products:
            node = root
            for c in prod:
                if c not in node.children:
                    node.children[c] = TrieNode();
                node.children[c].values.append(prod)
                node = node.children[c]
        return root

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = self.build_trie_tree(products)
        node = root
        res = []

        for c in searchWord:
            if c in node.children:
                words = node.children[c].values
                heapq.heapify(words)
                size = min(len(words), 3)
                res.append([heapq.heappop(words) for _ in range(size)])
                node = node.children[c]
            else:
                node = TrieNode()
                res.append([])
        return res
