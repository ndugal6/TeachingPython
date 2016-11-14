#Syntax errors and Evaluation errors
while True:
    try:
        number = int(input("what's your fave number hoss?\n"))
        print(18/number)
        break
    except ValueError:
        print("Please make sure you enter a number")
    except ZeroDivisionError:
        print("Don't pick zero")
    except: #Don't ever use this, just for show
        break
    finally:    #Executes regardless of issue or not>
        print("loop complete")