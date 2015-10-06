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
__author__ = 'Marcio Alexandre - marcio.alexandre83@gmail.com'
__since__ = 'October 06th, 2015'

import re
from easyXBRL.conn import Connection
from easyXBRL.taxonomy.linkbase import Arc, Label, Locator
from easyXBRL.xbrlglobal import XbrlTaxonomyRe
from easyXBRL.taxonomy.instance import XbrlElement

class XbrlInstance(object):
    def __init__(self, id=None, company=None, filename=None, elementList=[]):
        self._id = id
        self._company = company
        self._filename = filename
        self._elementList = elementList

    def __del__(self):
        pass

    def getInstanceByFile(self,
                          instanceName,
                          labelName,
                          calculationName,
                          referenceName,
                          presentationName,
                          DefinitionName,
                          position,
                          option): #option is for bringing the labels ("yes") or not("no").
        loc     = Locator.Locator()
        arc     = Arc.Arc()
        label   = Label.Label()
        xinstance = XbrlInstance
        xinstance._id = position
        xinstance._filename = instanceName
        flag = ""
        if (option == "yes"):
            locatorList = loc.get_listLocatorFromFile(labelName)
            arcList     = arc.get_listArcFromFile(labelName,"labelArc")
            labelList   = label.get_listLabelFromFile(labelName)
        else:
            pass
        file = Connection.get_file(instanceName)
        line = file.readline()
        xbrlElementList = []
        #looking for Element within XBRL Instance
        i = 1
        while line != "":
            e = XbrlElement.Element
            xre = XbrlTaxonomyRe.XbrlRe()
            match = re.search(xre.get_elementRe(), line)
            if match:
                #setting position
                e._position = i

                #setting xml line
                e._xml_line = match.group()

                #setting name
                name = re.search(xre.get_elementName(), match.group())
                if name:
                    e._name = str.replace(name.group(), ":", "")
                else:
                    e._name = None

                # getting decimal
                decimals = re.search(xre.get_elementDecimals(), match.group())
                if decimals:
                    decimals = str.replace(decimals.group(), "\"", "")
                    decimals = str.replace(decimals, "\'", "")
                    e._decimals = str.replace(decimals, "decimals=", "")
                else:
                    e._decimals = None

                # getting id
                id = str.replace(match.group(), "-",
                     "z9z9z9z9z9a9a9a9a9az9z9z9z9z9a9a9a9a9a")  # it replaces the hyphen by this improbable sequence
                id = re.search(xre.get_elementId(), id)
                if id:
                    id = str.replace(id.group(), "z9z9z9z9z9a9a9a9a9az9z9z9z9z9a9a9a9a9a",
                          "-")  # it replaces the improbable sequence by hyphen
                    id = str.replace(id, "\"", "")
                    id = str.replace(id, "\'", "")
                    e._id = str.replace(id, "id=", "").strip()
                else:
                    e._id = None

                # getting contextRef
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

                # getting unitRef
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

                # getting element value
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
                    #getting company
                    if (e._name == "EntityRegistrantName"):
                        flag = e._value
                else:
                    e._value = None

                #setting label(s)
                newLabelList = []
                if (option == "yes"): #do you wanna get Labels within Element object or not? yes/no
                    newLabelList = label.get_labelsByLabelFromMemory(labelList,arc.get_arcByLocatorFromMemory(arcList,loc.get_locatorByElementFromMemory(locatorList,e)))
                else:
                    pass
                print ""
                #for label in newLabelList:
                #    print label._value

                xbrlElementList.append(e(e._position, e._xml_line, e._name, e._decimals,e._id,e._context_ref,e._unit_ref,e._value,newLabelList))
                i += 1
            else: #match:
                pass
            line = file.readline()
        # while each XML line
        file.close()
        xinstance._company = flag
        xinstance._elementList = xbrlElementList
        return xinstance

