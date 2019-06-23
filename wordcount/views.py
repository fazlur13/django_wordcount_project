from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')


def count (request):
    typed_fulltext=request.GET['fulltext']
    wordlist = typed_fulltext.split()

    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word] += 1

        else:
            #add to the disctionary
            worddictionary[word] = 1

    #sorting by frequesncy of the word used in.
    sortedwords = sorted (worddictionary.items(), key = operator.itemgetter(1), reverse = True )

    return render(request,'count.html',{'typed_fulltext': typed_fulltext,'count':len(wordlist),'sortedwords': sortedwords})

def about(request):
    return render(request, 'about.html')
