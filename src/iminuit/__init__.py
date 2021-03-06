"""MINUIT2 from Python.

Basic usage example::

    from iminuit import Minuit
    def f(x, y, z):
        return (x - 2) ** 2 + (y - 3) ** 2 + (z - 4) ** 2
    m = Minuit(f)
    m.migrad()
    print(m.values)  # {'x': 2,'y': 3,'z': 4}
    print(m.errors)  # {'x': 1,'y': 1,'z': 1}

Further information:

* Code: https://github.com/scikit-hep/iminuit
* Docs: https://iminuit.readthedocs.io
"""

__all__ = ["Minuit", "minimize", "describe", "__version__"]

from ._minuit import Minuit
from ._minimize import minimize
from .util import describe
from .version import __version__
