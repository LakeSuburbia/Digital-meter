import sys
import serial
from datetime import datetime


print ("SAGEMCOM S211")
print ("Control-C to quit")


###################################################################
## Every second, the SAGEMCOM meter sends serial data.           ##
## Every minute, we collect this data and store it temporarily.  ##
## Every hour, we will update our webserver through an API call. ##
###################################################################


# The address where we will collect our data through an hourly API call
APIaddress = "127.0.0.1/API"
# Length of Sagemcom data
datalength=25
# Frequency in seconds
frequency_DATA=10
# Frequency in minutes
frequency_API=60


#Set COM port config (according to the ESMR5.0 specs)
ser = serial.Serial()
ser.baudrate = 115200
ser.bytesize=serial.EIGHTBITS
ser.parity=serial.PARITY_NONE
ser.stopbits=serial.STOPBITS_ONE
ser.xonxoff=0
ser.rtscts=0
ser.timeout=1
ser.port="/dev/ttyUSB0"


#Open COM port
try:
    ser.open()
except:
    sys.exit ("Couldn't open %s."  % ser.name)


# Function in which we load data.
# Except for logging, we don't do anything with this data.
def buffer_data():
    for i in range(datalength):

        #Read 1 line of the serial port
        try:
            ser.readline()

        except:
            sys.exit ("Couldn't read port %s." % ser.name )


# Function in which we store data.
# We store the data we want to use by returning a dictionary of the daily and nightly usage.
def read_data():

    usage=dict()

    usage['timestamp']=datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    #Store the first iteration
    for i in range(datalength):
        #Read 1 line of the serial port
        try:
            rawdata = str(ser.readline())
        except:
            sys.exit ("Couldn't read port %s." % ser.name )
        
        startindex = rawdata.find('(')+1
        stopindex = rawdata.find('*')

        if rawdata.find('1.8.1') != -1:
            if startindex != -1 and stopindex != -1:
                usage['daytime']=(rawdata[startindex:stopindex])
        
        if rawdata.find('1.8.2') != -1:
            if startindex != -1 and stopindex != -1:
                usage['nighttime']=(rawdata[startindex:stopindex])

    #Wait and monitor data
    for i in range(frequency_DATA-1):
        buffer_data()

    return(usage)




def store_data():
    for i in range(frequency_API):
        print(read_data())





store_data()