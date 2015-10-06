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
__since__ = 'Sep15nd, 2015'

def get_file(arg):
    try:
        return open(arg, "r")
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)

