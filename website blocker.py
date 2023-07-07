import datetime as dt
import time
start_time=dt.datetime.now()
end_time=dt.datetime(2022,12,4)
site_block=list(input("Enter the name of website: "))
host_path=""
redirect=""

while True:
    if start_time<end_time:
        print("start Blocking")
        with open(host_path,"r+") as host_file :
            content=host_file.read()
            for website in site_block:
                if website not in content:
                    host_file.write(redirect+" "+website+"\n")
                else:
                    pass
    else:
        with open(host_path, "r+") as host_file:
            content=host_file.readlines()
            host_file.seek(0)
            for lines in content:
                if not any(website in lines for website in site_block):
                    host_file.write(lines)
            host_file.truncate()
        time.sleep(5)
