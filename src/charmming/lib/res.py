"""
DOCME
"""
# fcp
# 10/26/2010


from numpy import array
from charmming.lib.basestruct import BaseStruct
from charmming.tools import Property


class Res(BaseStruct):
    """
    Properties
        `addr`
        `chainid`
        `heavyCom`
        `resid`
        `resIndex`
        `resName`
        `segid`
        `segType`
    """
    def __init__(self, iterable=None, **kwargs):
        super(Res, self).__init__(iterable, **kwargs)

##############
# Properties #
##############

    @Property
    def addr():
        doc =\
        """
        The `addr` property provides a human readable unique string
        representation for each `Res` instance.
        """
        def fget(self):
            return '%s.%4s.%04d' % (self.chainid, self.segType, self.resid)
        return locals()

    @Property
    def chainid():
        doc =\
        """
        DOCME
        """
        def fget(self):
            for atom in self:
                return atom.chainid
        return locals()

    @Property
    def heavyCom():
        doc =\
        """
        The center of mass of residue, computed using only "heavy"
        (non-hydrogen) atoms.

        Care should be taken with this method, as it filters with
        `BaseAtom.element` which won't necesarily be defined for all
        atoms.
        """
        def fget(self):
            result = array([ atom.mass * atom.cart for atom in self
                        if atom.element == 'h' ])
            result = result.sum(axis=0)
            mass = sum( ( atom.mass for atom in self if atom.element == 'h' ) )
            return result / mass
        return locals()

    @Property
    def resid():
        doc =\
        """
        DOCME
        """
        def fget(self):
            for atom in self:
                return atom.resid
        def fset(self, value):
            for atom in self:
                atom.resid = value
        return locals()

    @Property
    def resIndex():
        doc =\
        """
        DOCME
        """
        def fget(self):
            for atom in self:
                return atom.resIndex
        def fset(self, value):
            for atom in self:
                atom.resIndex = value
        return locals()

    @Property
    def resName():
        doc =\
        """
        DOCME
        """
        def fget(self):
            for atom in self:
                return atom.resName
        def fset(self, value):
            for atom in self:
                atom.resName = value
        return locals()

    @Property
    def segid():
        doc =\
        """
        DOCME
        """
        def fget(self):
            for atom in self:
                return atom.segid
        return locals()

    @Property
    def segType():
        doc =\
        """
        DOCME
        """
        def fget(self):
            for atom in self:
                return atom.segType
        return locals()
