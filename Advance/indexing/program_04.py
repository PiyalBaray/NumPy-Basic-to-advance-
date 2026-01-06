# Boolean indexing

import numpy as np

a=np.random.randint(1,100,24).reshape(6,4)
print("My numpy array is :\n")
# all data show for >5
print("which data is >5:\n",a>5)
# all data show for < 5
print("which data is >5:\n",a<5)
# That data equal to 5
print("which data is =5\n",a==5)
# All data /2
print("This data divided by 2 :\n",a%2==0)
