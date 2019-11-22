#!/usr/bin/env python3


#445573ea993dd09e9a7d2c57f02ea1e320310c37.png, MLKFW

import hashlib
image_name="MLKFW"
encoded="445573ea993dd09e9a7d2c57f02ea1e320310c37"
"""m = hashlib.sha1()
m.update(image_name.encode('utf-8'))
print(m.hexdigest())"""

save_binary = encoded.encode('utf-8')

decoded = save_binary.decode('utf-8')
print(decoded)