#write functions here, don't add input('') statements here!

class Stock:
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name
    
    def return_symbol (self):
        return (self.__symbol)
    
    def return_company_name(self):
        return (self.__company_name)

def stock_purchase_history ():
    stock_history = {}
    stock_1 = Stock("AAPL", "Apple Inc")
    stock_history [stock_1.return_symbol()] = stock_1.return_company_name()
    stock_2 = Stock("CAT", "Caterpillar")
    stock_history [stock_2.return_symbol()] = stock_2.return_company_name()
    stock_3 = Stock("EK", "Eastman Kodak")
    stock_history [stock_3.return_symbol()] = stock_3.return_company_name()
    stock_4 = Stock("GOOG", "Google")
    stock_history [stock_4.return_symbol()] = stock_4.return_company_name()
    stock_5 = Stock("MSFT", "Microsoft")
    stock_history [stock_5.return_symbol()] = stock_5.return_company_name()
    for key, value in stock_history.items():
        print (key, "\t", value, "\n")
