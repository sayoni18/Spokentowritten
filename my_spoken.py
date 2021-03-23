#!/usr/bin/env python
# coding: utf-8

# In[12]:


def rules():
    rules={"special":{"dollar":"$","dollars":"$","percentage":"%"},
    "my_numbers":{"zero": 0,"one" : 1,"two": 2, "three": 3,"four": 4,"five": 5,"six": 6,"seven": 7,"eight": 8,"nine": 9,"ten": 10,
           "twenty": 20,"thirty": 30,"forty": 40,"fifty": 50,"sixty": 60,"seventy": 70,"eighty": 80,"ninety": 90,"hundred": 100
            },
    "doubles": {"single":1,"double":2,"triple":3,"quadruple":4,"quintuple":5, "sextuple":6,"septuple":7,"octuple":8,"nonuple":9,
            "decuple":10},
    "rest": {"C M": "CM","P M": "PM","D M": "DM","A M": "AM"},
    "large_num":{"thousand":1000,"lakhs":100000,"million":1000000,"crores":10000000}}
    return rules

    


# In[13]:


def get_word(word):
    front=""
    last=""
    if(len(word)>1):
        if word[-1]==',' or word[-1]=='.':
            last=word[-1]
            word=word[:-1]
        if word[0]==',' or word[0]=='.':
            front=word[0]
            word=word[1:]
    return front,word,last


# In[23]:




#class for conversion
class SpokenToWritten:

    def __init__(self):

        self.rules=rules()
        self.paragraph=""
        self.ouptut=""

    #getting user input
    def get_user_input(self):

        self.paragraph=input("\n[IN]:Enter Your paragraph of spoken english:\n\t")

        if not self.paragraph:
            raise ValueError("[Error]: You entered nothing.")

    #getting  user output
    def show_output(self):
        print("\n[OUT]:The input Spoken English Paragraph: \n\n \" "+ self.paragraph+"\"")
        print("\nConverted Written English Paragraph: \n\n \"" +self.ouptut+"\"")

    def Convert(self):
        words_of_para=self.paragraph.split()

        special=self.rules['special']
        my_numbers=self.rules['my_numbers']
        doubles=self.rules['doubles']
        rest=self.rules['rest']
        large_num=self.rules['large_num']
        i=0
        no_of_words=len(words_of_para)
        while i<no_of_words: 
            
            front,word,last=get_word(words_of_para[i])
            if i+1!= no_of_words:
                front_n,next_word,last_n=get_word(words_of_para[i+1])
                if word.lower() in my_numbers.keys() and (next_word.lower() in special.keys() ):
                    self.ouptut=self.ouptut+" "+front+special[next_word]+str(my_numbers[word.lower()])+last
                    i=i+2

                elif word.lower() in doubles.keys() and len(next_word)==1:
                    self.ouptut=self.ouptut+" "+front_n+(next_word*doubles[word.lower()])+last_n
                    i=i+2
                elif (word+" "+next_word) in rest.keys():
                    self.ouptut=self.ouptut+" "+front+word+next_word+last_n
                    i=i+2
                elif word.lower() in my_numbers.keys() and (next_word.lower() in large_num.keys() ):
                    self.ouptut=self.ouptut+" "+front+str(my_numbers[word.lower()])+str(large_num[next_word])+last
                    i=i+2
                else:
                    self.ouptut=self.ouptut+" "+words_of_para[i]
                    i=i+1
            else:
                self.ouptut=self.ouptut+" "+words_of_para[i]
                i=i+1


#main function 
def my_conversion():
    #creating class object
    obj_spoken=SpokenToWritten()
    obj_spoken.get_user_input()
    obj_spoken.Convert()


    obj_spoken.show_output()


# In[24]:


my_conversion()


# In[ ]:




