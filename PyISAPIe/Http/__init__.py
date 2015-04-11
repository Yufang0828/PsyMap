# $URL: http://pyisapie.svn.sourceforge.net/svnroot/pyisapie/Trunk/PyISAPIe/Python/Http/__init__.py $
# $Rev: 181 $ $Date: 2010-04-16 17:38:17 -0700 (Fri, 16 Apr 2010) $
# (C)2008 Phillip Sitbon <phillip@sitbon.net>
#
"""Http interaction module.

Provides interaction with ISAPI built-in module
and access to other tools.

Note: When this package is being loaded for the
first time, the current request context is not
valid because the config and buffering (if used)
are not initialized, so any attempts to access
or manipulate the current request context will
fail.
"""
__all__ = (

  'Config',
  
  # From DLL
  'Read',
  'Write',
  'Env',
  'Header',
  'DisableBuffer'

)

# Imports
#
try:
  from PyISAPIe import Env, Header, Read, Write, DisableBuffer
  Loaded = True

except ImportError:
  # Won't work when extension hasn't been loaded from IIS.
  # Ignoring this error allows access to components and config
  # that don't need the server or a request to be accessed.
  # TODO: Add exception-raising replacements for request-related
  # functions?
  Loaded = False
  pass

# Get the version info. Note that this is NOT imported on star.
# Looks a little excessive but save a lot of low-level work.
#
if Loaded:
  from PyISAPIe import Version as Ver, VersionFull, VersionMajor, VersionMinor, VersionRelease, VersionRevision

  class Version(object):
    Version = Ver
    Full = VersionFull
    Major = VersionMajor
    Minor = VersionMinor
    Release = VersionRelease
    Revision = VersionRevision
    def __str__(This): return This.Version

  Version = Version()
    
  del Ver, VersionFull, VersionMajor, VersionMinor, VersionRelease, VersionRevision


  # Set up the environment hooks, which associates os.environ
  # with the current interpreter.
  # Only doing so when PyISAPIe is loaded, because here we can
  # be sure request processing is imminent.
  #
  def HookEnv():
    import os

    if hasattr(os, "environ_global"):
      raise RuntimeError, "os.environ already hooked"

    os.environ_global = os.environ
    Environ = dict(os.environ)

    def Putenv(Key, Value):
      assert(isinstance(Key, str) and isinstance(Value, str))
      Environ[Key] = Value
      
    def Getenv(Key, Default=None):
      return Environ.get(Key, Default)

    os.environ = Environ
    os.getenv = Getenv
    os.putenv = Putenv
    
  # Set the hook and then get rid of the function
  HookEnv()
  del HookEnv

