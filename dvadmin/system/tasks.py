from hashlib import md5
from io import BytesIO
from datetime import datetime
from time import sleep

from openpyxl import Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.utils import get_column_letter
from django.core.files.base import ContentFile
