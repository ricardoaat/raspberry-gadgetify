import argparse
from signal import pause
import pydbus

parser = argparse.ArgumentParser()
parser.add_argument('d', help='BD_ADDR of network server')
parser.add_argument('u', help='Server type to connect to [gn, panu, nap]')
args = parser.parse_args()

device = args.d
device_path = f"/org/bluez/hci0/dev_{device.replace(':', '_')}"
bus = pydbus.SystemBus()

network = bus.get('org.bluez', device_path)['org.bluez.Network1']
print(f'Connecting to {args.d} as a {args.u}')
network.Connect(args.u)
try:
    print('Press CTRL-C to disconnect')
    pause()
except KeyboardInterrupt:
    print('Disconnecting from network')
network.Disconnect()
