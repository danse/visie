import datetime

def data_range(min, max):
    while min < max:
        yield min
        min += datetime.timedelta(1)

def group_by_date(spendings, max_date=None):
    '''
    >>> spendings = [['1', datetime.date(2011, 12, 13), ''], ['1', datetime.date(2011, 12, 15), '']]
    >>> group_by_date(spendings, max_date=datetime.date(2011, 12, 17))
    [('1', datetime.date(2011, 12, 13)), (0, datetime.date(2011, 12, 14)), ('1', datetime.date(2011, 12, 15)), (0, datetime.date(2011, 12, 16))]
    '''
    date_indexed = {}
    for amount, date, description in spendings:
        if type(date) == datetime.datetime:
            date = date.date()
        if date in date_indexed:
            date_indexed[date] += amount
        else:
            date_indexed[date] = amount
    min_date = min(date_indexed.keys())
    if not max_date:
        max_date = datetime.date.today() + datetime.timedelta(1)
    result = []
    for date in data_range(min_date, max_date):
        amount = date_indexed.get(date, 0)
        result.append((amount, date))
    return result

def history(ll):
    '''
    >>> history((1, 1, 1, 1, 1))
    [1.0, 1.0, 1.0, 1.0, 1.0]
    >>> history((1, 2, 3, 4, 5, 6, 7))
    [4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0]
    '''
    s = 0
    r = []
    for l in reversed(ll):
        s+=float(l)
        r.append(s/(len(r)+1))
    r.reverse()
    return r

def profile(spendings, max_date=None, multiplier=1):
    '''
    >>> spendings = [['1', datetime.date(2011, 12, 13), ''], ['1', datetime.date(2011, 12, 15), '']]
    >>> profile(spendings, max_date=datetime.date(2011, 12, 17))
    [(datetime.date(2011, 12, 13), 0.5), (datetime.date(2011, 12, 14), 0.3333333333333333), (datetime.date(2011, 12, 15), 0.5), (datetime.date(2011, 12, 16), 0.0)]
    '''
    spendings = group_by_date(spendings, max_date)
    dates, amounts = [], []
    for spending in spendings:
        dates.append(spending[1])
        amounts.append(spending[0]*multiplier)
    amounts = history(amounts)
    spendings = []
    for date, amount in zip(dates, amounts):
        spendings.append((date, amount))
    return spendings
