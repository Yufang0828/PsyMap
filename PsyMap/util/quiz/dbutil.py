__author__ = 'Peter_Howe<haobibo@gmail.com>'

import MySQLdb
import psycopg2
import psycopg2.extensions
psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)

cfg = {
    'host':     "192.168.8.1",
    'user':     "psymap",
    'passwd':   "wsi_208",
    "db":       "psymap",
    "charset":  "utf8"
}

cfg_pg = {
    'host':     "127.0.0.1",
    'user':     "postgres",
    'password': "ccpl_817",
    "database": "PsyMap",
}

con_my = MySQLdb.connect(**cfg)
con_pg = psycopg2.connect(**cfg_pg)


def get_cur():
    cur = con_my.cursor(MySQLdb.cursors.DictCursor)
    return cur


def get_cur_pg():
    con_pg.autocommit = True
    cur = con_pg.cursor()
    return cur