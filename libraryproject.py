class Book:
    def __init__(self,name,genre):
        self.name = name
        self.genre = genre
        self.fantasy = []
        self.action = []
        self.romance = []
        self.horror = []
        self.mystery = []
        self.other =[]
    
    def Sorting(self):
        if self.genre in Book == "fantasy":
            self.fantasy.append(self)
        elif self.genre in Book == "action":
            self.action.append(self)
        elif self.genre in Book == "romance":
            self.romance.append(self)
        elif self.genre in Book == "horror":
            self.horror.append(self)
        elif self.genre in Book == "mystery":
            self.mystery.append(self)
        else:
            self.other.append(self)

    def __repr__(self):
        description = "This is your library: Fantasy: {fantasy}, Action: {action}, Romance: {romance}, Horror: {horror}, Mystery: {mystery} and Everything else: {other}. ".format(fantasy=self.fantasy, 
        action=self.action, romance=self.romance, horror=self.horror, mystery=self.mystery, other=self.other)




Aarons_Library_creator = input("Welcome to Aarons Library Creator, Please name your Library")
Users_Libary = print(str(Aarons_Library_creator) + " WOW what an awesome name!")