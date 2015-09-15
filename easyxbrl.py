__author__ = 'Marcio Alexandre - marcio.alexandre83@gmail.com, 13/09/2015'

import imp
Element = imp.load_compiled("Element", "Element.pyc")

class easyxbrl(object):

    def get_printElements(self, arg):
        ele = Element.Element()
        i = 0
        if (len(arg) > 0):
            for listele in arg:
                for ele in listele:
                    print "=================================================================="
                    print "=================================================================="
                    print "||||||||||||| Element |||||||||||||"
                    if (ele._filename):
                        print "File name: "+ele._filename
                    if ele._company:
                        print "Company: "+ele._company
                    if ele._name:
                        print "name: "+ele._name
                    if ele._value:
                        print "value: "+ele._value
                    if ele._unit_ref:
                        print "Unit: "+ele._unit_ref
                    if ele._context_ref:
                        print "Context: "+ele._context_ref
                    if ele._id:
                        print "Id: "+ele._id
                    if ele._decimals:
                        print "Decimals: "+ele._decimals
                    if (ele._label):
                        print "Label(s):"
                        for label in ele._label:
                            if label:
                                if label._value:
                                    print "======= Value: "+label._value
                                if label._lang:
                                    print "======= Lang: "+label._lang
                                if label._id:
                                    print "======= Id: "+label._id
                                if label._label:
                                    print "======= Id(/Label): "+label._label
                                print "======================================================================"
                    else:
                        print "::::: There is no labels"
        else:
            pass

    def get_allElements(self,listInstanceFile,listLabelFile,option):
        # option = "yes", it's gonna return elements with labels; = "no", without labels.
        e = Element.Element()
        return e.get_allElementsByFiles(listInstanceFile,listLabelFile,option)
