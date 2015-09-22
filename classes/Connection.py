__author__ = 'Marcio Alexandre - marcio.alexandre83@gmail.com, 06/09/2015'


def get_file(arg):
    try:
        return open(arg, "r")
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)

