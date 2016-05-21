'''
Created on May 5, 2016

@author: Saurabh P Sabnis
'''

def reverseWordsString(sentence):
    ll = sentence.split()
    print type(ll)
    ll.reverse()
    print type(ll)
    result = ""
    for i in ll:
        result = result + i + " "
    return result
        
if __name__ == '__main__':
    print reverseWordsString("This is for my git repo")