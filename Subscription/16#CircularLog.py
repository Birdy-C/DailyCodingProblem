'''
This problem was asked by Twitter.

You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
You should be as efficient with time and space as possible, both constant
'''
# circular buffer
class Log(object):
    def __init__(self, N):
        self._log = []
        self.N = N
        self.cur = 0

    def record(self, order_id):
        if len(self._log) == self.N:
            self._log[self.cur] = order_id
        else:
            self._log.append(order_id)
        self.cur = (self.cur+1) % self.N

    def get_last(self, i):
        return self._log[self.cur - i]


testlog = Log(5)
testlog.record(1)
testlog.record(2)
testlog.record(3)
testlog.record(4)
testlog.record(5)
testlog.record(6)
print(testlog.get_last(5))
