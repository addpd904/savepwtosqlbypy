from pymysql import Connection
# generate a connection object

class SqlInter():
    def __init__(self):
        self.con_sql = Connection(
            host='localhost',
            port=3306,
            user='root',
            password='123456'
        )
        # select the database
        self.con_sql.select_db('sqlpra')
        self.cursor = self.con_sql.cursor()

    # get the cursor object
    def getUser(self):
        self.cursor.execute('select * from savepw')
        # return a tuple,like ((1, 'zs', 'zs123456'), (2, 'ls', 'ls23456'))
        res:tuple=self.cursor.fetchall()
        return res
    def insertUser(self,id,username,pw):
        try:
            sqlSta=f"insert into savepw values ({id},'{username}','{pw}')"
            self.cursor.execute(sqlSta)
            # commit modify
            self.con_sql.commit()
            return 'insert successfully'
        except Exception:
            return 'failed to insert'
    def delUser(self,id:int,name,pw)->int:
        # return 1:success ; return 0:failed
            sqlSta=f"delete from savepw where id={id} and username='{name}' and password='{pw}'"
            print(sqlSta)
            res=self.cursor.execute(sqlSta)
            # commit modify
            return res

    def checkUserViaName(self,name)->int:
        # return 1:user exist ; return 0:user don't exist
            sqlSta = f"select * from savepw where username='{name}'"
            res=self.cursor.execute(sqlSta)
            return res
    def checkSignedUserViaName(self,name)->int:
        # return 1:user exist ; return 0:user don't exist
            sqlSta = f"select * from user where username='{name}'"
            res=self.cursor.execute(sqlSta)
            return res
    def checkSignPassword(self,name,pw):
        # select * from student where age>18;
        # return not 0:password is right ; return 0:password is wrong
        sqlSta = f"select * from user where username='{name}' and password='{pw}'"
        res = self.cursor.execute(sqlSta)
        return res
    def saveSignedUser(self,id:int,name,pw):
        sqlSta = f"insert into user values ({id},'{name}','{pw}')"
        self.cursor.execute(sqlSta)
        self.con_sql.commit()

    def getSignedupUser(self):
        pass

sqlI=SqlInter()
if __name__ == '__main__':
    sqlI=SqlInter()
    sqlI.getUser()
    sqlI.insertUser(3,'zjl','mima2342')
    sqlI.saveSignedUser(1,'zjl','123')
    # print(sqlI.checkSignPassword('zjl','23'))
    print(sqlI.delUser(1,'ww','123'))
