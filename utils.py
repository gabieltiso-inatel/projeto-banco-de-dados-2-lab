import sys
import os

from neo4j import Record

def clear_screen():
    if sys.platform.startswith("win32"):
        os.system("cls")
    else:
        os.system("clear")

def print_record_fields(rec: Record):
    key = rec.keys()[0]
    print("+--------------+")
    for k, v in rec.data()[key].items():
        print(f"{k}: {v}")
    print("+--------------+")
