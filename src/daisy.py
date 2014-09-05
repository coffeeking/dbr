###daisy.py
#This file describes both the daisy 2.02 standard, as well as the daisy 3.0 standard, and the various functions needed to process the various types
#This file is part of dbr
#This program is free software you may modify it and distribute it under the terms of the Gnu General Public License, Either version 3 of the license or, at your option, any later version
#import the xml parser
import xml.dom.minidom
import os, sys
file = open("/home/kendell/daisy-books/11-22-63/11_22_63.ncx", "r")
x = md.parse(file)
#create the book info dictionary
bookinfo = {"title" "author" "type"}
#define the class for daisy 3 talking books
class daisy3 :
    def getBookTitle(self, file, x):
        #Returns the book's title
        book_title = ''
        title = self.tree.getElementsByTagName(x, 'docTytle')
        for i in range(len(title)):
            if title[i].hasAttribute('text'):
                    print "we've got the book's title"
                    book_title = title[i].attributes['text'].value
            break
        return book_title
    def getAuthor(self, file, x):
        #returns the author of the book
        bookAuthor=""
        author=self.tree.getElementsByTagName(author)
        for i in range (len(author)):
            if author[i].hasAttribute('docAuthor'):  
                bookAuthor = author[i].attributes['text'].value
                print("the author is" + bookAuthor)
                break       
        return bookAuthor
def getMultimediaType(self):
    #gets the type of daisy book we're looking at here, not the format.
    multimediaType=""
    type=self.tree.getElementsByTagname(meta)
    for i in range (len(type)):
        if type[i].hasAttribute('name'):    
            if type[i].attributes['name'].value == 'dtb:multimediaType':
                multimediaType = type[i].attributes['content'].value
break                   
return multimediaType
