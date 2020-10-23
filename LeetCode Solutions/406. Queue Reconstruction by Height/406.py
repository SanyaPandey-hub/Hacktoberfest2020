class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        max_heap, res = [], []
        
        for h,k in people: heapq.heappush(max_heap, (-h, k) )
        
        while max_heap:
            h, k = heapq.heappop(max_heap)
            res.insert(k,[-h,k])
            
        return res
