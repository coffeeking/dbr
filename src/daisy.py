###daisy.py
#This file describes both the daisy 2.02 standard, as well as the daisy 3.0 standard, and the various functions needed to process the various types
#This file is part of dbr
#This program is free software you may modify it and distribute it under the terms of the Gnu General Public License, Either version 3 of the license or, at your option, any later version
#import the xml parser
import xml.dom.minidom as md
#define the class for daisy 3 talking books
class daisy3 :
    def __init__ (self, title, author, multimediaType):
    def getBookTitle(self):
    """
    Returns the book's title
    """
    book_title = ''
    title = self.tree.getElementsByTagName('title')
    for i in range(len(title)):
    if title[i].hasAttribute('name'):
    if title[i].attributes['name'].value == 'docTitle':
    book_title = title[i].attributes['content'].value
    break
    return book_title
def getAuthor(self):
        #returns the author of the book
        bookAuthor=""
        author=self.tree.getElementsByTagName(author)
        for i in range (len(author)):
        if author[i].hasAttribute('name'):
        if author[i].attributes['name'].value == 'docAuthor':
break
return bookAuthor
def getMultimediaType(self):
        #gets the type of daisy book we're looking at here, not the format.
        multimediaType=""
        type=self.tree.getElementsByTagname(type)
        for i in range (len(type)):
        if type[i].hasAttribute('name')
        if type[i].attributes['name'].value == 'dtb:multimediaType':
        return multimediaType

