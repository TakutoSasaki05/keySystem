import RPi.GPIO as GPIO
import time

# GPIOピンの番号付けをBCMモードに設定
GPIO.setmode(GPIO.BCM)

# センサーを接続したGPIOピン番号
SENSOR_PIN = 17

# SENSOR_PINを入力モードに設定
# プルアップ抵抗は物理的に接続しているため、ここではプルダウン/プルアップ設定は不要
GPIO.setup(SENSOR_PIN, GPIO.IN)

print("センサーの準備ができました。Ctrl+Cで終了します。")

try:
    while True:
        # センサーの状態を読み取る
        sensor_state = GPIO.input(SENSOR_PIN)

        if sensor_state == GPIO.LOW:
            # しゃ光時ONモードの場合、LOWが検出状態
            print("【検出】物体があります。")
        else:
            print("（待機中）物体はありません。")
        
        # 1秒待機
        time.sleep(1)

except KeyboardInterrupt:
    print("プログラムを終了します。")

finally:
    # GPIOをクリーンアップ
    GPIO.cleanup()