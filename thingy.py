import dbus, time, socket, sys

# Disclaimer: I am not responsible for any misuse of the following script.
# Created for educational and experimental purposes only.

bus = dbus.SessionBus()
obje = bus.get_object("org.cinnamon.ScreenSaver", "/")
inte = dbus.Interface(obje, "org.cinnamon.ScreenSaver")

s = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
s.connect("/var/run/acpid.socket")

while True:
    try:
        msg = s.recv(4096, socket.MSG_DONTWAIT)
        if "jack/headphone HEADPHONE unplug" in msg.decode('utf-8') and inte.GetActive():
            inte.SetActive(False)
            sys.exit(0)
    except BlockingIOError as e:
        pass
