from time import time
from threading import Timer


class MyTimer(Timer):
    started_at = None

    def start(self):
        self.started_at = time()
        Timer.start(self)

    @property
    def elapsed(self):
        return time() - self.started_at

    @property
    def remaining(self):
        return self.interval - self.elapsed
