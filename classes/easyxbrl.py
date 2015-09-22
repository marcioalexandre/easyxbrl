__author__ = 'Marcio Alexandre - marcio.alexandre83@gmail.com, 13/09/2015'

''' #if you want to load the pyc file (compiled)
import imp
Element  = imp.load_compiled("Element", "Element.pyc")
 '''
import Element

class easyxbrl(object):

    def get_printElements(self, arg):
        ele = Element.Element()
        i = 0
        if (len(arg) > 0):
            for listele in arg:
                for ele in listele:
                    try:
                        print ""
                        if ele._position:
                            print "Element number: ["+str(ele._position)+"]"
                        if (ele._filename):
                            print "File name:      ["+ele._filename+"]"
                        if (ele._xml_line):
                            print "Xml Line:       ["+str(ele._xml_line)+"]"
                        if ele._company:
                            print "Company:        ["+ele._company+"]"
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
                        try:
                            if (ele._label):
                                print "Label(s) {"
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
                            print "} //label(s)"
                        except ValueError:
                            print("This element has no labels")
                    except Exception:
                        print("This element is been represented with a error in XBRL file.")
                        print ("If you are sure about the correct XBRL representation (in XBRL file),"
                               "Probably it's been represented in different XBRL standard. "
                               "In this case, please, send me a email: marcio.alexandre83@gmail.com. (Marcio)")
        else:
            pass


    def get_allElements(self,listInstanceFile,listLabelFile,option):
        # option = "yes", it's gonna return elements with labels; = "no", without labels.
        e = Element.Element()
        return e.get_allElementsByFiles(listInstanceFile,listLabelFile,option)
