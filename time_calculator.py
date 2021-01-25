
class time :

    periods = {0:'AM', 1:'PM'}
    periods_idx = {'AM':0, 'PM':1}
    days = {1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday', 7:'Sunday'}
    days_idx = {'Monday':1, 'Tuesday':2, 'Wednesday':3, 'Thursday':4, 'Friday':5, 'Saturday':6, 'Sunday':7}

    hours = 0
    minutes = 0
    period = 0
    day = None
    days_after = None

    def __init__(self, time_as_string, day):
        tas = time_as_string.split()
        self.period = self.periods_idx[tas[1]]
        t = tas[0].split(':')
        self.hours = int(t[0])
        self.minutes = int(t[1])
        if day :
            self.day = self.days_idx[day.title()]

    def add(self, duration):
        d = duration.split(':')
        m = divmod(self.minutes + int(d[1]), 60)
        self.minutes = m[1]
        h = divmod(self.hours + int(d[0]) + m[0], 12)
        self.hours = h[1]
        p = divmod(self.period + h[0], 2)
        if self.day :
            self.day += divmod(p[0], 7)[1]
            if self.day > 7 :
                self.day = self.day % 7
        if p[0] == 1 :
            self.days_after = '(next day)'
        if p[0] > 1 :
            self.days_after = f'({p[0]} days later)'
        self.period = p[1]
        if self.hours == 0 :
            self.hours = 12

    def __str__(self):
        str = f'{self.hours}:{self.minutes:02d} {self.periods[self.period]}'.rstrip()
        if self.day :
            str += f', {self.days[self.day]}'
        if self.days_after :
            str += f' {self.days_after}'
        return str


def add_time(start, duration, day = None):

    new_time = time(start, day)
    new_time.add(duration)

    return str(new_time)
