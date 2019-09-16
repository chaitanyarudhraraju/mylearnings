print 'Hi'
L = [1,2,3]
try:
    import chaitanya
    x = int(raw_input("enter a no: "))
    y = int(raw_input("Enter another no:"))
    z = x/y
    print L[10]
except ValueError:
    print "i got value error"
except IndexError:
    print "i got Index error"
except ZeroDivisionError:
    print "I got zerodivison error"
except Exception as e:
    print "I got some other exception",e
else:
    print "No exception"
finally:
    print "i do always"
print "rest of the app goes here"