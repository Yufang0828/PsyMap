# $URL: http://pyisapie.svn.sourceforge.net/svnroot/pyisapie/Trunk/PyISAPIe/Python/Http/Isapi.py $
# $Rev: 198 $ $Date: 2010-05-03 11:55:56 -0700 (Mon, 03 May 2010) $
# (C)2008 Phillip Sitbon <phillip@sitbon.net>
#
"""Global ISAPI request handler.

All requests go here - after the first successful
import of this module & Request() function, it
will not be reloaded for the life of the interpreter.

This default simply attempts to load the file targeted
by the URL and call its Request() function. Although
SCRIPT_TRANSLATED is not available in IIS 5.x, it is
emulated for completeness.

I don't really recommend this method - it's not as
package/module oriented as the Regex and Advanced
examples, which can handle arbitrary URLs and pass
them to preloaded handlers.

ALSO: imp.load_source is NOT case-sensitive and doesn't
follow the typical import case rules. You might like this
but it's really not great behavior. It does, however,
match IIS's case-insensitivity.

See example Isapi.py files in ../Examples, including
one that makes this version backwards compatible with
v1.0.0 (in the Compat folder).
"""
from PyISAPIe import Env
import imp, hashlib

Handlers = {}

def Initialize(File):
  try:
    ## This would be a good place to do any filename
    ## filtering if necessary.
    #
    #if not File.endswith(".py"):
    #  raise ImportError, File

    # Mapping a file name to its hash just normalizes the
    # text used for the module's __name__, since Python will
    # complain about dots without packages present, among
    # a few other things. You might choose to do more
    # reasoning about the module name, but be careful about
    # collisions if you use just the file base name-- if
    # you have /a/x.py and /b/x.py both will map to module
    # name 'x' in sys.modules and only the one loaded first
    # will produce the proper output.
    Name = hashlib.md5(File).hexdigest()

    Req = imp.load_source(Name, File).Request
  except:
    ## trigger a passthrough to the next ISAPI handler -
    ## ONLY WORKS FOR WILDCARD APPLICATION MAPPINGS
    return lambda: True
    ## or just fail, preferable for an application map
    # raise
  
  Handlers[File] = Req
  return Req

def Request():
  Script = Env.SCRIPT_TRANSLATED.lower()
  return Handlers.get(Script, Initialize(Script))()

