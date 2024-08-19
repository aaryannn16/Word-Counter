import string
from collections import Counter
#function for word count
def Word_counter(file_path):
    with open(file_path,'r') as file:
        text = file.read()
        text = text.translate(str.maketrans('','',string.punctuation)) #eliminating any punctuations
        words = text.split()
        sentences = text.split('.')
        
        total_words = len(words)
        total_sentences = len([s for s in sentences])
        #Creating a dictionary to store words and sentences in Key Value pairs
        result = {
            'Total Words in the File': total_words,
            'Total sentences in the File':total_sentences
        }
        
        return result

file_path = input("Enter your File Name/Path: ") #Taking file name/path as input
result = Word_counter(file_path)
print("File Summary: ")
for key,value in result.items():
    print(f"{key}: {value}")
    
        
    
    