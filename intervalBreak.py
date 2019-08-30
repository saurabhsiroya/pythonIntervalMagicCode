import time
from datetime import datetime, timedelta


## the below function will help to break the time into range into intervals, these intervals are configurable
def datetime_range(start, end, delta):
    print("\nstart_datetime_range: {}".format(start))
    print("end_datetime_range: {}\n".format(end))
    current = start
    while current < end:
        yield current
        current += delta


start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1567037180.277))  # epoch time to datetime string
end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1567093959.98))  # epoch time to datetime string

datetime_check = datetime(2016, 9, 1, 7)

new_start_time_check = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")  # string to datetime format
new_end_time_check = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")  # string to datetime format

print("\ndatetime_check:{}".format(datetime_check))
print("datetime_check obj type:{}".format(type(datetime_check)))
print("\new_start_time_check:{}".format(new_start_time_check))
print("new_start_time_check obj type:{}".format(type(new_start_time_check)))


# dts = [
#     datetime.strftime("%Y-%m-%d %H:%M:%S")
#     for datetime in datetime_range(new_start_time_check, new_end_time_check, timedelta(minutes=30))
# ]

# print(dts)


def lower_bound(start_time):
    print("datetime.min: {}".format(datetime.min))
    rounded = start_time - (start_time - datetime.min) % timedelta(minutes=30)
    print(timedelta(minutes=30))
    return rounded


def upper_bound(dt, delta):
    return dt + (datetime.min - dt) % delta


upper_bound_value = upper_bound(new_end_time_check, timedelta(minutes=30))
print("The upper_bound_interval_value: {}".format(upper_bound_value))

lower_bound_value = lower_bound(new_start_time_check)
print("The lower_bound_interval_value: {}".format(lower_bound_value))


dts = [
    datetime.strftime("%Y-%m-%d %H:%M:%S")
    for datetime in datetime_range(lower_bound_value, upper_bound_value, timedelta(minutes=30))
]

print(dts)

import datetime

e = 1524349374
print(datetime.datetime.fromtimestamp(e))

# def convert_datetime_to_epoc(datetime_value):
#     permissions = []
#     for i in dts:
#         print(i)
#         datetime_to_epoch = datetime.datetime.fromtimestamp(i)
#         permissions.append(datetime_to_epoch)
#     return permissions
#
#
# dt2 = convert_datetime_to_epoc(dts)
# print(dt2)
