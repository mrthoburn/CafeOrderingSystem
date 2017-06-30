from sqlalchemy import create_engine
engine = create_engine('mysql://root:root@172.22.193.69:3306/ups_eats')
connection = engine.connect()
result = connection.execute("select * from customer;")
for row in result:
    print("username:", row['username'])
connection.close()
