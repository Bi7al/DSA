# Takes an input value
# Generates a Hash code for that value
# Places the item in the array based on the hash code
# Chaining -> The way collisions are solved (collision occur when there is already a value at the index)
# Open addressing -> if the bucket is already taken then the value is placed at the next index
my_hash_set = [["none"],["none"],["none"],["none"],["none"],["none"],["none"],["none"],["none"],["none"],["none"]];






def getHashCode(value):
    return sum(ord(char) for char in value) % 10;


def addValue(value):
    index = getHashCode(value);
    bucket = my_hash_set[index];
    if value not in bucket:
        bucket.append(value);
        
        
def checkValue(value):
    index = getHashCode(value);
    bucket=my_hash_set[index];
    return value in bucket;





addValue("Bilal");
addValue("Jamal");
addValue("Burhan");


print(checkValue("Bilal"))