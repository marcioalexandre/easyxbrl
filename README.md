# easyxbrl

A cross-platform python library for loading XBRL taxonomy in computer memory. Hence, the developers can manipulate all financial data without to learn about the XBRL technology. As easy as handle a object-oriented python class. 

How to load data:
You can/have to inform the path and the file name in the library. You can load one or many XBRL instances and its taxonomy, there is no a limit about ammount of files, but the performance can vary.

XBRL Objects Structure ====================

About File Object:
        self._name
        self._elements

About Element Object:
        self._name
        self._decimals
        self._id
        self._context_ref
        self._unit_ref
        self._value
        self._company
        self._labels

About Label Object:
        self._type
        self._label
        self._lang
        self._role
        self._id
        self._value

