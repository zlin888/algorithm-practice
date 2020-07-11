# 普通的贪心算法，注意考虑6种情况
class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort(key=lambda _:_[0])
        if not intervals:
            return 0
        merging_intervals = None
        output = 0
        for interval in intervals:
            if not merging_intervals:
                merging_intervals = interval
            else:
                if merging_intervals[1] > interval[0]:
                    merging_intervals = merging_intervals if merging_intervals[1] < interval[1] else interval
                    output += 1
                else:
                    merging_intervals = interval 
        return output

# 贪心算法：找出尽量多不重合的interval （经典的办公室会议问题，排课问题），按照结束时间排序
class Solution:
    def eraseOverlapIntervals(self, intervals):
        if not intervals:
            return 0
        intervals.sort(key=lambda _:_[1])
        prev = None
        count = 1
        for interval in intervals:
            if not prev:
                prev = interval
            else:
                if not prev[1] > interval[0]:
                    count += 1
                    prev = interval
        return len(intervals) - count