import os
import re
from tika import parser

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

class Keywords():

  ROBOT_LIBRARY_SCORE = 'GLOBAL'


  @keyword(name='Get PDF Text')
  def get_pdf_text(self, filename):
    filepath = self.__valid_file(filename)
    raw = parser.from_file(filepath)
    return raw['content']


  @keyword(name='Get PDF Text XHTML')
  def get_pdf_text_XHTML(self, filename):
    filepath = self.__valid_file(filename)
    raw = parser.from_file(filepath, xmlContent=True)
    return raw['content']


  @keyword(name='Get PDF Metadata')
  def get_pdf_metadata(self, filename):
    filepath = self.__valid_file(filename)
    raw = parser.from_file(filepath)
    return raw['metadata']


  def __valid_file(self, file):
    if file is None:
      raise Exception("A valid argument must be entered")
    if os.path.isdir(file):
      raise Exception("A valid file must be entered")
    elif '.pdf' not in file:
      raise Exception("A file in .pdf format must be informed")
    return file