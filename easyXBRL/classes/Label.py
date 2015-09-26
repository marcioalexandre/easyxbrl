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

class Label(object):
    def __init__(self,_label= None, _lang=None, _role=None, _id=None, _value=None):
        self._type  = "resource"
        self._label = _label
        self._lang  = _lang
        self._role  = _role
        self._id    = _id
        self._value  = _value

    def __del__(self):
        pass

    def get_labelByLabelFromFile_Deprecated(self,arg_file,arc):
        # :::: Warning:  This method was discontinued
        #  Very low performance, that's why you should not use this function. It's here just for recording.
        # ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
        root = ET.parse(arg_file).getroot()
        ns = {'link':'http://www.xbrl.org/2003/linkbase'}
        if (arc != None):
            listLabel = []
            for label in root.findall('link:labelLink/link:label',ns): #run
                if (label.attrib['{http://www.w3.org/1999/xlink}label'] == arc._to):
                    newlabel = Label()
                    newlabel._label =   label.attrib['{http://www.w3.org/1999/xlink}label']
                    newlabel._lang  =   label.attrib['{http://www.w3.org/XML/1998/namespace}lang']
                    newlabel._role  =   label.attrib['{http://www.w3.org/1999/xlink}role']
                    if (label.attrib['id']):
                        newlabel._id  =   label.attrib['id']
                    newlabel._value = label.text
                    listLabel.append(newlabel)
            return listLabel
        else:
            pass

    def get_listLabelFromFile(self,file):
        root = ET.parse(file).getroot()
        ns = {'link':'http://www.xbrl.org/2003/linkbase'}
        listLabel = []
        for label in root.findall('link:labelLink/link:label',ns):
            newlabel = Label()
            newlabel._label =   label.attrib['{http://www.w3.org/1999/xlink}label']
            newlabel._lang  =   label.attrib['{http://www.w3.org/XML/1998/namespace}lang']
            newlabel._role  =   label.attrib['{http://www.w3.org/1999/xlink}role']
            """
            if ('id' in label.__dict__):
                newlabel._id  =   label.attrib['id']
            """
            newlabel._value = label.text
            listLabel.append(newlabel)
        return listLabel

    def get_labelsByLabelFromMemory(self,listLabel,arc):
        newlistlabel = []
        for label in listLabel:
            if (label._label in arc._to):
                newlistlabel.append(label)
            else:
                pass
        return newlistlabel
