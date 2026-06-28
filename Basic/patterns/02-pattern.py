class patterns:
    def patternPrint(rows):
        for i in range(1,rows+1):
            for j in range(i):
                print("*",end="")
                
            print()
            
obj = patterns
obj.patternPrint(5)