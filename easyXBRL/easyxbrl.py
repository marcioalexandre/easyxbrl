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

import easyXBRL.classes.Element as el

class easyxbrl(object):

    def get_printElements(self, arg):
        ele = el.Element()
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
        e = el.Element()
        return e.get_allElementsByFiles(listInstanceFile,listLabelFile,option)

    def print_copyright(self):
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
                    "along with Foobar.  If not, see <http://www.gnu.org/licenses/>.\n\n" \
                    "@author: Marcio A. P. da Silva \n" \
                    "@since: September 22nd, 2015\n" \
                    "@Email: marcio.alexandre83@gmail.com\n" \
                    "==========================================================\n\n"
		return copyright;
