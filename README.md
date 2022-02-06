# dht22
> The DHT22 is a basic, low-cost digital temperature and humidity sensor. It uses a capacitive humidity sensor and a thermistor to measure the surrounding air and spits out a digital signal on the data pin (no analog input pins needed). It's fairly simple to use but requires careful timing to grab data. The only real downside of this sensor is you can only get new data from it once every 2 seconds, so when using our library, sensor readings can be up to 2 seconds old.
>
> Simply connect the first pin on the left to 3-5V power, the second pin to your data input pin, and the rightmost pin to ground. Although it uses a single wire to send data it is not Dallas One Wire compatible! If you want multiple sensors, each one must have its own data pin.

**DHT22 on Raspberry Pi** use [Adafruit_DHT](https://github.com/adafruit/Adafruit_Python_DHT) to get data from DHT22, and use [Flask](https://flask.palletsprojects.com/en/2.0.x/) to provide a simple api to get data.

## Prerequisite

- python/python3
- pip/pip3

Run below commands to install packages:

```shell
$ sudo pip3 install flask
$ sudo pip3 install Adafruit_DHT
```

## How to start

- Manually

  1. Connect DHT22 to your pi: connect the first pin on the left to 3.3/5V power, the second pin to GPIO, and the rightmost pin to ground.
  2. Clone the code to your local environment and cd into the folder, update the **DHT_PIN** value in *sensor.py* according to your second pin connection.
  3. Run `python3 sensor.py` in terminal, and visit http://your_raspberrypi_ip:8080 in browser.

- Auto

  1. Follow 1-2 steps in manually start part.

  2. Add follow lines to */etc/rc.local*

     ```shell
     # Start dht22, below line should be your real path.
     /home/pi/github/dht22/start.sh
     ```

## FAQ

1. **ImportError: cannot import name 'Beaglebone_Black_Driver' from 'Adafruit_DHT'**

   This will occur on Raspberry Pi 4B, casued by lacking 4B judgement in Adafruit_DHT. Add below lines to **pi_version()** function in */usr/local/lib/python3.7/dist-packages/Adafruit_DHT/platform_detect.py*

   ```python
   elif match.group(1) == 'BCM2711':
       # Pi 4b
       return 3
   ```

