import datetime

row = ['igaV', '3 いいね', 'kissyossy', '23MB', '2021/2/26（金） 10:15']
name_raw = row[0]
like_raw = row[1]
creator_raw = row[2]
size_raw = row[3]
date_raw = row[4]

def trim_like(raw_d):
    like = raw_d.split(' ')[0]
    return like

def trim_size(raw_d):
    size = raw_d[:-2]
    unit = raw_d[-2:]
    s = int(size)
    if unit == 'GB':
        s *= 1000
    elif unit == 'KB':
        s /= 1000
    return s

def trim_date(raw_d):
    date_string = raw_d.split('（')[0]
    date_all = datetime.datetime.strptime(date_string, '%Y/%m/%d')
    date = datetime.date(date_all.year, date_all.month, date_all.day)
    return date

def calc_date_interval(date1, date2):
    return abs(date1-date2).days

def trim_all_data(name_r, like_r, creator_r, size_r, date_r):
    name = name_r
    like = trim_like(like_r)
    creator = creator_r
    size = trim_size(size_r)
    date = trim_date(date_r)
    data = [name, like, creator, size, date]
    return data
