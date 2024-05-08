#write functions here, don't add input('') statements here!
def test_config():
    return True
def get_lowest(nums):
    low = min(nums)
    return low

def get_highest(nums):
    high = max(nums)
    return high

def get_sum(nums):
    total = sum(nums)
    return total

def get_average(nums):
    total= sum(nums)
    size = len(nums)
    avg = total/size
    return avg