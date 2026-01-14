from waveshare_epd import epd2in13_V4 as wavesharelib
from render import render_screen
import subprocess

# ---------- helper ----------

def get_uptime():
    uptime = subprocess.check_output(
        ["uptime", "-p"]
    ).decode().strip()
    return uptime.replace("up ", "").replace("hour", ":").replace("minute", "").replace("s", "").replace(",", "")

def get_wifi_strength():
    try:
        output = subprocess.check_output(
            ["iwconfig", "wlan0"],
            stderr=subprocess.DEVNULL
        ).decode()
        for line in output.split("\n"):
            if "Link Quality" in line:
                quality = line.split("Link Quality=")[1].split()[0]
                value, maxv = quality.split("/")
                return int(int(value) / int(maxv) * 4)
    except:
        pass
    return 0

# ---------- main ----------

stats = {
    "uptime": get_uptime(),
    "wifi": get_wifi_strength(),
    "busy": True
}

config = {
    "font": "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 
    "font_bold": "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
}

epd = wavesharelib.EPD()
epd.init()

image = render_screen(stats, config)
image = image.rotate(180)

epd.display(epd.getbuffer(image))
epd.sleep()