# Juan Ignacio Navarro
# Jose David Sánchez
# Mónica Waterhouse
# Jose Ignacio Granados

import queue 
import threading as th
import time

on = True

ak = queue.Queue()
bk = queue.Queue()
ck = queue.Queue()
dk = queue.Queue()
ek = queue.Queue()
fk = queue.Queue()

# add function in kpn
def add():
    while on:
        a = ck.get()
        b = fk.get()
        ak.put(a + b)

# delay 1 function in kpn
def delay1():
    while on:
        bk.put(ak.get())

# split function in kpn
def split():
    while on:
        a = bk.get()
        ck.put(a)
        ek.put(a)
        dk.put(a)

# deleay 0 function in kpn
def delay0():
    while on:
        fk.put(ek.get())

th.Thread(target=add, daemon=True).start()
th.Thread(target=delay1, daemon=True).start()
th.Thread(target=split, daemon=True).start()
th.Thread(target=delay0, daemon=True).start()

ck.put(1)
fk.put(1)

while on:
    time.sleep(1)
    print(dk.get())