from main import Os
import sys 

run = Os()
try:
    run.send_back()
except AssertionError as y:
    print(y)
