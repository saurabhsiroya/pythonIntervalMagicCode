import time
from datetime import datetime, timedelta


def date_range(start, end, intv):
    from datetime import datetime

    start = datetime.strptime(start, "%Y%m%d")
    end = datetime.strptime(end, "%Y%m%d")
    print("start:{}".format(start))
    print("end:{}".format(end))
    diff = (end - start) / intv
    print(diff)
    for i in range(intv):
        yield (start + diff * i).strftime("%Y%m%d")
    yield end.strftime("%Y%m%d")


def datetime_range(start, end, delta):
    print("\nstart_datetime_range: {}".format(start))
    print("end_datetime_range: {}\n".format(end))
    current = start
    while current < end:
        yield current
        current += delta


start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1567037180.277))
end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1567093959.98))
# dts = list(datetime_range(start_time, end_time, timedelta(minutes=30)))
datetime_check = datetime(2016, 9, 1, 7)
start_time_check = start_time
end_time_check = end_time
new_start_time_check = datetime.strptime(start_time_check, "%Y-%m-%d %H:%M:%S")
new_end_time_check = datetime.strptime(end_time_check, "%Y-%m-%d %H:%M:%S")

print("\ndatetime_check:{}".format(datetime_check))
print("datetime_check obj type:{}".format(type(datetime_check)))
print("\nstart_time_check:{}".format(start_time_check))
print("start_time_check obj type:{}".format(type(start_time_check)))
print("\new_start_time_check:{}".format(new_start_time_check))
print("new_start_time_check obj type:{}".format(type(new_start_time_check)))

# dts = [datetime_range(new_start_time_check, new_end_time_check, timedelta(minutes=30))]

dts = [
    datetime.strftime("%Y-%m-%d %H:%M:%S")
    for datetime in datetime_range(new_start_time_check, new_end_time_check, timedelta(minutes=30))
]

# dts = [
#     dt.strftime("%Y-%m-%d T%H:%M Z")
#     for dt in datetime_range(datetime(2016, 9, 1, 7), datetime(2016, 9, 1, 9 + 12), timedelta(minutes=30))
# ]

# print(dts)
# print(type(dts))


# start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1567037180.277))
# end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1567093959.98))
# print("start_time:{}".format(start_time))
# print("end_time:{}".format(end_time))
#
# begin = "20150101"
# end = "20150331"
#
# # begin = start_time
# # end = end_time
#
# final_data = list(date_range(begin, end, 10))
# print(final_data)


def ceil_dt(dt, delta):
    return dt + (datetime.min - dt) % delta


# now = datetime.now()
now = new_start_time_check
print(now)
print("The upper_bound_interval_value: {}".format(ceil_dt(now, timedelta(minutes=30))))


def rounded_to_the_last_30th_minute_epoch(start_time):
    # now = datetime.now()
    now = start_time
    print("datetime.min: {}".format(datetime.min))
    rounded = now - (now - datetime.min) % timedelta(minutes=30)
    print(timedelta(minutes=30))
    return rounded


lower_bound = rounded_to_the_last_30th_minute_epoch(new_start_time_check)
print("The lower_bound_interval_value: {}".format(lower_bound))


# the below function takes the list of epoch values and convert it to datetime format
def convert_datetime_to_epoc(datetime_value):
    permissions = []
    for i in dts:
        print(i)
        datetime_to_epoch = datetime.datetime.fromtimestamp(i)
        permissions.append(datetime_to_epoch)
    return permissions
