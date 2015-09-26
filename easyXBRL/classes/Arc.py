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


import xml.etree.ElementTree as ET

class Arc(object):
    def __init__(self, _concept=None, _role=None, _order=None, _from = None, _to = None):
        self._concept   =   _concept #if labelarc, definitionarc, calculationarc, presentationarc
        #labelarc
        self._type      =   "arc"
        self._role      =   _role
        self._order     =   _order
        self._from      =   _from
        self._to        =   _to
        # +calculationarc
        self.weight     = None
        self.priority   = None
        self.use        = None

    def __del__(self):
        pass

    def get_arcByLocatorFromFile_Discontinued(self,arg_file,locator,concept):
        # concept may be "labelarc", "calculationarc", "definitionarc"
        # :::::::: Warning: This method was discontinued
        # Very low performance, that's why you should not use this function
        # :::::::::::::::::
        root = ET.parse(arg_file).getroot()
        ns = {'link':'http://www.xbrl.org/2003/linkbase'}
        #print arg_locator._label
        if (locator != None):
            for arc in root.findall('link:labelLink/link:'+concept,ns): #run
                if (arc.attrib['{http://www.w3.org/1999/xlink}from'] == locator._label):
                    #from = arc.attrib['{http://www.w3.org/1999/xlink}from']
                    newarc = Arc()
                    newarc._concept = concept
                    newarc._order   = arc.attrib['order']
                    newarc._role    = arc.attrib['{http://www.w3.org/1999/xlink}arcrole']
                    newarc._from    = arc.attrib['{http://www.w3.org/1999/xlink}from']
                    newarc._to      = arc.attrib['{http://www.w3.org/1999/xlink}to']
                    return newarc
                    break
        else:
            pass

    def get_listArcFromFile(self,file,concept):
        # concept may be "labelarc", "calculationarc", "definitionarc"
        root = ET.parse(file).getroot()
        ns = {'link':'http://www.xbrl.org/2003/linkbase'}
        listArc = []
        for arc in root.findall('link:labelLink/link:'+concept,ns):
            newarc = Arc()
            newarc._concept = concept
            if hasattr(arc.attrib,'order'):
                newarc._order   = arc.attrib['order']
            if arc.attrib['{http://www.w3.org/1999/xlink}arcrole']:
                newarc._role    = arc.attrib['{http://www.w3.org/1999/xlink}arcrole']
            else:
                newarc._role    = arc.attrib['{http://www.w3.org/1999/xlink}role']
            newarc._from    = arc.attrib['{http://www.w3.org/1999/xlink}from']
            newarc._to      = arc.attrib['{http://www.w3.org/1999/xlink}to']
            listArc.append(newarc)
        return listArc

    def get_arcByLocatorFromMemory(self,listArc,loc):
        for arc in listArc:
            if arc._from in loc._label:
                return arc
            else:
                pass


