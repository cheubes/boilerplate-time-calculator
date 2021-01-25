
class time :

    periods = {0:'AM', 1:'PM'}
    periods_idx = {'AM':0, 'PM':1}

    hours = 0
    minutes = 0
    period = 0
    day = ''
    days_after = ''

    def __init__(self, time_as_string, day):
        tas = time_as_string.split()
        self.period = self.periods_idx[tas[1]]
        t = tas[0].split(':')
        self.hours = int(t[0])
        self.minutes = int(t[1])
        if day :
            self.day = ', ' + day

    def add(self, duration):
        d = duration.split(':')
        m = divmod(self.minutes + int(d[1]), 60)
        self.minutes = m[1]
        h = divmod(self.hours + int(d[0]) + m[0], 12)
        self.hours = h[1]
        p = divmod(self.period + h[0], 2)
        if p[0] == 1 :
            self.days_after = '(next day)'
        if p[0] > 1 :
            self.days_after = f'({p[0]} days later)'
        self.period = p[1]
        if self.hours == 0 :
            self.hours = 12

    def __str__(self):
        return f'{self.hours}:{self.minutes:02d} {self.periods[self.period]}{self.day} {self.days_after}'.rstrip()


def add_time(start, duration, day = None):

    new_time = time(start, day)
    new_time.add(duration)

    return str(new_time)
