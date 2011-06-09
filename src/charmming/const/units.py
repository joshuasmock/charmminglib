"""
A collection of useful unit conversions for chemistry and physics.

:Attributes:
    | ``RAD2DEG``
    | ``DEG2RAD``
    | ``BOLTZMANN`` - In SI units.
    | ``AVOGADRO``
    | ``JOULE2CAL`` - In SI units.
    | ``CAL2JOULE`` - In SI units.
"""


from math import pi


RAD2DEG = 180. / pi
DEG2RAD = pi / 180.
BOLTZMANN   = 1.3806503e-23 # m**2 * kg * s**-2 * K**-1
AVOGADRO    = 6.0221415e23  # Number
JOULE2CAL   = 0.239005736   # Calorie * Joule**-1
CAL2JOULE   = JOULE2CAL**-1
