from PyPDF2 import PdfReader
import re
from datetime import datetime
import tabula

reader = PdfReader("thong_tin_ung_ho_qua_tsk_vcb_0011001932418_tu_01_09_den10_09_2024.pdf")
datePattern = r'^\d{2}/\d{2}/\d{4}$'

def isDate(string):
  if(re.match(datePattern, string)):
    return True
  else:
    return False
    
def parse_page(page, type = "json"):
  text = reader.pages[page-1].extract_text()
  res = []
  content = text.split('\n', 7)[7].rsplit('\n', 6)[0]
  arr = content.split('\n')
  i = 0
  while i < len(arr):
    if(isDate(arr[i])):
      date = arr[i]
      nextLine = arr[i+1].split(' ', 2)
      docNo = nextLine[0]
      amount = int(nextLine[1].replace('.', ''))
      message = nextLine[2]
      j = i + 2
      while j < len(arr) and not isDate(arr[j]):
        message += arr[j]
        j += 1
      i = j
      if type == "json":
        res.append({
          "date_created": date,
          "amount": amount,
          "message": message,
          "doc_no": docNo,
          "file_id": 1,
          "page": page
        })
      elif type == "tuple":
        res.append((datetime.strptime(date, '%d/%m/%Y'), amount, message, docNo, 1, page))
  return res

def parse_first_page(type = "json"):
  text = reader.pages[0].extract_text()
  content = text.split('\n', 18)[18].rsplit('\n', 6)[0]
  res = []
  arr = content.split('\n')
  i = 0
  while i < len(arr):
    if(isDate(arr[i])):
      date = arr[i]
      nextLine = arr[i+1].split(' ', 1)
      docNo = nextLine[0][:10]
      amount = int(nextLine[0][10:].replace('.', ''))
      message = nextLine[1]
      j = i + 2
      while j < len(arr) and not isDate(arr[j]):
        message += arr[j]
        j += 1
      i = j
      if type == "json":
        res.append({
          "date_created": date,
          "amount": amount,
          "message": message,
          "doc_no": docNo,
          "file_id": 1,
          "page": 1
        })
      elif type == "tuple":
        res.append((datetime.strptime(date, '%d/%m/%Y'), amount, message, docNo, 1, 1))
  return res

def parse_last_page(type = "json"):
  res = []
  date = ["10/09/2024", "10/09/2024", "10/09/2024", "10/09/2024", "10/09/2024"]
  amount = [500000, 300000, 100000, 200000, 46667]
  message = ["MBVCB.6998628625.Cuu tro thiet hai bao Yagi.CT tu 0071001104341 PHAN NGUYEN DUC NGUYEN toi 0011001932418 MAT TRAN TO QUOC VN - BAN CUU TRO TW", "884114.100924.223854.DANG DAO THANH NHAN chuyen FT24255276428461", "243304.100924.223855.Ung ho dong bao bi bao lu", "884140.100924.223855.Nga Pham chuyen tien", "FT24255999347270 807439.100924.223851.cua it long nhieu ung ho mien bac"]
  docNo = ["5242.74128", "5215.2452", "5017.1390", "5214.2470", "5209.2469"]
  for i in range (0, 5):
    if type == "json":
      res.append({
        "date_created": date[i],
        "amount": amount[i],
        "message": message[i],
        "doc_no": docNo[i],
        "file_id": 1,
        "page": 12028
      })
    elif type == "tuple":
      res.append((datetime.strptime(date[i], '%d/%m/%Y'), amount[i], message[i], docNo[i], 1, 12028))
  return res