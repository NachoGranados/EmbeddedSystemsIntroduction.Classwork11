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
gk = queue.Queue()

# mult function in kpn
def mult():
    while on:
        a = ek.get()
        b = dk.get()
        ak.put(a * b)

# delay function in kpn
def delay():
    while on:
        a = ak.get()
        bk.put(a)

# split 0 function in kpn
def split_0():
    while on:
        a = bk.get()
        dk.put(a)
        ck.put(a)

# split 1 function in kpn
def split_1():
    while on:
        a = fk.get()
        ek.put(a)
        gk.put(a)

# add function in kpn
def add():
    while on:
        a = gk.get()
        fk.put(a + 1)       

th.Thread(target=delay, daemon=True).start()
th.Thread(target=mult, daemon=True).start()
th.Thread(target=add, daemon=True).start()
th.Thread(target=split_0, daemon=True).start()
th.Thread(target=split_1, daemon=True).start()

dk.put(1)
gk.put(0)

while on:
    time.sleep(1)
    print(ck.get())