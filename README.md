# embeds

## PlatformIO (C/C++)

### Requirements

- PlatformIO CLI installed on the host.
- USB type C to USB type C cable to connect the peripheral (board) to the host (computer).

### Getting Started

First find the port of the peripheral.

```bash
$ pio device list
```

You should see something like this:

```bash
/dev/cu.usbmodem1101
--------------------
Hardware ID: USB ...
Description: RaspberryPi Pico
```

Then compile and upload the code to the peripheral.


```bash
$ pio run -t upload --upload-port /dev/tty.usbmodem101
```

```bash
$ pio device monitor
```

```bash
$ pio run -t clean
```

## MicroPython

### Getting Started

Download the UF2 file from the [official website](https://micropython.org/download/).

Flash the UF2 file to the peripheral.
Install rshell, then connect to the peripheral.

```bash
$ cd rp2040/micropython/src
$ rshell
$ cp main.py /pyboard
```

Then reset the peripheral by pressing the reset button.
Code should start running.

rshell is a remote MicroPython shell tool for accessing and managing files on the device.rshell represents your device’s flash storage as /pyboard.
Use the special filename main.py to automatically execute your program on boot.

You can also use the REPL to interact with the device.

```bash
$ rshell
$ repl
```

### Other ways to connect to the REPL

Open REPL with either screen or minicom.

```bash
$ screen /dev/tty.usbmodem101 115200
$ minicom -D /dev/tty.usbmodem101 -b 115200
```

To exit screen, press `Ctrl + A` followed by `K` and then `Y`, or `Ctrl + A` followed by `:quit`.

### Board specific installation instructions

- esp32-s3-wroom-1

```bash
$ esptool.py -p /dev/tty.usbmodem101 erase_flash
$ esptool.py -p /dev/tty.usbmodem101 write_flash -z 0 firmware.bin
```

- rp2040

connect the board with the boot button pressed, then copy the UF2 file to the RPI-RP2 drive.
