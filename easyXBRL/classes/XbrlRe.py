'''
Copyright 2015 Marcio Alexandre Pereira da Silva

This file is part of easyXBRL.

easyXBRL is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

easyXBRL is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Foobar.  If not, see <http://www.gnu.org/licenses/>.

@author: Marcio A. P. da Silva
@since: September 22nd, 2015
@Email: marcio.alexandre83@gmail.com
'''

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


