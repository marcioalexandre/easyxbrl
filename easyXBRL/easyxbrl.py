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
__since__ = 'Sep22nd, 2015'

import time
from easyXBRL.taxonomy.instance import XbrlInstance,XbrlElement
from easyXBRL.taxonomy.linkbase import Label

class easyxbrl(object):

    def getPrintElements(self, instanceList):
        i = 0
        print("Len:"+str(len(instanceList)))
        print str(instanceList)
        if (len(instanceList) > 0):
            for xbrlInstance in instanceList:
                if xbrlInstance._id:
                    print "Instance Id: ["+str(xbrlInstance._id)+"]"
                if xbrlInstance._company:
                    print "Instance company: ["+str(xbrlInstance._company)+"]"
                if xbrlInstance._filename:
                    print "Instance filename: ["+str(xbrlInstance._filename)+"]"
                print "Element number: ["+str(len(xbrlInstance._elementList))+"]"
                if (len(xbrlInstance._elementList)>0):
                    ele = XbrlElement
                    for ele in xbrlInstance._elementList:
                        try:
                            print ""
                            if ele._position:
                                print "Element number: ["+str(ele._position)+"]"
                            if (ele._xml_line):
                                print "Xml Line:       ["+str(ele._xml_line)+"]"
                            if ele._name:
                                print "name:           ["+ele._name+"]"
                            if ele._value:
                                print "value:          ["+ele._value+"]"
                            if ele._unit_ref:
                                print "Unit:           ["+ele._unit_ref+"]"
                            if ele._context_ref:
                                print "Context:        ["+ele._context_ref+"]"
                            if ele._id:
                                print "Id:             ["+ele._id+"]"
                            if ele._decimals:
                                print "Decimals: ["+ele._decimals+"]"
                            print "Label(s) {"
                            try:
                                if (ele._label):
                                    label = Label
                                    for label in ele._label:
                                        if label:
                                            if label._type:
                                                print "  ===== Type :    ["+label._type+"]"
                                            if label._value:
                                                print "  ===== Value:    ["+label._value+"]"
                                            if label._lang:
                                                print "  ===== Lang:     ["+label._lang+"]"
                                            if label._id:
                                                print "  ===== Id:       ["+label._id+"]"
                                            if label._label:
                                                print "  ===== label/id: ["+label._label+"]"
                                            if label._role:
                                                print "  ===== Role:     ["+label._role+"]"
                                            print "  ==============================="
                                else:
                                    print "  ===== [No labels]"
                                    print "  ===== [Warning: check the method: [index.py]{[Line 53: ex.getXbrlInstanceList(,,,,,,'no')]}]"
                                    print "  ===== [if the last parameter is 'yes', this xbrl element has no label]"
                                print "} //label(s)"
                            except ValueError:
                                print("This element has no labels")
                        except Exception as e:
                            print("This element is been represented with a error in XBRL file:"+e.message)
                            print ("If you are sure about the correct XBRL representation (in XBRL file),\n"
                                   "Probably it's been represented in different XBRL standard. \n"
                                   "In this case, please, send me a email: marcio.alexandre83@gmail.com. (Marcio)\n")
        else:
            pass

    def getXbrlInstanceList(self,instanceNameList,
                        labelNameList,
                        calculationNameList,
                        referenceNameList,
                        presentationNameList,
                        definitionNameList,
                        option): # option = "yes", it's gonna return elements with labels; = "no", without labels.
        xbrlInstanceList = []
        i = 0
        for instanceName in instanceNameList:
            xbrlInstance = XbrlInstance.XbrlInstance()
            xi = XbrlInstance
            xi = xbrlInstance.getInstanceByFile(instanceName,
                                                          labelNameList[i],
                                                          calculationNameList,
                                                          referenceNameList,
                                                          presentationNameList,
                                                          definitionNameList,
                                                          i,
                                                          option)
            xbrlInstanceList.append(xi(xi._id,xi._company,xi._filename,xi._elementList))
            i += 1
        return xbrlInstanceList

    def printCopyright(self):
		copyright = "\n\n" \
                    "==========================================================\n" \
                    "Copyright 2015 Marcio Alexandre Pereira da Silva \n\n" \
				    "This file is part of easyXBRL.\n\n" \
                    "easyXBRL is free software: you can redistribute it and/or modify\n" \
                    "it under the terms of the GNU General Public License as published by\n" \
                    "the Free Software Foundation, either version 3 of the License, or\n" \
                    "(at your option) any later version.\n\n" \
                    "easyXBRL is distributed in the hope that it will be useful,\n" \
                    "but WITHOUT ANY WARRANTY; without even the implied warranty of\n" \
                    "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the\n" \
                    "GNU General Public License for more details.\n\n" \
                    "You should have received a copy of the GNU General Public License\n" \
                    "along with easyXBRL.  If not, see <http://www.gnu.org/licenses/>.\n\n" \
                    "@author: Marcio A. P. da Silva \n" \
                    "@since: September 22nd, 2015\n" \
                    "@Email: marcio.alexandre83@gmail.com\n" \
                    "==========================================================\n\n"
		return copyright;
