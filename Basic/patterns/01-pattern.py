# pattern 1
class patterns:
    def patternPrint(rows, cloumns):
        for i in range(rows):
            for j in range(cloumns):
                print("*", end="")
                
            print()
obj = patterns
obj.patternPrint(5,5)
