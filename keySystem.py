import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
SENSOR_PIN = 17
GPIO.setup(SENSOR_PIN, GPIO.IN)

try:
    while True:
        sensor_state = GPIO.input(SENSOR_PIN)
        if sensor_state == GPIO.LOW
            print("物体あり")
        else:
            print("物体なし")

        time.sleep(1)

except KeyboardInterrupt:
    print("プログラムを終了")

finally:
    GPIO.cleanup()
