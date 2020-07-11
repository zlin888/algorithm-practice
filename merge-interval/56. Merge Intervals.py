from typing import List

class Solution0:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        self.index = 0
        self.intervals = sorted(intervals, key=lambda _:_[0])
        self.result_intervals = []
        if not intervals:
            return []
        if len(intervals) == 1:
            return intervals
        cur_interval = self.next_interval()
        while True:
            next_interval = self.next_interval()
            if not next_interval:
                self.result_intervals.append(cur_interval)
                break
            new_interval = self.try_to_merge(cur_interval, next_interval)
            if new_interval: # mergable
                cur_interval = new_interval
                print(cur_interval)
            else:
                self.result_intervals.append(cur_interval)
                cur_interval = next_interval
        return self.result_intervals
            
    def try_to_merge(self, l0, l1) -> List[List[int]]:
        if l0[1] >= l1[0]:
            return [min(l0[0], l1[0]), max(l1[1], l0[1])]
        else:
            return None 

    def next_interval(self):
        if self.index < len(self.intervals):
            interval = self.intervals[self.index]
            self.index += 1
            return interval
        else:
            return None

class Solution2:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merged = []
        for interval in sorted(intervals, key=lambda _:_[0]):
            if not merged:
                merged.append(interval)
            if merged[-1][1] >= interval[0]:
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
            else:
                merged.append(interval)
        return merged
