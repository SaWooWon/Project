from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Events

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()


	def formatday(self, day, contents):
		contents_per_day = contents.filter(date__day=day)
		d = ''
		for event in contents_per_day:
			d += f'<li> {Events.title} </li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
		return '<td></td>'

	def formatweek(self, theweek, contents):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, contents)
		return f'<tr> {week} </tr>'


	def formatmonth(self, withyear=True):
		contents = Events.objects.filter(date__year=self.year, date__month=self.month)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, contents)}\n'
		return cal