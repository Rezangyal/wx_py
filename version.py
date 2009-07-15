"""Provides an object representing the current 'version' or 'release'
of Py as a whole.  Individual classes, such as the shell, filling and
interpreter, each have a revision property based on the CVS Revision."""

__author__ = "Patrick K. O'Brien <pobrien@orbtech.com>"
__cvsid__ = "$Id: version.py 36607 2005-12-30 23:02:03Z RD $"
__revision__ = "$Revision: 36607 $"[11:-2]

VERSION = '0.9.7'
