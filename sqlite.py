import sqlite3



conn = sqlite3.connect('information.db')
c = conn.cursor()
#c.execute('create table sensor(dataq)')
c.execute("insert into sensor(dataq) values (38)")
c.execute("insert into sensor(dataq) values (39)")
c.execute("insert into sensor(dataq) values (21)")
c.execute('select * from sensor')
print(c.fetchall())
conn.commit()
conn.close()
