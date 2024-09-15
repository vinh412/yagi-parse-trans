from connectdb import connectdb
import parse_vietcom
import parse_viettin

mydb = connectdb()
mycursor = mydb.cursor()
sql1 = "insert into transactions1 (date_created, amount, message, doc_no, file_id, page) values (%s, %s, %s, %s, %s, %s)"
sql2 = "insert into transactions1 (date_created, amount, message, sender, no_in_file, file_id, page) values (%s, %s, %s, %s, %s, %s, %s)"

def insert_vietcom_to_db():
  cnt = 0
  num_batch = 0
  # insert first page
  transList = parse_vietcom.parse_first_page(type="tuple")
  cnt += len(transList)
  num_batch += len(transList)
  mycursor.executemany(sql1, transList)

  #i insert page 2-12027
  for i in range(2, 12028):
    transList = parse_vietcom.parse_page(i, type="tuple")
    mycursor.executemany(sql1, transList)
    cnt += len(transList)
    num_batch += len(transList)
    if num_batch > 1000:
      mydb.commit()
      print(f"Inserted {cnt} transactions")
      num_batch = 0
  mydb.commit()
  print(f"Inserted {cnt} transactions")
  # insert last page
  transList = parse_vietcom.parse_last_page(type="tuple")
  cnt+=len(transList)
  mycursor.executemany(sql1, transList)
  mydb.commit()
  print(f"Inserted {cnt} transactions")


def insert_viettin_to_db():
  cnt = 0
  transList = parse_viettin.parse_all_pages(type="tuple")
  for trans in transList:
    mycursor.execute(sql2, trans)
    cnt += 1
    if cnt % 1000 == 0:
      mydb.commit()
      print(f"Inserted {cnt} transactions")
  mydb.commit()
  print(f"Inserted {cnt} transactions")

insert_vietcom_to_db()
insert_viettin_to_db()
