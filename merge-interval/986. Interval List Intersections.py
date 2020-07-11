class Solution:
    def intervalIntersection(self, A, B):
        if not A or not B:
            return []
        i_a = 0
        i_b = 0
        merged = []
        while i_a < len(A) and i_b < len(B):
            a, b = A[i_a], B[i_b]
            if mergable(a, b):
                merged.append(merge(a, b))
            if a[1] < b[1]:
                i_a += 1
            else:
                i_b += 1
            print(i_a, i_b)
        return merged


def mergable(l0, l1):
    if l0[0] >= l1[0]:
        l0, l1 = l1, l0
    return l0[1] >= l1[0]

def merge(l0, l1):
    if l0[0] >= l1[0]:
        l0, l1 = l1, l0
    return [max(l0[0], l1[0]), min(l0[1], l1[1])]