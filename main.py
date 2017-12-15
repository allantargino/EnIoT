import numpy as np
import matplotlib.pyplot as plt
import sys
import iothub_service_client
import json
from iothub_service_client import IoTHubRegistryManager, IoTHubRegistryManagerAuthMethod
from iothub_service_client import IoTHubDeviceStatus, IoTHubError
from d2cMsgSender import D2CMsgSender
from datetime import datetime

def get_sin_data(freq, A, n):
    f_sin = freq # Hz
    f = np.arange(0.0, f_sin, f_sin / n)
    t = 2 * np.pi * f
    y = A * np.sin(t)
    return t, y, 

def get_fft(t, y, n):
    sp = np.fft.fft(y)
    freq = np.fft.fftfreq(t.shape[-1]) * n
    freq = freq[:n/2]
    amp = abs(sp.imag)[:n/2] / (n/2)
    return amp, freq


def get_simulation(code, n):
    return {
        0: get_sin_data(8.0,  2, n),
        1: get_sin_data(5.0,  1, n),
        2: get_sin_data(15.0, 1, n),
        3: get_sin_data(23.0, 1, n),
        4: get_sin_data(38.0, 1, n)
        }[code]

n = 60
error = 0
t, y = get_simulation(0, n)
if(error >0):
    te, ye = get_simulation(error, n)
    y = y + ye

connectionString = "HostName=grupo8.azure-devices.net;SharedAccessKeyName=iothubowner;SharedAccessKey=SLnGVhKQbTQcLqJJyjMrneV+YsZgEUVWkrl18nLj0hg="
deviceId = "MyFirstPythonDevice"

timestamp = str(datetime.now())
values = json.dumps(list(y))

message = "{\"timestamp\":\""  + timestamp +"\",\"deviceid\":\"MyFirstPythonDevice\",\"values\": " + values + "}"
sender = D2CMsgSender(connectionString)
sender.sendD2CMsg(deviceId, message)

# plt.plot(t, y)
# plt.show()

# amp, freq = get_fft(t, y, n)

# plt.plot(freq, amp)
# plt.xlabel("Frequency(Hz)")
# plt.ylabel("Amplitude")
# plt.show()
