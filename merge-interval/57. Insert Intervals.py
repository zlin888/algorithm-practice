from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            intervals.append(newInterval)
        elif newInterval[0] < intervals[0][0]:
            intervals.insert(0, newInterval)
        else:
            for i in range(len(intervals)):
                if i+1 >= len(intervals) or intervals[i][0] <= newInterval[0] <= intervals[i+1][0]:
                    intervals.insert(i+1, newInterval)
                    break
                    
        merged = []
        for interval in intervals:
            if not merged:
                merged.append(interval)
            if merged[-1][1] >= interval[0]:
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
            else:
                merged.append(interval)
        return merged