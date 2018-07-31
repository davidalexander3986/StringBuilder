""" This class is the class for StringBuilder, which I plan on using when 
solving string related problems in python """

class StringBuilder:

    

    def __init__(self, initString):
        self.str = list(initString)
        self.count = len(initString)

    def __str__(self):
        return str(self.str)

    def append(self, addOn):
        for char in addOn:
            self.str.append(char)
        self.count += len(addOn)

    def get(self, index):
        return self.str[index]

    def set(self, char, index):
        self.str[index] = char

    def size(self):
        return self.count

    def substring(self, start, end):
        toReturn = ""
        
        i = start

        while i <  end:
            toReturn.append(self.str[i])
            i += 1

        return toReturn 





