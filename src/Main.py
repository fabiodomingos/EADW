'''
Created on 2013/04/05

@author: goncalocarito, fabiodomingos

Main Function to invoke all the functions

When a search is performed, the result should include the sentimental on each person
in each returned news item

- other analysis could also been invoked here and creat another functions/py modules

'''

#interface
while(1):
    print "INTERFACE\n"
    option = raw_input("Select an option:")
    print "1 Search in news\n"
    if option == 1:
        queries = raw_input("SEARCH (insert your queries):")
        break
    else:
        print "Invalid Input: Insert the option Number"