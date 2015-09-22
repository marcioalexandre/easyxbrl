__author__ = 'Marcio Alexandre - marcio.alexandre83@gmail.com, 18/09/2015'

class XbrlRe(object):
    __elementre         =   str(r'(<(?!xbrl)(?!link)(?!\!\-)\w*.-.\w*.:.(\w|\W)*.>)|(<(?!xbrl)(?!link)(?!\!\-)\w+.:.(\w|\W)*.>)')
    __elementname       =   str(r':\w+')
    __elementdecimals   =   str(r' decimals=(\"|\').\w+(\"|\')')
    __elementid         =   str(r' id=\"(\w+|\W+).(\"|\')')
    __elementcontextRef =   str(r' contextRef=\"(\w+|\W+).(\"|\')')
    __elementunitref    =   str(r' unitRef=\"(\w+|\W+).(\"|\')')
    __elementvalue      =   str(r'>.(\w|\W)*.<')
    #(...)

    def get_elementRe(self):
        return self.__elementre
    def get_elementName(self):
        return self.__elementname
    def get_elementValue(self):
        return self.__elementvalue
    def get_elementId(self):
        return self.__elementid
    def get_elementDecimals(self):
        return self.__elementdecimals
    def get_elementContextRef(self):
        return self.__elementcontextRef
    def get_elementUnitRef(self):
        return self.__elementunitref


