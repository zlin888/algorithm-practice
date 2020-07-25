## Content
* (295) find-median-from-data-stream
* sliding window median
* maximize capital

## 295. find-median-from-data-stream
### Two Heaps 
the key is to maintain the balance of two heap, which is piece of cake.

### AVL Tree
AVL Tree (e.g. B tree or RBT). In C++, can use `mutilset` that is implemented in RBT to solve this problem.
1. First, think about **how a to get the median from a AVL Tree**. (think ......) YES! We can use a pointer to track it. **But how to move the tracker?** We can use `next` and `prev` keywords to find the value that is slightly bigger or smaller than the current value. By doing so, we are always tracking the median.
2. **Complexity**, `next` and `prev` can be treated as O(1) in amortized time. Thus, total complexity should be O(N)
