import sqlite3

my_conn = sqlite3.connect('data.db')

cur = my_conn.cursor()
  
columns = []

def get_columns():
  cur.execute("PRAGMA table_info(shoes);")
  for row in cur:
    columns.append(row[1])

get_columns()
print(columns)

def print_columns():
  #say the columns in the table are 
  print("The columns in the table are:" + " ".join(col for col in columns))

print_columns()

def owner_lookup(name):
  line = cur.execute('select * from shoes where owner is ?',(name,)).fetchone()
  if line == None:
    print("no records found")
  else:
    print(str(line))



owner_lookup("Bob")


def add_owner():
  print_columns()
  owner = input("give me a new data entry in this format: owner,brand,size,price \n").split(",")
  print(len(owner))
  if len(owner) < len(columns):
    print("sorry can't add a partial record")
  else:
    cur.execute("INSERT into shoes(owner,brand,size,price)VALUES(?,?,?,?);",owner)
    my_conn.commit()
   
  print(len(owner))




#print(my_conn)

# res = my_conn.execute("SELECT name FROM sqlite_master WHERE type='table';")

# for name in res:
#   print(name[0])

def main():
  pass
  while True:
    answer = input("What would you like to do?: (1) Look up")

if __name__== '__main__':
  main()