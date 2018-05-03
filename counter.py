class Counter():
    ''' this program counts words in a file'''
    def __init__(self,filename):
        '''self, filename means you have to pass it the name of the file'''
        self.filename = filename
        self.words = []
        self.word_frequency = {}
        self.num_words = 0
        self.contents = ''
        self.pstring = ''
        print(self.filename)
        
    def try_to_open_file_and_read(self):
        ''' see if that file exists'''
        print('ok')
        try:
            with open(self.filename) as f_obj:
                # self.contents = f_obj.read() # could be readlines
                # this one is full of new lines. Strip takes them out.
                #print('sup1')
                # I can't do read and readlines?
                lines = f_obj.readlines()
                for line in lines:
                    self.pstring += line.strip()
                print(self.pstring)
        except FileNotFoundError:
            msg = "Sorry, the file " + self.filename + " does not exist."
            print(msg)
        else:
            # Count the number of words in the file
            # self.words = self.contents.split()
            # self.num_words = len(self.words)
            #print(self.num_words)
            print('ok') 
            print(self.pstring.lower().split().count('a'))
            print(set(self.pstring.lower().split()))
            
    def word_counter(self):
        #for word in set(self.words):  # I have to change this to lower also
            # I need a clean set of words with the punctuation removed bc
            # right now it is like S. or at:
        #    self.word_frequency[word] = self.contents.lower().count(word)
        for word in set(self.pstring.lower().split()):
            self.word_frequency[word] = self.pstring.lower().split().count(word)
        print(sorted(self.word_frequency.items(), key=lambda x: x[1]))
    # sorted(word_frequency.items(), key=lambda x: x[1])


cc = Counter('8547utf-8.txt')
cc.try_to_open_file_and_read()
cc.word_counter()

print('sucks')
# a is a string
# a.lower().split()

#>>> a.lower().split().count('o')
#4