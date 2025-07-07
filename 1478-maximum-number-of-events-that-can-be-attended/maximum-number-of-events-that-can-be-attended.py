class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        m=0
        for event in events:
            m=max(m,event[1])
        events.sort()
        pq=[]
        ans=0
        i=0
        n=len(events)
        for d in range(1,m+1):
            while i<n and events[i][0]<=d:
                heapq.heappush(pq,events[i][1])
                i+=1
            while pq and pq[0]<d:
                heapq.heappop(pq)
            if pq:
                heapq.heappop(pq)
                ans+=1
        return ans

