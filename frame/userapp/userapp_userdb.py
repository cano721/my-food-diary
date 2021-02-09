
from frame.userapp.userapp_sql import Sql
from frame.userapp.userapp_db import Db
from frame.userapp.userapp_value import User, PopIngr, Recateg


class UserDb(Db):
    def update(self, u_id, u_nick, u_pwd, u_name, u_age):
        try:
            conn = super().getConnection();
            cursor = conn.cursor();
            cursor.execute(Sql.userupdate % (u_nick,u_pwd,u_name,u_age,u_id));
            conn.commit();
        except:
            conn.rollback();
            raise Exception;
        finally:
            super().close(conn, cursor);

    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.userlist)
        result = cursor.fetchall();
        all = [];
        for u in result:
            user = User(u[0],u[1],u[2],u[3],u[4]);
            all.append(user);
        super().close(conn,cursor);
        return all;

    def nickselect(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.userlist)
        result = cursor.fetchall();
        all = [];
        for n in result:
            all.append(n[1]);
        super().close(conn,cursor);
        return all

class PopIngrDb(Db):
    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.ingrselect);
        result = cursor.fetchall();
        all = [];
        for u in result:
            item = PopIngr(u[0],u[1],u[2])
            all.append(item)
        super().close(conn, cursor);
        return all;

class RecategDb(Db):
    def select(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.recategselect);
        result = cursor.fetchall();
        all = [];
        for i in result:
            recateg = Recateg(i[0],i[1],i[2])
            all.append(recateg);
        super().close(conn, cursor);
        return all;

    def supselect(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.supcselect);
        result = cursor.fetchall();
        all = [];
        for i in result:
            all.append(i[1]);
        super().close(conn, cursor);
        return all;

    def subselect(self):
        conn = super().getConnection();
        cursor = conn.cursor();
        cursor.execute(Sql.subcselect);
        result = cursor.fetchall();
        all = [];
        for i in result:
            all.append(i[0]);
        super().close(conn, cursor);
        return all;

def select_test():
    result = PopIngrDb().select()
    for i in result:
        print(i);

def recateg_test():
    result = RecategDb().select()
    for i in result:
        print(i);

def supselect_test():
    result = RecategDb().supselect()
    for i in result:
        print(i)

def subselect_test():
    result = RecategDb().subselect()
    for i in result:
        print(i);

if __name__ == '__main__':
    select_test();
    recateg_test();
    supselect_test();
    subselect_test();
# def nickselect_test():
#     for n in UserDb().nickselect():
#         print(n);
#
# def select_test():
#     result = UserDb().select();
#     for i in result:
#         print(i);
#
# def update_test():
#     UserDb().update('id04','nck04','pwd04','hong',31)
#
# if __name__ == '__main__':
#     update_test();
#     select_test();

#     nickselect_test();

# from frame.userapp.userapp_sql import Sql
# from frame.userapp.userapp_db import Db
# from frame.userapp.userapp_value import User
#
#
# class UserDb(Db):

#     def selectone(self,id):
#         conn = super().getConnection();
#         cursor = conn.cursor();
#         cursor.execute(Sql.userlistone % id);
#         u = cursor.fetchone();
#         user = User(u[0],u[1],u[2],u[3],u[4]);
#         super().close(conn,cursor);
#         return user;
#
#     def select(self):
#         conn = super().getConnection();
#         cursor = conn.cursor();
#         cursor.execute(Sql.userlist);
#         result = cursor.fetchall();
#         all = [];
#         for u in result:
#             user = User(u[0],u[1],u[2],u[3],u[4]);
#             all.append(user);
#         super().close(conn,cursor);
#         return all;
#
#     def insert(self,u_id,u_nick,u_pwd,u_name,u_age):
#         try:
#             conn = super().getConnection();
#             cursor = conn.cursor();
#             cursor.execute(Sql.userinsert % (u_id,u_nick,u_pwd,u_name,u_age));
#             conn.commit();
#         except:
#             conn.rollback();
#             raise Exception;
#         finally:
#             super().close(conn, cursor);
#
#
# # userlist Test Function ..........
# def userlist_test():
#     users = UserDb().select();
#     for u in users:
#         print(u);
#
# def userlistone_test():
#     users = UserDb().selectone('id01');
#     print(users);
#
# if __name__ == '__main__':
#     userlistone_test();