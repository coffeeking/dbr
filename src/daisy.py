###daisy.py
#This file describes both the daisy 2.02 standard, as well as the daisy 3.0 standard, and the various functions needed to process the various types
#This file is part of dbr
#This program is free software you may modify it and distribute it under the terms of the Gnu General Public License, Either version 3 of the license or, at your option, any later version
#import the xml parser
import xml.dom.minidom as md
import os, sys
#define the class for daisy 3 talking books
class daisy3 :
    def getBookTitle(self):
    #Returns the book's title
        book_title = ''
        title = self.tree.getElementsByTagName('title')
        for i in range(len(title)):
            if title[i].hasAttribute('text'):
                if title[i].attributes['text'].value == 'docTitle':
                    book_title = title[i].attributes['text'].value
                break
            return book_title
            print (' the title of the book is book_title')
    def getAuthor(self):
        #returns the author of the book
        bookAuthor=""
        author=self.tree.getElementsByTagName(author)
        for i in range (len(author)):
            if author[i].hasAttribute('text'):  
                if author[i].attributes['text'].value == 'docAuthor':
                    break       
        bookAuthor = author[i].attributes['text'].value
        return bookAuthor
def getMultimediaType(self):
    #gets the type of daisy book we're looking at here, not the format.
    multimediaType=""
    type=self.tree.getElementsByTagname(meta)
    for i in range (len(type)):
        if type[i].hasAttribute('name'):    
            if type[i].attributes['name'].value == 'dtb:multimediaType':
                break
        multimediaType = type[i].attributes['content'].value
        return multimediaType
        file = open("/home/kendell/daisy-books/11-22-63/11_22_63.ncx", "r")
        x = md.parse(file)
        
