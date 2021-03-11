from .Keywords import Keywords
from .version import VERSION

class OpenPDFLibrary(Keywords):
  ROBOT_LIBRARY_SCOPE = 'GLOBAL'
  ROBOT_LIBRARY_VERSION = VERSION

def __init__(self):
  vs = VERSION