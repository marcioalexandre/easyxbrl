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
along with easyXBRL.  If not, see <http://www.gnu.org/licenses/>.
'''
__author__ = 'Marcio Alexandre P. da Silva - marcio.alexandre83@gmail.com'
__since__ = 'Sep15nd, 2015'

class Element(object):

    def __init__(self, position=None, xml_line=None, name=None, decimals=None,id=None,context_ref=None,unit_ref=None,value=None,label=[]):
        #public for access in other modules
        self._position     = position
        self._xml_line      = xml_line
        self._name         = name
        self._decimals     = decimals
        self._id           = id
        self._context_ref  = context_ref
        self._unit_ref     = unit_ref
        self._value        = value
        self._label        = label

    def __del__(self):
        pass

    ''' Following method is just for recording and future analysis (it can be helpful)
    def get_allElements_Deprecated(self,instancelist): #return listElement
        # this method was discontinued, you can find this action in get_allElementsByFiles(self,listInstanceFile,listLabelFile,"no")
        # and still here just for record
        flag = ""
        listElementByFile = []
        xre = XbrlTaxonomyRe.XbrlRe()
        for file in instancelist:
            file = Connection.get_file(str(file))
            line = file.readline()
            listElement = []
            #try:
            # begin of file ========================================================================================
            while line != "":
                e = Element
                e._filename = file
                match = re.search(
                    xre.get_elementRe(),
                    line)  # com digito no namespace
                if match:
                    # name ----------------------------------------------------------------
                    name = re.search(xre.get_elementName(), match.group())
                    if name:
                        e._name = str.replace(name.group(), ":", "")
                    else:
                        e._name = None

                    # decimals ----------------------------------------------------------------
                    decimals = re.search(xre.get_elementDecimals(), match.group())
                    if decimals:
                        decimals = str.replace(decimals.group(), "\"", "")
                        decimals = str.replace(decimals, "\'", "")
                        e._decimals = str.replace(decimals, "decimals=", "")
                    else:
                        e._decimals = None

                    # id ----------------------------------------------------------------
                    id = str.replace(match.group(), "-",
                                     "z9z9z9z9z9a9a9a9a9az9z9z9z9z9a9a9a9a9a")  # it replaces the hyphen by this improbable sequence
                    id = re.search(xre.get_elementId(), id)
                    if id:
                        id = str.replace(id.group(), "z9z9z9z9z9a9a9a9a9az9z9z9z9z9a9a9a9a9a",
                                         "-")  # it replaces the improbable sequence by hyphen
                        id = str.replace(id, "\"", "")
                        id = str.replace(id, "\'", "")
                        e._id = str.replace(id, "id=", "")
                    else:
                        e._id = None

                    # contextRef ----------------------------------------------------------------
                    cr = str.replace(match.group(), "-",
                                     "z9z9z9z9z9a9a9a9a9az9z9z9z9z9a9a9a9a9a")  # it replaces the hyphen by this improbable sequence
                    cr = re.search(xre.get_elementContextRef(), cr)
                    if cr:
                        cr = str.replace(cr.group(), "z9z9z9z9z9a9a9a9a9az9z9z9z9z9a9a9a9a9a",
                                         "-")  # it replaces the improbable sequence by hyphen
                        cr = str.replace(cr, "\"", "")
                        cr = str.replace(cr, "\'", "")
                        e._context_ref = str.replace(cr, "contextRef=", "").strip()
                    else:
                        e._context_ref = None

                    # unitRef ----------------------------------------------------------------
                    ur = str.replace(match.group(), "-",
                                     "z9z9z9z9z9a9a9a9a9az9z9z9z9z9a9a9a9a9a")  # it replaces the hyphen by this improbable sequence
                    ur = re.search(xre.get_elementUnitRef(), ur)
                    if ur:
                        ur = str.replace(ur.group(), "z9z9z9z9z9a9a9a9a9az9z9z9z9z9a9a9a9a9a",
                                         "-")  # it replaces the improbable sequence by hyphen
                        ur = str.replace(ur, "\"", "")
                        ur = str.replace(ur, "\'", "").strip()
                        e._unit_ref = str.replace(ur, "unitRef=", "").strip()
                    else:
                        e._unit_ref = None

                    # value ----------------------------------------------------------------
                    value = str.replace(match.group(), ".",
                                        "z9z9z9z9z9a9a9a9a9az9z9z9z9z9a9a9a9a9a")  # it replaces the dot by this improbable sequence
                    value = str.replace(value, ",",
                                        "a9a9a9a9a9z9z9z9z9za9a9a9a9a9z9z9z9z9z")  # it replaces the commakmii777 by this improbable sequence
                    value = re.search(xre.get_elementValue(), value)
                    if value:
                        value = str.replace(value.group(), ">", "")
                        value = str.replace(value, "<", "")
                        value = str.replace(value, "z9z9z9z9z9a9a9a9a9az9z9z9z9z9a9a9a9a9a", ".")
                        e._value = str.replace(value, "a9a9a9a9a9z9z9z9z9za9a9a9a9a9z9z9z9z9z", ",").strip()
                        #verifying the name of entity and get its name value
                        if (e._name == "EntityRegistrantName"):
                            flag = e._value
                        else:
                            pass
                    else:
                        e._value = None

                    e._company = flag
                    e._filename = str(file)
                    label = []
                    listElement.append(e(e._name, e._decimals,e._id,e._context_ref,e._unit_ref,e._value,e._company,label,e._filename))
                else: #didnt match
                    pass
                line = file.readline()
            file.close()
            # end file ========================================================================================
            listElementByFile.append(listElement)
        return listElementByFile #
        '''
