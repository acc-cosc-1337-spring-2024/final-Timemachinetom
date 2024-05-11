import question_c
from question_c import Stock


stock_1 = Stock("GOOG","Google ")
print ("\033[1mStock Report\033[0m")
print ("Company Symbol")
print (stock_1.get_company_name(), stock_1.get_symbol())