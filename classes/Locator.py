__author__ = 'Marcio Alexandre - marcio.alexandre83@gmail.com, 07/09/2015'

import xml.etree.ElementTree as ET
import re


class Locator(object):
    def __init__(self, _href = None, _label=None):
        self._type  =   "locator"
        self._href  =   _href
        self._label =   _label

    def __del__(self):
        pass

    def get_locatorByElementFromFile_Discontinued(self, arg_file,ele):
        # ::::::: Warning: This method was discontinued
        # Very low performance, that's why you should not use this function
        # ::::::::::::::::::::::::::::::::::::::::::::
        root = ET.parse(arg_file).getroot()
        ns = {'link':'http://www.xbrl.org/2003/linkbase'}
        print "Elemento (locator.py): "+ele._name
        for locator in root.findall('link:labelLink/link:loc',ns): #run
            match = re.search(r'_'+ele._name, locator.attrib['{http://www.w3.org/1999/xlink}href'])
            if match:
                newloc = Locator()
                newloc._href    = locator.attrib['{http://www.w3.org/1999/xlink}href']
                newloc._label   = locator.attrib['{http://www.w3.org/1999/xlink}label']
                return newloc
                break
            else:
                pass

    def get_listLocatorFromFile(self, file):
        root = ET.parse(file).getroot()
        ns = {'link':'http://www.xbrl.org/2003/linkbase'}
        listLocator = []
        for locator in root.findall('link:labelLink/link:loc',ns): #run
            loc = Locator()
            loc._href    = locator.attrib['{http://www.w3.org/1999/xlink}href']
            loc._label   = locator.attrib['{http://www.w3.org/1999/xlink}label']
            listLocator.append(loc)
        return listLocator

    def get_locatorByElementFromMemory(self,listLocator,ele):
        for loc in listLocator:
            if "_"+ele._name in loc._href:
                return loc
            else:
                pass




'''
#run

file    =   str("../../xbrlfiles/fb/fb-20131231_lab.xml")
ele = Element
ele._name     =   'CapitalLeasesLesseeBalanceSheetAssetsByMajorClassAccumulatedDeprecation'
loc = Locator()
listLocator = []
listLocator = loc.get_listLocatorFromFile(file)
print len(listLocator)
list = loc.get_locatorsByElementFromMemory(listLocator,ele)
for newloc in list:
    print ("Type:"+newloc._type+". Href: "+newloc._href+". Label:"+newloc._label)
'''

