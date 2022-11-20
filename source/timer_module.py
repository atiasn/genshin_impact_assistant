import time


class Timer:
    def __init__(self, diff_start_time=0):
        self.start_time = time.time()
        self.start_time = self.start_time - diff_start_time
        self.end_time = time.time()

    def reset(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

    def get_delta_time(self):
        self.stop()
        return self.end_time - self.start_time

    def get_diff_time(self):  # new
        self.stop()
        return self.end_time - self.start_time

    def loop_time(self):
        t = self.get_diff_time()
        self.reset()
        return t


'''class 流速/fps检测器 之后再写'''
