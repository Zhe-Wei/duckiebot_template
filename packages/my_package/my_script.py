
# message = "Hello World!"
# print(message)

import os
message = "Hello from %s!" % os.environ['VEHICLE_NAME']
print(message)
print(message)
print(message)