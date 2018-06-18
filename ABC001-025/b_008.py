n = int(input())
s = [input() for _ in range(n)]

import collections
d = collections.Counter(s)
print(d.most_common(1)[0][0])
