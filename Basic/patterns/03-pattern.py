class patterns:
    def patternPrint(rows):
        for i in range(1,rows+1):
            for j in range(1,i):
                print(j,end="")
                
            print()
            
obj = patterns
obj.patternPrint(5)