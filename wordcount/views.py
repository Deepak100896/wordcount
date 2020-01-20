from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render (request,'homepage.html')

def count(request):
    text = request.GET['fulltext']
    wordlist = text.split()

    #creating a dictionery to store the words
    worddict = {}
    #looping through the wordlist and storing it into the dictionery
    for i in wordlist:
        if i in worddict:
        #increase the dictionery
            worddict[i] += 1
        else:
        # add to the dictionery
            worddict[i] = 1

    sortedwords = sorted(worddict.items(), key=operator.itemgetter(1), reverse=False)
    return render(request, 'count.html',{'fulltext':text,'count':len(wordlist),'sortedwords':sortedwords})

#    print (len(wordlist))
#    return render (request,'count.html',{'fulltext':text,'wordcount':len(wordlist)})
