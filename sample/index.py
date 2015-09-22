__author__ = 'Marcio Alexandre - marcio.alexandre83@gmail.com, 10/09/2015'
'''
This is just a how-to.
 A simple and very useful sample for loadind XBRL data in-memory.
'''
from classes import easyxbrl
import time
# These financial files is available on SEC website
# you must create a list is which has to contain the name of XBRL instances, you'd like to handle so
instances = []
instances.append("../xbrlfiles/fb/fb-20130331.xml")
instances.append("../xbrlfiles/fb/fb-20130630.xml")
instances.append("../xbrlfiles/fb/fb-20130930.xml")
instances.append("../xbrlfiles/fb/fb-20131231.xml")
#(...)

# you must create a list in which has to contain the name of XBRL label files you'd like to handle so
# you also must inform every label file is linked to xbrl instance (instances = []), in the same sequence
labels = []
labels.append("../xbrlfiles/fb/fb-20130331_lab.xml")
labels.append("../xbrlfiles/fb/fb-20130630_lab.xml")
labels.append("../xbrlfiles/fb/fb-20130930_lab.xml")
labels.append("../xbrlfiles/fb/fb-20131231_lab.xml")
#(...)

ex = easyxbrl.easyxbrl()
# if you want to know de element labels, you must put "yes" in the last parameter
start = time.time()
listEle = ex.get_allElements(instances,labels,"yes")
end = time.time()
# for trying, easyXBRL has a printing method, which you can use:
ex.get_printElements(listEle)
print "Performance time (milliseconds): "+str(end-start)








