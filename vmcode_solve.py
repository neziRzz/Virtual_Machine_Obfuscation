result = [""]*(29)
result[0] = bytes.fromhex(hex(0x5113-0x3bd).strip("0x")).decode("utf-8")[::-1]
result[1] = bytes.fromhex(hex(0x306d^0x2e).strip("0x")).decode("utf-8")[::-1]
result[2] = bytes.fromhex(hex(0x336f^0xb).strip("0x")).decode("utf-8")[::-1]
result[3] = bytes.fromhex(hex(0x34c8-0x369).strip("0x")).decode("utf-8")[::-1]
result[4] = bytes.fromhex(hex(0x2b^0x57^0x5f0f).strip("0x")).decode("utf-8")[::-1]
result[5] = bytes.fromhex(hex(0x61^0x61^0x40^0x6823).strip("0x")).decode("utf-8")[::-1]
result[6] = bytes.fromhex(hex(0x2de5+0x34f).strip("0x")).decode("utf-8")[::-1]
result[7] = bytes.fromhex(hex(0x3377^0x46).strip("0x")).decode("utf-8")[::-1]
result[8] = bytes.fromhex(hex(0x1f^0x1c^0x26^0x394b).strip("0x")).decode("utf-8")[::-1]
result[9] = bytes.fromhex(hex(0xf^0x57^0x3f^0x5f54).strip("0x")).decode("utf-8")[::-1]
result[10] = bytes.fromhex(hex(0x37^0x58^0x4c^0x3141).strip("0x")).decode("utf-8")[::-1]
result[11] = bytes.fromhex(hex(0x24^0x5f1d).strip("0x")).decode("utf-8")[::-1]
result[12] = bytes.fromhex(hex(0x1a^0x1c^0x346e).strip("0x")).decode("utf-8")[::-1]
result[13] = bytes.fromhex(hex(0x60ee+0x380).strip("0x")).decode("utf-8")[::-1]
result[14] = bytes.fromhex(hex(0x206a+0x109).strip("0x")).decode("utf-8")[::-1]
for i in result:
    print(i,end='')
