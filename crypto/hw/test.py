def i2c_simulation(data, slave_address):
    transmission = []

    # slave Address (7 bits) + R/W bit (0 for write)
    address = f"{slave_address:07b}0"  # convert address to binary and append R/W bit
    transmission.append(address)

    for row in data:
        for byte in row:
            byte_bin = f"{byte:08b}"  
            transmission.append(byte_bin)  
            transmission.append("0")  

    return ''.join(transmission)  

# data bitmap
data = [
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,0,255,255,0,0,0,255,0,0,0,255,255,255,0,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,0,255,255,255,255,0,255,255,0,255,255,255,255,255,0,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,0,255,255,255,255,255,0,255,255,0,0,255,255,255,0,0,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,0,255,255,255,255,255,0,255,255,0,255,255,255,255,0,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,0,255,255,255,255,255,0,255,255,0,255,255,255,255,255,0,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,0,0,0,255,255,0,255,255,0,255,255,255,255,255,0,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,0,255,255,0,0,0,255,255,0,0,0,255,255,255,0,0,255,0,0,0,255,0,0,255,0,0,255,255],
[255,255,255,255,0,255,255,255,255,0,255,255,0,255,255,255,255,255,0,255,255,0,255,0,255,0,255,0,255,0,255,255],
[255,255,255,255,0,255,255,0,0,0,255,255,0,255,255,255,255,255,0,255,255,0,255,0,255,0,255,255,255,0,255,255],
[255,255,255,255,0,255,255,0,255,255,255,255,0,255,255,255,255,255,0,255,255,0,0,0,255,0,255,255,255,0,255,255],
[255,255,255,255,0,255,255,0,0,0,0,255,0,0,0,255,0,255,0,0,255,0,0,0,255,0,255,255,255,0,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,0,0,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255],
[255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255,255]]

# slave address
slave_address = 0x10  
transmission_output = i2c_simulation(data, slave_address)
print(transmission_output)
with open('test.txt', 'w') as file:
    file.write(transmission_output)