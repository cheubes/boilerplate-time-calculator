
class time :
    hours = 0
    minutes = 0
    period = 'AM'

    def __init__(self, time_as_string):
        tas = time_as_string.split()
        self.period = tas[1]
        t = tas[0].split(':')
        self.hours = int(t[0])
        self.minutes = int(t[1])

    def add(self, duration):
        d = duration.split(':')
        self.hours += int(d[0])
        self.minutes += int(d[1])

    def __str__(self):
        return f'{self.hours}:{self.minutes} {self.period}'

def add_time(start, duration, day = None):

    new_time = time(start)
    new_time.add(duration)
    print(f'{start} + {duration} = {new_time}')

    return str(new_time)
