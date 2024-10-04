class TextEditir():
    def __init__(self, TextF):
        self.TextF = TextF
        self.text=''
        self.count=1
    
    def read(self):
        with open( self.TextF + ".txt" , "r", encoding="utf-8") as file:
            self.text = file.read()
            
            print(self.text)


    def Copy(self):
        with open (self.TextF + str(self.count)+".txt","w", encoding="utf-8") as file:
            file.write(self.text)
            self.count+=1

    def Add(self):
        with open (self.TextF +".txt","a", encoding="utf-8") as file:
            file.write(self.text)

        

NameFile=input("Name File")
first=TextEditir(NameFile)
first.read()
first.Copy()
first.Add()

