#import matplotlib.ft2font
import speedtest
import datetime
import csv
import time
import os
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

FILES_STORAGE_PATH = os.path.dirname(os.path.realpath(__file__))
if FILES_STORAGE_PATH == "C:\\WINDOWS\\system32":
    FILES_STORAGE_PATH = "C:\\Speedtest\\"
    try:
        os.chdir(FILES_STORAGE_PATH)
    except IOError:
        print("Unable to change directory")
times = []
datetimes = []
download = []
upload = []

s = speedtest.Speedtest()
timestamp = time.strftime("%y_%m_%d_")
filename = timestamp + 'speedtest_results.csv'
try:
    speedcsv = open(filename, mode='r', newline='')
    print("File already exists, appending data")
    speedcsv.close()
except IOError:
    with open(filename, mode='w', newline='') as speedcsv:
        print("File does not exist, creating")
        csv_writer = csv.DictWriter(speedcsv, fieldnames=['time', 'downspeed', 'upspeed'])
        csv_writer.writeheader()
        speedcsv.close()


time_now = datetime.datetime.now().strftime("%H:%M")
datetime_now = datetime.datetime.now()
with open(filename, mode='a', newline='') as speedcsv:
    csv_writer = csv.DictWriter(speedcsv, fieldnames=['time', 'downspeed', 'upspeed'])
    downspeed = round((round(s.download()) / 1048576), 2)
    upspeed = round((round(s.upload()) / 1045876), 2)
    print(f"Time: {time_now}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s")
    csv_writer.writerow({'time': datetime_now,
                         'downspeed': downspeed,
                         'upspeed': upspeed
                         })
    speedcsv.close()

with open(filename, mode='r') as speedcsv:
    plots = csv.reader(speedcsv, delimiter=',')
    next(speedcsv)
    for row in plots:
        #datetime = datetime.datetime.strptime(, '%Y-%m-%d %H:%M:%S.%f'
        times.append(str(row[0]))
        download.append(float(row[1]))
        upload.append(float(row[2]))
    for csv_timestamp in times:
        date_time = datetime.datetime.strptime(csv_timestamp, '%Y-%m-%d %H:%M:%S.%f')
        datetimes.append(date_time)
    speedcsv.close()
    
    dates = matplotlib.dates.date2num(datetimes)
    
    plt.figure()
    plt.plot_date(dates, download, 'g-', label='download')
    plt.plot_date(dates, upload, 'b-', label='upload')
    ax = plt.gca()
    plt.xticks(rotation=90)
    for label in ax.get_xaxis().get_ticklabels()[::2]:
        label.set_visible(False)
    plt.xlabel('Time')
    plt.ylabel('Speed in Mb/s')
    title = "Maidin Gheal Internet Speed on " + time.strftime("%a the %d of %B")
    plt.title(title)
    plt.legend()
    plt.tight_layout()
    plt.savefig("current_speed.jpg")
    filename = timestamp + 'speedtest_results.jpg'
    plt.savefig(filename)

    
    times = []
    download = []
    upload = []

