import os
import re
from tika import parser
from bs4 import BeautifulSoup

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

class OpenPDF(object):


  ROBOT_LIBRARY_SCORE = 'GLOBAL'
  ROBOT_LIBRARY_VERSION = '0.1.0'


  def __init__(self, curpath=None):
    if curpath is None:
      self.curpath = os.path.dirname(os.path.abspath(__file__))


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
    filepath = f'{self.curpath}\\{file}'
    if filepath is None:
      raise Exception("Deve ser informado um argumento válido.")
    if os.path.isdir(filepath):
      raise Exception("Deve ser informado um arquivo válido")
    elif '.pdf' not in filepath:
      raise Exception("Deve ser informado um arquivo no formato .pdf")
    return filepath