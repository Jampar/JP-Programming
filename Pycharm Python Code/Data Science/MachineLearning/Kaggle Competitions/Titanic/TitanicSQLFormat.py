import sqlite3
from sqlite3 import Error
import pandas as pd
import  csv

def main():

    database = "trainingdata.db"

    conn = create_connection(database)

    with conn:
        #converts the csv to sqlite database.
        fill_from_csv(conn,"train.csv")

        #fetchs all the values of the age column.
        ages = fetch_column_values(conn,'Age')

        #formats the age data list.
        validAgeList = list(sum(ages, ()))

    AgesDelIds = []

    #Finds all the nulls in the ages column.
    for i in range(0,validAgeList.__len__()):
        if validAgeList[i] is None:
            AgesDelIds.append(i + 1)

    #Removes all nulls from ages.
    for x in range(0,AgesDelIds.__len__()):
        delete_row(conn,'tData',str(AgesDelIds[x]))

    #Embarked Null Removed
    delete_row(conn,'tData','47')


    conn.commit()
    conn.close()

def table_columns(conn, table_name):
    curs = conn.cursor()
    sql = "select * from %s where 1=0;" % table_name
    curs.execute(sql)
    return [d[0] for d in curs.description]

def create_connection(db_file):

    try:
        con = sqlite3.connect(db_file)
        return con

    except Error as e:

        print(e)

    return None

def delete_row(conn,table,row):

    try:
        sql = 'DELETE FROM ' + table + ' WHERE rowid=' + row
        cur = conn.cursor()
        cur.execute(sql)

    except Error as e:
        print(e)

def fetch_column_values(conn,col):

    try:
        cursor = conn.cursor()
        sql = 'SELECT ' + col + ' FROM tData'
        ids = cursor.execute(sql).fetchall()
        return ids

    except Error as e:
        print(e)

def fill_from_csv(conn,csv):

    try:
        data = pd.read_csv(csv)
        con = sqlite3.connect("trainingData.db")
        data.to_sql("tData", con, if_exists='append', index=False)
        con.commit()

    except Error as e:
        print(e)


if __name__ == '__main__':
    main()



