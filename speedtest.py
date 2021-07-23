# Internet-Speedtest
# Users can not only calculate their download and upload speed and ping to the best server but also see where the best server is located.

import speedtest
import time

test = speedtest.Speedtest()

print("Loading Server List...")
test.get_servers() # gets list of the servers

time.sleep(1)
print("Choosing Best Server...")
best_server = test.get_best_server() # chooses best server

print(f"Your Internet Provider is found as {best_server['sponsor']} Located In {best_server['country']}, {best_server['name']}")

print("Calculating Download Speed...")
download_speed =  test.download() # download speed
time.sleep(1)
print("Calculating Upload Speed...")
upload_speed =  test.upload() # upload speed
ping_result = test.results.ping # ping result

print(f"Your Download Speed is {download_speed / 1024 / 1024: .2f} Mbit/s")
time.sleep(1)
print(f"Your Upload Speed is {upload_speed / 1024 / 1024: .2f} Mbit/s")
print(f"Your Ping is {ping_result: .2f} ms")

