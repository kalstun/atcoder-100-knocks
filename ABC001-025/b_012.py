n = int(input())

import datetime
d = datetime.timedelta(seconds=n)
print(str(d).zfill(8))
