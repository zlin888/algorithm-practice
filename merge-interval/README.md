# Content
* 56 - Merge Intervals (Greedy)
* 57 - Insert Interval (Greedy)
* 435 - Non-overlapping Intervals (Greedy, meeting rooms problem)
* 986 - Interval List Intersections (double pointer, 垃圾题)

# 6 overlaps situations 
![6-overlaps](6-overlaps.png)

# 56. & 57. merge and insert intervals
56.Merge Interval and 57.Insert Interval is similar. For 57, Just need to insert the interval to the correct position of given interval and then use the 56 algorithm will be find. Or use greedy.

* 57 can use greedy algorithm to do it. But need to take full care of 6 overlapping situataions.

* when using for/while-loop, be careful of the situation where len=0/1

# 435. Non-overlapping Interval
1. Greedy: if two interval mergable, pick one whose end point is smaller
2. It is also A classic Meeting Rooms / Class Rooms problem. Greedy, sort intervals by its left point(ending time). And then iterate it.

# 986. Interval List Intersections
太简单了，双指针

# common code

```python
def mergable(l0, l1):
    if l0[0] >= l1[0]:
        l0, l1 = l1, l0
    return l0[1] > l1[0]


def merge(l0, l1):
    if l0[0] >= l1[0]:
        l0, l1 = l1, l0
    return [l0[0], max(l1[1], l0[1])]
```

# Other Links:
1. [zhihu note][zhihu-note]

[zhihu-note]: https://zhuanlan.zhihu.com/p/114704401