import random
import string
def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
print ("Random String is ", randomString(5) )
print ("Random String is ", randomString(7) )
print ("Random String is ", randomString(5) )
print ("Random String is ", randomString(7) )
print ("Random String is ", randomString(5) )
print ("Random String is ", randomString(7) )