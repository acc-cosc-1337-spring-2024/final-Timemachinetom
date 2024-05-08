#add import
import question_a
nums = []
while len(nums)!= 5:
    num = input ('Enter a number: ')
    num = int(num)
    nums.append(num)
if len(nums) == 5:
    low = question_a.get_lowest(nums)
    print ("Lowest number:", low)
    high = question_a.get_highest(nums)
    print ("Highest number:", high)
    sum = question_a.get_sum(nums)
    print ("Sum of numbers:", sum)
    avg = question_a.get_average(nums)
    print ("Average of numbers:", avg)


