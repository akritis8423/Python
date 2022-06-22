import threading
def gfg():
    print("python.hub\n")
timer=threading.Timer(5.0, gfg)

timer.start()