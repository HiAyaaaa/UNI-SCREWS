#method to report all screws
def screwReport(passedList):
    #print labels at appropriate spacings to line up with values
    print("\tMATERIAL TYPE    \tLENGTH\tSTOCK(50) STOCK(100) STOCK(150) COST(50) DISCOUNT")
    #
    length = len(passedList)
    totalStock = 0
    totalCost = 0
    #iterate through the list until completed, taking 8 bits at a time (the details on 1 item)
    for x in range(0, length, 8):
         tempstring = ''
         #add each detail to a string before outputting in 1 line
         tempstring = tempstring + '\t' + passedList[x+0]
         tempstring = tempstring + '\t ' + passedList[x+1]
         tempstring = tempstring + '    \t' + passedList[x+2]
         tempstring = tempstring + '\t' + passedList[x+3]
         tempstring = tempstring + '\t  ' + passedList[x+4]
         tempstring = tempstring + '\t     ' + passedList[x+5]
         tempstring = tempstring + '\t\t' + passedList[x+6]
         tempstring = tempstring + '\t' + passedList[x+7]
         print(tempstring)
         #add the stock and cost of the current string to the running totals
         totalStock = totalStock + float(passedList[x+3]) + (float(passedList[x+4]))*2 + (float(passedList[x+5]))*3
         totalCost = totalCost + totalStock * float(passedList[x+6])
    print("Total stock:", totalStock)
    print("Total Value of stock: £", totalCost)


def screwLengthReport(passedListSCR):
    #print labels at appropriate spacings to line up with values
    print("20cm\t 40cm\t60cm")
    lengthSCR = len(passedListSCR)
    total20 = 0
    total40 = 0
    total60 = 0
    #iterate through the list until completed, adding screws of the respective lengths to their running totals)
    for IterateSCR in range(0, lengthSCR, 8):
         lengthStockSCR = 0
         lengthStockSCR = lengthStockSCR + int(passedListSCR[IterateSCR+3]) + (int(passedListSCR[IterateSCR+4]))*2 + (int(passedListSCR[IterateSCR+5]))*3
         lengthCheckSCR = int(passedListSCR[IterateSCR+2])
         if lengthCheckSCR == 20:
             total20 = total20 + lengthStockSCR
         elif lengthSCR == 40:
             total40 = total40 + lengthStockSCR
         else:
             total60 = total60 + lengthStockSCR
    #print the running totals
    print(total20, '\t', total40, '\t', total60)

def specificLengthReport(passedListl):
    #take input of the required length
    chosenLength = int(input("please input the length of screw you are looking for (in cm)"))
     #print labels at appropriate spacings to line up with values
    print("\tMATERIAL TYPE    \tLENGTH\tSTOCK(50) STOCK(100) STOCK(150) COST(50) DISCOUNT")
    lengthl = len(passedListl)
    totalStockl = 0
    totalCostl = 0
    #iterate through the list until completed, taking 8 bits at a time, ONLY do so if it is of the requested length
    for lengthIterate in range(0, lengthl, 8):
        if(int(passedListl[lengthIterate+2]) == chosenLength):
             tempstringl = ''
             #add each detail to a string before outputting in 1 line
             tempstringl = tempstringl + '\t' + passedListl[lengthIterate+0]
             tempstringl = tempstringl + '\t ' + passedListl[lengthIterate+1]
             tempstringl = tempstringl + '    \t' + passedListl[lengthIterate+2]
             tempstringl = tempstringl + '\t' + passedListl[lengthIterate+3]
             tempstringl = tempstringl + '\t  ' + passedListl[lengthIterate+4]
             tempstringl = tempstringl + '\t     ' + passedListl[lengthIterate+5]
             tempstringl = tempstringl + '\t\t' + passedListl[lengthIterate+6]
             tempstringl = tempstringl + '\t' + passedListl[lengthIterate+7]
             print(tempstringl)
             totalStockl = totalStockl + float(passedListl[lengthIterate+3]) + (float(passedListl[lengthIterate+4]))*2 + (float(passedListl[lengthIterate+5]))*3
             totalCostl = totalCostl + totalStockl * float(passedListl[lengthIterate+6])
    print("Total stock:", totalStockl)
    print("Total Value of stock: £", totalCostl)
    
    
def categoryQuery(passedListCQ):
    #take input for the specifications of the wanted category
    lengthCQ = len(passedListCQ)
    CQlength = int(input("what is the length of the screw you are searching for?"))
    CQmaterial = input("what is the material of the screw you are searching for(no capitals)?")
    CQtype = (input("what is the screw type you are searching for?"))
    
    print("\tMATERIAL TYPE    \tLENGTH\tSTOCK(50) STOCK(100) STOCK(150) COST(50) DISCOUNT")
    #set up variables to help with iteration
    categoryIterate = 0
    categoryCheck = 1
    #iterate throught the items until the end of the list is reached or the item is found
    while(categoryCheck == 1 and categoryIterate < lengthCQ):
   
        if((int(passedListCQ[categoryIterate+2]) == CQlength)and((passedListCQ[categoryIterate]) == CQmaterial)and((passedListCQ[categoryIterate+1]) == CQtype)):
             tempstringCQ = ''
             #add each detail to a string before outputting in 1 line
             tempstringCQ = tempstringCQ + '\t' + passedListCQ[categoryIterate+0]
             tempstringCQ = tempstringCQ + '\t ' + passedListCQ[categoryIterate+1]
             tempstringCQ = tempstringCQ + '    \t' + passedListCQ[categoryIterate+2]
             tempstringCQ = tempstringCQ + '\t' + passedListCQ[categoryIterate+3]
             tempstringCQ = tempstringCQ + '\t  ' + passedListCQ[categoryIterate+4]
             tempstringCQ = tempstringCQ + '\t     ' + passedListCQ[categoryIterate+5]
             tempstringCQ = tempstringCQ + '\t\t' + passedListCQ[categoryIterate+6]
             tempstringCQ = tempstringCQ + '\t' + passedListCQ[categoryIterate+7]
             print(tempstringCQ)
             categoryCheck = 0
             categoryFound = categoryIterate

        categoryIterate = categoryIterate + 8
    #if the item was found proceed
    if(categoryCheck == 0):
        print("1. increase stock level")
        print("2. make a sale of these screws")
        #take input on the users options
        categoryChoice = int(input("please enter the number of the option you want"))
        #option 2 sale
        if(categoryChoice == 2):
            boxChoice = int(input("please choose beetween 1:boxes of 50, 2:100, 3:150"))
            amountChoice = int(input("please input how many boxes you are selling"))
            #50s
            if(boxChoice == 1):
                #check to see if there are enough boxes to supply the order then process as neccessary
               if(int(passedListCQ[categoryFound+3]) < amountChoice):
                   stockChoice = int(input("There is not enough boxes to process this order, Would you like to take as many as possible? 1 for yes 2 for no"))
                   if(stockChoice == 1):
                      print("boxes of 50 depleted")
                      amountChoice = int(passedListCQ[categoryFound+3])
                      passedListCQ[categoryFound+3] = str(0)
                   else:
                       print("aborting sale")
               else:
                   passedListCQ[categoryFound+3] = str(int(passedListCQ[categoryFound+3]) - amountChoice)
                   print("the total amount of these boxes is now", passedListCQ[categoryFound+3])
            #100s
            elif(boxChoice == 2):
               if(int(passedListCQ[categoryFound+4]) < amountChoice):
                   stockChoice = int(input("There is not enough boxes to process this order, Would you like to take as many as possible? 1 for yes 2 for no"))
                   if(stockChoice == 1):
                      print("boxes of 100 depleted")
                      amountChoice = int(passedListCQ[categoryFound+4])
                      passedListCQ[categoryFound+4] = str(0)
                   else:
                       print("aborting sale")
               else:
                   passedListCQ[categoryFound+4] = str(int(passedListCQ[categoryFound+4]) - amountChoice)
                   print("the total amount of these boxes is now", passedListCQ[categoryFound+4])
            #150's       
            else:
               if(int(passedListCQ[categoryFound+5]) < amountChoice):
                   stockChoice = int(input("There is not enough boxes to process this order, Would you like to take as many as possible? 1 for yes 2 for no"))
                   if(stockChoice == 1):
                      print("boxes of 150 depleted")
                      amountChoice = int(passedListCQ[categoryFound+5])
                      passedListCQ[categoryFound+5] = str(0)
                   else:
                       print("aborting sale")
               else:
                   passedListCQ[categoryFound+5] = str(int(passedListCQ[categoryFound+5]) - amountChoice)
                   print("the total amount of these boxes is now", passedListCQ[categoryFound+5])
            #calculate the total price of the sale, if there is a discount on this item apply it
            totalPrice = amountChoice * float(passedListCQ[categoryFound+6])
            if(passedListCQ[categoryFound+7].__contains__("y")):
               print("congrats their is a discount of 10% on this order")
               totalPrice = totalPrice *0.9
            print("the total price is£", totalPrice)              
        else:
            #select the box type and the amount you want to add
            boxChoice = int(input("please choose beetween 1:boxes of 50, 2:100, 3:150"))
            amountChoice = int(input("please input how many boxes you are adding"))
            if(boxChoice == 1):
               passedListCQ[categoryFound+3] = str(int(passedListCQ[categoryFound+3]) + amountChoice)
               print("the total amount of 50 boxes is now:",passedListCQ[categoryFound+3])
            elif(boxChoice == 2):
                passedListCQ[categoryFound+4] = str(int(passedListCQ[categoryFound+4]) + amountChoice)
                print("the total amount of 100 boxes is now:",passedListCQ[categoryFound+4])
            else:
                passedListCQ[categoryFound+5] = str(int(passedListCQ[categoryFound+5]) + amountChoice)
                print("the total amount of 150 boxes is now:",passedListCQ[categoryFound+5])
                
                
     #return the updated list to the main function           
    return(passedListCQ)
            

def discountQuery(passedListD):
    
    #set up variables to track the current discounted item, the item that currently has the highest stock, and the number of stock of said items
    lengthD = len(passedListD)
    tempStock = 0
    highestStock = 0
    newHighest = 0
    currentDiscount = 0
    
    #iterate through the list until completed, taking 8 bits at a time (the details on 1 item)
    for DIterate in range(0, lengthD, 8):
        tempStock = float(passedListD[DIterate+3]) + (float(passedListD[DIterate+4]))*2 + (float(passedListD[DIterate+5]))*3
        tempDCheck = passedListD[DIterate+7]
        tempDCheck.strip()
        #if the item is currently discounted note that down
        if(tempDCheck.__contains__("y")):
        
            currentDiscount = DIterate
        #if the stock of the current item is higher than the current record, replace the record with it
        if(tempStock > highestStock):
             (tempstringD) = ''
             #add each detail to a string before outputting in 1 line
             tempstringD = tempstringD  + '\t' + passedListD[DIterate+0]
             tempstringD  = tempstringD  + '\t ' + passedListD[DIterate+1]
             tempstringD  = tempstringD  + '    \t' + passedListD[DIterate+2]
             tempstringD  = tempstringD  + '\t' + passedListD[DIterate+3]
             tempstringD  = tempstringD  + '\t  ' + passedListD[DIterate+4]
             tempstringD  = tempstringD  + '\t     ' + passedListD[DIterate+5]
             tempstringD  = tempstringD  + '\t\t' + passedListD[DIterate+6]
             tempstringD  = tempstringD  + '\t' + passedListD[DIterate+7]
             highestStock = tempStock
             newHighest = DIterate
             
    #if the old discount hasnt been outranked, do nothing         
    if(int(newHighest) == int(currentDiscount)):
       print("The highest stock item is currently discounted, there is no need for action")
       #else ask the user if they wish to swap the item that is currently discounted
    else:
        print("\tMATERIAL TYPE    \tLENGTH\tSTOCK(50) STOCK(100) STOCK(150) COST(50) DISCOUNT")
        print(tempstringD)
        discountChoice =  int(input("This item with the highest stock is not currently discounted, would you like to change this? 1 for yes 2 for no"))
        if(discountChoice == 1):
            passedListD[newHighest+7] = "yes"
            passedListD[currentDiscount+7] = "no"
            #pass the list back to the main function
    return(passedListD)    
                                                              
                                                            
    
    
#loop variable 
stopLoop = 1
#read data in from the file into a list, splitting elements by a comma
screwFile = open('ScrewData.txt', 'r')
screwLine = screwFile.readline()
screwList = list()
screwCheck = int(0)
while screwLine != '':
    if (screwLine.startswith('#') == False):
            dividedList = screwLine.split(',')
            for i in range(8):
                screwList.append(dividedList[i])
                
                
    screwCheck = screwCheck+1
    
    screwLine = screwFile.readline()
        
 #menu to choose selected options   
screwFile.close()
while(stopLoop == 1):
    print("1:Full Screw Report")
    print("2:Screw Report by length")
    print("3:List of screws of chosen length")
    print("4:query particular screw category")
    print("5:update the discounts")
    print("6:quit")
    menuOption = int(input("please select the number of the option you want"))
    if(menuOption == 1):
        screwReport(screwList)
    elif(menuOption == 2):
        screwLengthReport(screwList)
    elif(menuOption == 3):
        specificLengthReport(screwList)
    elif(menuOption == 4):
        screwList=categoryQuery(screwList)
    elif(menuOption == 5):
        screwList=discountQuery(screwList)
    elif(menuOption == 6):
        stopLoop = 2
        print("GOODBYE!")
    else:
        stopLoop = 1
        
        

