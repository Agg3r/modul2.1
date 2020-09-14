# Dette er et eksemple på brugen at Thingspeak
import thingspeak
import time
import random


channel_id = 1144538  # PUT CHANNEL ID HERE
write_key = 'M40M4ZFS5HXE63MK' # PUT YOUR WRITE KEY HERE
read_key = 'SJMB5GFP6THSZ5PT' # PUT YOUR READ KEY HERE


def measure(channel):
    try:

        humidity=random.randrange(30,100)
        temperature=random.randrange(-30,100)
        print("Fugt:",humidity)
        print("Temp:",temperature)
        response = channel.update({'field1': temperature, 'field2': humidity})
        #response = channel.update({'field2': humidity})
        read = channel.get({})
        print(read)

    except:
        print("connection failed")


if __name__ == "__main__":
    channel = thingspeak.Channel(id=channel_id, api_key=write_key)
    while True:
        measure(channel)
        # free account has an api limit of 15sec
        time.sleep(15)

