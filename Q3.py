#Ayşenur YETER

from pathlib import Path

source_path = Path("data.bin")
destination_path = Path("newdata.bin")

with source_path.open("rb") as source:
    with destination_path.open("wb") as destination:
        bytes = source.read(8)
        while len(bytes) > 0:
            destination.write(bytes[:6])
            destination.write(bytes[7:8])
            bytes = source.read(8)

#destination_path.rename(source_path)