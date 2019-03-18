import datetime


def date_filter(entry):
    """This function returns True if the entry's published date is newer
    than one day."""

    now = datetime.datetime.now()
    interval = datetime.timedelta(days=1)
    entry_published = datetime.datetime.strptime(
        entry['published'][:-4],
        '%a, %d %b %Y %H:%M:%S',
    )
    return now - entry_published <= interval
