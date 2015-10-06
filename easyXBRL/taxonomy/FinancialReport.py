__author__ = 'Marcio Alexandre - marcio.alexandre83@gmail.com, 06/10/2015'
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
__since__ = 'Oct06nd, 2015'

class FinancialReport(object):
    def __init__(self, reportType = None, xbrlInstance = None, xbrlLinkbaseList = None):
        self.reportType = reportType
        self.xbrlInstance = xbrlInstance
        self.xbrlLinkbaseList = xbrlLinkbaseList

    def getFinancialReport(self):
        return self;