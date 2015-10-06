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

#Just a how-to.


import time

from easyXBRL import EasyXbrl

''' These financial files (form Facebook) is available on SEC website
you must create a list is which has to contain the name of XBRL instances,
you'd like to handle so '''
instances = []
instances.append("../xbrlfiles/fb/fb-20130331.xml")
#instances.append("../xbrlfiles/fb/fb-20130630.xml")
#instances.append("../xbrlfiles/fb/fb-20130930.xml")
#instances.append("../xbrlfiles/fb/fb-20131231.xml")

''' you must create a list in which has to contain the name of XBRL label files you'd
like to handle so you also must inform every label file is linked to xbrl instance
(instances = []), in the same sequence'''

labels = []
labels.append("../xbrlfiles/fb/fb-20130331_lab.xml")
#labels.append("../xbrlfiles/fb/fb-20130630_lab.xml")
#labels.append("../xbrlfiles/fb/fb-20130930_lab.xml")
#labels.append("../xbrlfiles/fb/fb-20131231_lab.xml")
start = time.time()
xbrlInstanceList = []
ex = EasyXbrl.easyxbrl()
try:
    xbrlInstanceList = ex.getXbrlInstanceList(instances,
                                          labels,
                                          None,
                                          None,
                                          None,
                                          None,
                                          "yes") #[yes] with linkbases, [no] without linkbases

except Exception as e:
    print "[easyxbrl][sample][Index.py] error({0})".format(e.message)
end = time.time()
# for trying, easyXBRL has a printing method, which you can use:
ex.getPrintElements(xbrlInstanceList)
print "Performance time (seconds): "+str(end-start)
print ex.printCopyright()








