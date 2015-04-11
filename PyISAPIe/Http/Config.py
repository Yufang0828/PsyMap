# $URL: http://pyisapie.svn.sourceforge.net/svnroot/pyisapie/Trunk/PyISAPIe/Python/Http/Config.py $
# $Rev: 194 $ $Date: 2010-04-16 18:46:46 -0700 (Fri, 16 Apr 2010) $
# (C)2008 Phillip Sitbon <phillip@sitbon.net>
#
"""Configuration parameters for PyISAPIe.

These parameters can be overridden if they are
changed during the import of the ISAPI handler;
however, they are not request-specific.

Python-specific configuration parameters are at
the end of the file.
"""

# Debug
#
# Used to differentiate between a development and
# production environment. This setting is only used
# the manipulate the optimize flag at the end of
# this file. It does not allow reloading on a per-
# request basis; for that, set the maximum number
# of handled requests in your IIS application pool
# settings to 1.
#
Debug = False

# BufferSize
#
# The amount of data to buffer before sending. The
# buffering policy is strict, meaning that the exact
# size will be sent on each write - this provides
# predictable behavior.
#
# If the buffer is not exceeded when the handler
# exits, a content-length header is sent followed
# by the buffer contents. Otherwise, there are a
# few possibilities:
#
#   Client sends close header or not KeepAlive:
#     - No content length header
#     - Buffers and sends normally
#     - Connection closed
#
#   Keepalive:
#     - No content length header
#     - HTTP/1.1:
#         - Use chunked transfer encoding
#         - Chunk size == BufferSize,
#           or write size if None
#     - HTTP/1.0:
#         - Implies KeepAlive == False
#
# Note: The buffer is allocated on the stack
# for speed - keep an eye on your stack usage
# if you go over 64K, the recommended minimum.
#
# Default: None (output on each write)
# Range:   64-131072
#
BufferSize = 131072

# KeepAlive
#
# Use to disable chunked transfer
# encoding for HTTP/1.1 and always
# close the connection.
#
# Default: True
#
KeepAlive = True

# DefaultHeaders
#
# Headers to send (when none have been set) on
# the first write.
#
# Note that output is not considered sent when
# it goes into the buffer.
# Also, don't try to include any \r's, \n's or
# multi-line strings in general - it will only
# confuse the client. To specify a close header,
# use Header(Close=True) for correct behavior.
#
# The most efficient way to specify content
# length is to use Header(Length=NNNN).
#
# Default: Empty
#
DefaultHeaders = ( \
  "Content-Type: text/html",
)

# StaticHeaders
#
# Headers that are always sent. Good to add your
# application-specific headers you'll always need.
# I recommend leaving the X-Powered-By header, it
# is used in some places.
#
# Default: Empty
#
from PyISAPIe import VersionFull
StaticHeaders = ( \
  "X-Powered-By: PyISAPIe-" + VersionFull,
)

# InterpreterMap
#
# Determines how separate interpreters are used.
# An interpreter consists of a totally isolated
# environment, although not GIL-independent.
# Each interpreter is identified by a name.
#
# Default: None
# Values:
#   None     - Always use the same interpreter
#   "XXX"    - Given by Env.XXX (i.e. SERVER_NAME)
#   Function - A function returning either None,
#              which maps the main interpreter, or
#              a string containing the interpreter's
#              name.
#
# For the function, PyISAPIe.Env is valid, unlike
# during module loading before Request() is called.
# Reading from & writing to the client are not
# allowed here.
#   
#
InterpreterMap = None
#
# NOTE: There are C extensions that are not compatible
# with this option. If PyISAPIe hangs, that's why.
#
# You can (kind of) find out if an extension is compatible
# by opening it (the binary) in notepad and searching for
# this string:
#   "PyGILState_Ensure"
# If you see this string, chances are you'll run into
# trouble. It's not always true, but a good indicator.
#


## Begin Python-specific settings
##
import sys, ctypes

# sys.dont_write_bytecode
#
# Since we're loading bytecode into memory once per process
# anyway and presumably not reloading, saving bytecode to
# disk isn't really necessary. Also, the service may not
# have the proper permissions to do so anyway (NB: it usually
# does).
#
# This is set to True by default in the DLL.
#
#
sys.dont_write_bytecode = True

# Py_OptimizeFlag
#
# This corresponds to the -O command line setting, but is no
# longer set internally thanks to ctypes. It will only take
# effect on modules imported after it is changed.
#
# 0 = disable
# 1 = -O
# 2 = -OO
#
#
if not Debug:
  ctypes.c_int.in_dll(ctypes.pythonapi, "Py_OptimizeFlag").value = 1
