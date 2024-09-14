import tabula
from datetime import datetime

def parse_all_pages(type = "json"):
  filename = "Thong-tin-so-tien-ung-ho-qua-so-tai-khoan-VietinBank-CT1111-111602391111-tu-ngay-10-den-12.9.2024.pdf"
  dics = tabula.read_pdf(filename, pages=1, pandas_options={'header': None}, lattice=True, multiple_tables=False, output_format="json", area=[351, 51, 788, 544])
  dics = dics + tabula.read_pdf(filename, pages='2-2009', pandas_options={'header': None}, lattice=True, multiple_tables=False, output_format="json")
  res = []
  for idx, dic in enumerate(dics):
    pre_list = dic['data']
    for sub_list in pre_list:
      stt = int(sub_list[0]['text'])
      date = sub_list[1]['text'].replace('\r', ' ')
      amount = int(sub_list[3]['text'].replace('.', ''))
      message = sub_list[2]['text'].replace('\r', ' ')
      sender = sub_list[4]['text']
      if type == "json":
        res.append({
          "date_created": date,
          "amount": amount,
          "message": message,
          "sender": sender,
          "no_in_file": stt,
          "file_id": 2,
          "page": idx+1
        })
      elif type == "tuple":
        res.append((datetime.strptime(date, '%d/%m/%Y %H:%M:%S'), amount, message, sender, stt, 2, idx+1))
  return res