# This is a sample Python script.
import usb.core

# Find all connected USB devices
devices = usb.core.find(find_all=True)

# Iterate over the devices and print information about each one
num_devices = 0
for device in devices:
    # Check if the device is an external device
    print(device)
    if device.port_number is not None:
        num_devices += 1
        print(f"Device: {device.manufacturer} {device.product}")
        print(f"Port number: {device.port_number}")

print(f"Number of external devices: {num_devices}")
