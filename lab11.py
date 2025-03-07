# integrity pledge: The work I have done is my own - DK
# program name: lab11.py
# lab section: X05L

import pickle

# purpose: main calls the class
# parameters: none
# return: none
def main():
    t = Translation()
    t.addEntry("dog", "atim")
    t.addEntry("mouse", "wâpakosîs")
    t.addEntry("beer", "iskwêsisâpoy")
    t.addEntry("medicine", "maskihkiy")
    t.addEntry("river", "sîpiy")
    t.addEntry("garden", "kiscikânis")
    t.addEntry("ball", "pâkâhtowân")
    t.addEntry("peanut butter", "anikwacâsi-mîciwin")
    t.addEntry("cow", "mostos")
    t.addEntry("hill", "waciy")
    t.saveData()
    t2 = Translation("cr-en")
    t2.addEntry("atim", "dog")
    t2.addEntry("wâpakosîs", "mouse")
    t2.addEntry("iskwêsisâpoy", "beer")
    t2.addEntry("maskihkiy", "medicine")
    t2.addEntry("sîpiy", "river")
    t2.addEntry("kiscikânis", "garden")
    t2.addEntry("pâkâhtowân", "ball")
    t2.addEntry("anikwacâsi-mîciwin", "peanut butter")
    t2.addEntry("mostos", "cow")
    t2.addEntry("waciy", "hill")
    t2.saveData()

# purpose: class Translation translates words
# parameters:  none
# return: none
class Translation:
    def __init__(self, tkey = 'en-cr'):
        self.tkey = tkey
        self.filename = "dictionary-"+tkey+".pkl"
        self.data = self.loadData()

    def __str__(self):
            string = "\n"
            for key in self.data:
                string += "     "+ key + ": " + self.data[key] + "\n"
            return("Length: " + str(len(self.data)) + "\nEntries:" + string)
    
    def __len__(self):
        return(len(self.data))

    def modifyEntry(self, fromWord, toWord):
        self.data[fromWord] = toWord

# purpose: will load data
# parameters: self
# return: data
    def loadData(self):
        try:
            file = open(self.filename, "rb")
            pickle.load(self.filename)
            pickle.save(self.filename)
            file.close()
            return self.filename
        except:
            self.data = {}
            return self.data
        
# purpose: will save the data
# parameters: self
# return: none
    def saveData(self):
            file = open(self.filename, "wb")
            pickle.dump(self.data, file)
            file.close()

# purpose: will add entry to data
# parameters: self, fromWord, toWord
# return: none
    def addEntry(self, fromWord, toWord):
        self.data.update({fromWord: toWord})

# purpose: deletes an existing entry in data
# parameters: self, fromWord
# return: none
    def deleteEntry(self, fromWord):
        if fromWord in self.data:
            del self.data[fromWord]

# purpose: translates a word
# parameters: self, fromWord
# return: toWord
    def translate(self, fromWord):
        if fromWord in self.data:
            toWord = self.data[fromWord]
            return toWord
           
if __name__ == "__main__":
    main()

        


