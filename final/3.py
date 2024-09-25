import asyncio
import random
import time

class SolarCell:
    def __init__(self, id):
        self.id = id
        self.hardware_readtime = random.randint(1, 3)
        print(f"Solar Cell {id} hardware speed: {self.hardware_readtime}")
    
    async def read_voltage(self):
        voltage = round(random.uniform(3.2, 6.0), 2)
        await asyncio.sleep(self.hardware_readtime)
        return voltage

async def read_from_solar_cell(solar_cell):
    while True:
        voltage = await solar_cell.read_voltage()
        print(f"{time.ctime()} Solar Cell #{solar_cell.id} Voltage: {voltage} V")

async def main():
    num_cells = 5
    print(f"จำนวนแผงโซล่าเซลที่สร้าง: {num_cells}")
    solar_cells = [asyncio.create_task(read_from_solar_cell(SolarCell(i+1))) for i in range(num_cells)]
    
    try:
        await asyncio.gather(*solar_cells)
    except asyncio.CancelledError:
        print("\nโปรแกรมหยุดทำงาน.")
    
if __name__ == "__main__":
    asyncio.run(main())  