import threading

class P2ESThread(threading.Thread):

    def __init__(self, idx, CONFIG, errors_queue):
        threading.Thread.__init__(self)
        self.idx = idx
        self.CONFIG = CONFIG
        self.errors_queue = errors_queue
