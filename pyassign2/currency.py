#!/usr/bin/env python3

"""currency.py: A module that helps the user to convert the amount of money in an original currency to another currency. 

__author__ = "Xuefeng Wang"
__pkuid__  = "1800011707"
__email__  = "wang-xuefeng@pku.edu.cn"
"""

def before_space(x):
    """Returns: Substring of x; up to, but not including, the first space.

    Parameter x: the string to slice
    Precondition: x has at least one space in it"""
    
    return x[:x.find(" ")]

def get_to(jstr):
    """Returns: The TO value in the response to a currency query.
    Parameter jstr: a json string to parse
    Precondition: jstr is the response to a currency query"""
    
    jstr1 = jstr.replace("true","True")
    json = dict(eval(jstr1))
    return json["to"]

def has_error(jstr):
    """Returns: True if the query has an error; False otherwise.
    Parameter jstr: a json string to parse
    Precondition: jstr is the response to a currency query"""
    
    jstr1 = jstr.replace("true","True")
    jstr2 = jstr1.replace("false","False")
    json = dict(eval(jstr2))
    return not json["success"]

def currency_response(currency_from, currency_to, amount_from):
    """Returns: a JSON string that is a response to a currency query.
    
    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string
    
    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string
    
    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a string"""

    from urllib.request import urlopen

    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+currency_from+'&to='+currency_to+'&amt='+amount_from)
    docstr = doc.read()
    doc.close()
    return docstr.decode('ascii')

def iscurrency(currency):
    """Returns: True if currency is a valid (3 letter code for a) currency. 
    It returns False otherwise.

    Parameter currency: the currency code to verify
    Precondition: currency is a string."""
    
    jstr = currency_response(currency, currency, "1.0")
    return not has_error(jstr)

def exchange(currency_from, currency_to, amount_from):
    """Returns: amount of currency received in the given exchange or reporting the error.

    Parameter currency_from: the currency on hand
   
    Parameter currency_to: the currency to convert to
    
    Parameter amount_from: amount of currency to convert"""
    
    jstr = currency_response(currency_from, currency_to, amount_from)
    try:
        float(amount_from)
        if iscurrency(currency_from) and iscurrency(currency_to):
            x = get_to(jstr)
            amount_to_str = before_space(x)
            return float(amount_to_str)
        elif not iscurrency(currency_from) and iscurrency(currency_to):
            return "Source currency code is invalid."
        elif iscurrency(currency_from) and not iscurrency(currency_to):
            return "Exchange currency code is invalid."
        else:
            return "Source currency code and exchange currency code are invalid."
    except ValueError:
        if iscurrency(currency_from) and iscurrency(currency_to):
            return "Currency amount is invalid."
        elif not iscurrency(currency_from) and iscurrency(currency_to):
            return "Source currency code and currency amount are invalid."
        elif iscurrency(currency_from) and not iscurrency(currency_to):
            return "Exchange currency code and currency amount are invalid."
        else:
            return "Source currency code, exchange currency code and currency amount are invalid."
        
def test_currency_response():
    """test function currency_response(currency_from, currency_to, amount_from)"""
    assert(currency_response("USD", "EUR", "2.5")==
           '{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }')
    assert(currency_response("CNY", "JPY", "1")==
           '{ "from" : "1 Chinese Yuan", "to" : "16.257643642095 Japanese Yen", "success" : true, "error" : "" }')
    assert(currency_response("AAA","USD","3.1")==
           '{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }')
    assert(currency_response("EUR","XYZ","2.8")==
           '{ "from" : "", "to" : "", "success" : false, "error" : "Exchange currency code is invalid." }')
    assert(currency_response("EUR","CNY","a")==
           '{ "from" : "", "to" : "", "success" : false, "error" : "Currency amount is invalid." }')

def test_has_error():
    """test function has_error(jstr)"""
    assert(True == has_error('{ "from" : "", "to" : "", "success" : false, "error" : "Source currency code is invalid." }'))
    assert(False == has_error( '{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }'))

def test_iscurrency():
    """test function iscurrency(currency)"""
    assert(True == iscurrency("USD"))
    assert(False == iscurrency("AAA"))
        
def test_get_to():
    """test function get_to(jstr)"""
    assert("2.1589225 Euros" == 
           get_to('{ "from" : "2.5 United States Dollars", "to" : "2.1589225 Euros", "success" : true, "error" : "" }'))
    assert("16.257643642095 Japanese Yen" == 
           get_to( '{ "from" : "1 Chinese Yuan", "to" : "16.257643642095 Japanese Yen", "success" : true, "error" : "" }'))
    
def test_before_space():
    """test function before_space(x)"""
    assert("28.0" == before_space("28.0 Euros"))
    assert("107.289" == before_space("107.289 Chinese Yuan"))
    assert("291.4" == before_space("291.4 United States Dollars"))

def test_exchange():
    """test function exchange(currency_from, currency_to, amount_from)"""
    assert(2.1589225 == exchange("USD", "EUR", "2.5"))
    assert(16.257643642095 == exchange("CNY", "JPY", "1"))
    assert("Source currency code is invalid." == exchange("AAA", "USD", "1.2"))
    assert("Exchange currency code is invalid." == exchange("EUR","XYZ","3.4"))
    assert("Source currency code and exchange currency code are invalid." == exchange("eur","usd","2.88"))
    assert("Currency amount is invalid." == exchange("USD","EUR","a"))
    assert("Source currency code and currency amount are invalid." == exchange("aaa","EUR","a"))
    assert("Exchange currency code and currency amount are invalid." == exchange("USD","aaa","a"))
    assert("Source currency code, exchange currency code and currency amount are invalid." == exchange("aaa","bbb","a"))

def test_all():
    """test all cases"""
    test_currency_response()
    test_has_error()
    test_iscurrency()
    test_get_to()
    test_before_space()
    test_exchange()
    print("All tests passed.")

def main():
    """main module"""
    test_all()
    currency_from = input("Please enter the currency on hand:")
    currency_to = input("Please enter the currency to convert to:")
    amount_from = input("Please enter the amount of currency to convert:")
    amount_to = exchange(currency_from, currency_to, amount_from)
    if type(amount_to) == float:
        print("The amount of currency received in the given exchange is "+str(amount_to)+".")
        return amount_to
    else:
        print(amount_to)

if __name__ == '__main__':
    main()
