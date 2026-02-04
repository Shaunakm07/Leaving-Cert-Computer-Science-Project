import serial
import time
import csv
import serial.tools.list_ports

# List available ports (optional)
ports = serial.tools.list_ports.comports()
for port in ports:
    print(port.device, "-", port.description)

# Open serial port
ser = serial.Serial(
    port='/dev/cu.usbmodem21301',
    baudrate=9600,
    timeout=1
)

time.sleep(2)  # let Arduino reset

# Open both CSV files
raw_file = open("serial_raw_data.csv", mode="w", newline="")
clean_file = open("serial_cleaned_data.csv", mode="w", newline="")

raw_writer = csv.writer(raw_file)
clean_writer = csv.writer(clean_file)

# Write headers
raw_writer.writerow(["timestamp", "raw_data"])
clean_writer.writerow(["timestamp", "cleaned_data"])

print("Logging data... Press Ctrl+C to stop.")

try:
    while True:
        if ser.in_waiting:
            raw_line = ser.readline()   # bytes
            cleaned_line = raw_line.decode(
                "utf-8", errors="ignore"
            ).strip()

            timestamp = time.time()

            # Console output
            print("RAW:", raw_line)
            print("CLEAN:", cleaned_line)

            # Write to CSVs
            raw_writer.writerow([timestamp, raw_line])


            clean_writer.writerow([timestamp, cleaned_line])

            raw_file.flush()
            clean_file.flush()

except KeyboardInterrupt:
    print("\nStopped by user.")

finally:
    ser.close()
    raw_file.close()
    clean_file.close()
