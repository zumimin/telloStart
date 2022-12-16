import socket
import math
from time import sleep

# NOTE: 円形用です

# 設定値関連
radius = 50
n_rect = 6
t_speed = 60
t_dir = "ccw"

# 1箇所での旋回角度計算
fly_angle = 360 / n_rect
# 1飛行距離(1辺の長さ)計算
fly_leg = int(2 * radius * math.sin(math.pi / n_rect))

# TelloのIPアドレスとポート
tello_ip = "192.168.10.1"
tello_port = 8889
# 受信側のアドレスとポート(戻り)
my_ip = ""
my_port = 9000
my_addr = (my_ip, my_port)

# ソケット生成（受信側）
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(my_addr)

# ------------------------ 関数定義


# 受信処理関数
def recv():
    data, server = sock.recvfrom(1518)
    print(data.decode(encoding="utf-8"))


# 離陸処理
def do_takeoff():
    sock.sendto(b"command", (tello_ip, tello_port))
    recv()
    sock.sendto(b"takeoff", (tello_ip, tello_port))
    recv()
    sleep(10)


# 着陸処理
def do_land():
    sock.sendto(b"land", (tello_ip, tello_port))
    recv()


# 離陸以外の処理
def do_cmds(tello_cmd, tello_param):
    t_cmd = tello_cmd + " " + tello_param
    t_bytes = t_cmd.encode()
    sock.sendto(t_bytes, (tello_ip, tello_port))
    recv()


# ---------------------------- メインの処理
if __name__ == "__main__":
    print("Takeoff")
    # 離陸
    do_takeoff()

    #
    # do_cmds("speed", str(t_speed))

    # 旋回させる
    # for i in range(n_rect):
    #     print("Fly " + str(fly_leg) + " cm")
    #     do_cmds("forward", str(fly_leg))
    #     print("Rotate " + t_dir + " " + str(fly_angle) + " degree")
    #     do_cmds(t_dir, str(fly_angle))

    # sleep(5)

    print("Land")

    # 着陸
    # do_land()
