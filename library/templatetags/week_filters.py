from django import template
from itertools import zip_longest
from datetime import datetime, timedelta
from collections import defaultdict

register = template.Library()

@register.filter
def week_list(queryset):
    weeks = defaultdict(list)
    for obj in queryset:
        # Get the year and week number of the object's event_date attribute
        year, week_num, _ = obj.event_date.isocalendar()
        # Add the object to the list of objects for that week
        weeks[year, week_num].append(obj)
    return dict(weeks)

@register.filter
def my_range(value, arg):
    try:
        start, stop, step = value
    except ValueError:
        start, stop = value
        step = arg
    return range(int(start), int(stop) + 1, int(step))