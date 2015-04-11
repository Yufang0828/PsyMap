# $URL: http://pyisapie.svn.sourceforge.net/svnroot/pyisapie/Trunk/PyISAPIe/Python/Examples/WSGI/Isapi.py $
# $Rev: 198 $ $Date: 2010-05-03 11:55:56 -0700 (Mon, 03 May 2010) $
# (C)2008 Phillip Sitbon <phillip@sitbon.net>
#
"""Global ISAPI request handler for use with WSGI applications.

This example merges two WSGI applications and also runs scripts
directly.

If you don't have either Django or Trac, comment out that section
and the entry in "Apps" and it should work fine.

You may also believe that you can run multiple Django projects just
by choosing the DJANGO_SETTINGS_MODULE environment variable based
on the URL, but beware- that is a process-level value you're
changing! I'm not sure if the value is also looked for in the WSGI
environment. For now, I'm just leaving it at one project.

I chose to place the root folder under /app for the specific
purpose of making PyISAPIe the wildcard handler for that path only.
For IIS 5.x, all the paths must end in ".py" because an extension
must be associated with a handler.

See the install docs for further information, and the WSGI setup
page for specifics about getting this script going.
"""
from Http.WSGI import RunWSGI
from Http import Env
import imp, hashlib
import os


# Django:
#  site_root: eg: r'D:\WebSites\app'
#  site_settings: eg: r"app.settings"
#os.environ["DJANGO_SETTINGS_MODULE"] = "Web.settings"
def get_django_handler(site_root, site_settings):
    os.sys.path.append(site_root)
	
    import django
    from django.core.handlers.wsgi import WSGIHandler as DjangoHandler
    os.environ["DJANGO_SETTINGS_MODULE"] = site_settings

    django.setup()
    return DjangoHandler()


# Trac
#	site_root: eg: r"C:\Path\To\Trac"
def get_trac_handler(site_root):
    from trac.web.main import dispatch_request as TracHandler
    os.environ["TRAC_ENV_PARENT_DIR"] = site_root # or TRAC_ENV
    return TracHandler


# Simple script handling.
#   Just a copy of what's in the Request() of the default handler.
#   It of course assumes that the file specified by the URL is valid.
#  ScriptHandlers : a dictionary 
def register_script_handler(ScriptHandlers):
  Script = Env.SCRIPT_TRANSLATED.lower()
  return ScriptHandlers.get(Script, Initialize(Script))()


def InitializeScript(File):
  try:
    ## This would be a good place to do any filename filtering if necessary.
    #
    #if not File.endswith(".py"):
    #  raise ImportError, File

    Name = hashlib.md5(File).hexdigest()

    Req = imp.load_source(Name, File).Request
  except:
    ## trigger a passthrough to the next ISAPI handler -
    ## ONLY WORKS FOR WILDCARD APPLICATION MAPPINGS
    return lambda: True
    ## or just fail, preferable for an application map
    # raise

  ScriptHandlers[File] = Req
  return Req


# URL prefixes to map to the roots of each application.
# None of these actually use the path, and you could either optimize it out or find a reason to use it.
#
# Remember that this dictionary is not ordered, so make sure substrings for paths are distinct,
# e.g. don't have /app/1 and /app/1/2 -- the mapped handler that gets used for /app/1 is not known in this case.


Apps = {
  "/"  : lambda P: RunWSGI(get_django_handler(r'D:\WebSites\PsyMap', "Web.settings")),
  #"/app/trac/"    : lambda P: RunWSGI(TracHandler),
  #"/app/scripts/" : lambda P: RunScript(),
}


# The main request handler.
def Request():
  # Note that this is case sensitive
  Name = Env.SCRIPT_NAME

  # Apps might be better off as a tuple-of-tuples,
  # but for the sake of representation I leave it
  # as a dict.
  for App, Handler in Apps.items():
    if Name.startswith(App):
      return Handler(Name)

  # Cause 500 error: there should be a 404 handler, eh?
  raise Exception, "Handler not found."
