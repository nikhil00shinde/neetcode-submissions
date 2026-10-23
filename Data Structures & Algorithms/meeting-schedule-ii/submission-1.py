"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        cnt = 0
        ans = []
        intervals.sort(key=lambda x : x.start)
        for interval in intervals:
            st,ed = interval.start, interval.end
            if not ans:
                heapq.heappush(ans, ed)
            else:
                if ans[0] <= st:
                    heapq.heappop(ans)
                heapq.heappush(ans, ed)
            cnt = max(cnt, len(ans))
        return cnt
