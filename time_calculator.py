
class time :
    periods = {0:'AM', 1:'PM'}
    periods_idx = {'AM':0, 'PM':1}

    hours = 0
    minutes = 0
    period = 0

    def __init__(self, time_as_string):
        tas = time_as_string.split()
        self.period = self.periods_idx[tas[1]]
        t = tas[0].split(':')
        self.hours = int(t[0])
        self.minutes = int(t[1])

    def add(self, duration):
        d = duration.split(':')
        m = divmod(self.minutes + int(d[1]), 60)
        self.minutes = m[1]
        h = divmod(self.hours + int(d[0]) + m[0], 12)
        self.hours = h[1]
        self.period = (self.period + h[0]) % 2

    def __str__(self):
        return f'{self.hours}:{self.minutes:02d} {self.periods[self.period]}'

def add_time(start, duration, day = None):

    new_time = time(start)
    new_time.add(duration)
    print(f'{start} + {duration} = {new_time}')

    return str(new_time)
