bytecode = [
    0x0, 0xCFFB289AF4B1D1, 0x0, 0x83, 0x2, 0x1, 0x0, 0x83, 0x3, 0x4, 0x9, 0x5, 0x0, 0x955F7E7A2ABC09,
    0x0, 0x82, 0x2, 0x1, 0x0, 0x82, 0x3, 0x4, 0x9, 0x5, 0x0, 0x171D0EEF6E34564, 0x0, 0x92, 0x2, 0x1,
    0x0, 0x92, 0x3, 0x4, 0x9, 0x5, 0x0, 0x1C8C0106F982D2C, 0x0, 0x78, 0x2, 0x1, 0x0, 0x78, 0x3, 0x4,
    0x9, 0x5, 0x0, 0x1A3DF010DB43D50, 0x0, 0x79, 0x2, 0x1, 0x0, 0x79, 0x3, 0x4, 0x9, 0x5, 0x0, 0x70D52B655429D4,
    0x0, 0xA0, 0x2, 0x1, 0x0, 0xA0, 0x3, 0x4, 0x9, 0x5, 0x0, 0x86BA083DB4A00E, 0x0, 0x8F, 0x2, 0x1,
    0x0, 0x8F, 0x3, 0x4, 0x9, 0x5, 0x0, 0x1EE6D244821E17E, 0x0, 0x93, 0x2, 0x1, 0x0, 0x93, 0x3, 0x4,
    0x9, 0x5, 0x0, 0x21F3E25788406B2, 0x0, 0x8A, 0x2, 0x1, 0x0, 0x8A, 0x3, 0x4, 0x9, 0x5, 0x0, 0x13C0021E70D77B4,
    0x0, 0xA3, 0x2, 0x1, 0x0, 0xA3, 0x3, 0x4, 0x9, 0x5, 0x0, 0x27EDD2385F658C6, 0x0, 0xAA, 0x2,
    0x1, 0x0, 0xAA, 0x3, 0x4, 0x9, 0x5, 0x0, 0xA07DA21EF9E1B4, 0x0, 0x34, 0x2, 0x1, 0x0, 0x34, 0x3,
    0x4, 0x9, 0x5, 0x0, 0xD00E8519E9CC06, 0x0, 0x41, 0x2, 0x1, 0x0, 0x41, 0x3, 0x4, 0x9, 0x5, 0x0, 0xD6DFC3F1E11375,
    0x0, 0x78, 0x2, 0x1, 0x0, 0x78, 0x3, 0x4, 0x9, 0x5, 0x0, 0xEFAA53300DA663, 0x0, 0x8D, 0x2, 0x1,
    0x0, 0x8D, 0x3, 0x4, 0x9, 0x5, 0x0, 0x7568123DB27DB8, 0x0, 0x89, 0x2, 0x1, 0x0, 0x89, 0x3, 0x4,
    0x9, 0x5, 0x0, 0xF174602422164A, 0x0, 0x87, 0x2, 0x1, 0x0, 0x87, 0x3, 0x4, 0x9, 0x5, 0x0, 0x9B991D46E343EE,
    0x0, 0x75, 0x2, 0x1, 0x0, 0x75, 0x3, 0x4, 0x9, 0x5, 0x0, 0x16C43FB0F9B780, 0x0, 0x44, 0x2, 0x1,
    0x0, 0x44, 0x3, 0x4, 0x9, 0x5, 0x0, 0x10C7B1796D09C04, 0x0, 0x44, 0x2, 0x1, 0x0, 0x44, 0x3, 0x4,
    0x9, 0x5, 0x0, 0x5F5CFCF58C8717, 0x0, 0x7A, 0x2, 0x1, 0x0, 0x7A, 0x3, 0x4, 0x9, 0x5, 0x0, 0xD715FDA1220CE0,
    0x0, 0x93, 0x2, 0x1, 0x0, 0x93, 0x3, 0x4, 0x9, 0x5, 0x6
]
vip = 0

while(vip<len(bytecode)):
    if(bytecode[vip] == 0):
        print(f"{hex(vip)}: "+"push "+f"{hex(bytecode[vip+1])}")
        vip += 2
    elif(bytecode[vip] == 1):
        print(f"{hex(vip)}: "+"push")
        vip+=1
    elif(bytecode[vip] == 2):
        print(f"{hex(vip)}: "+"sub")
        vip += 1
    elif(bytecode[vip] == 3):
        print(f"{hex(vip)}: "+"cmp")
        vip += 1
    elif(bytecode[vip] == 4):
        print("jge"+f" {hex(vip+2-bytecode[vip+1])}")
        vip += 2
    elif(bytecode[vip] == 5):
        print(f"{hex(vip)}: "+"print")
        vip += 1
    elif(bytecode[vip] == 6):
        break
'''
0x0: push 0xcffb289af4b1d1
0x2: push 0x83
0x4: sub
0x5: push
0x6: push 0x83
0x8: cmp
jge 0x2
0xb: print
0xc: push 0x955f7e7a2abc09
0xe: push 0x82
0x10: sub
0x11: push
0x12: push 0x82
0x14: cmp
jge 0xe
0x17: print
0x18: push 0x171d0eef6e34564
0x1a: push 0x92
0x1c: sub
0x1d: push
0x1e: push 0x92
0x20: cmp
jge 0x1a
0x23: print
0x24: push 0x1c8c0106f982d2c
0x26: push 0x78
0x28: sub
0x29: push
0x2a: push 0x78
0x2c: cmp
jge 0x26
0x2f: print
0x30: push 0x1a3df010db43d50
0x32: push 0x79
0x34: sub
0x35: push
0x36: push 0x79
0x38: cmp
jge 0x32
0x3b: print
0x3c: push 0x70d52b655429d4
0x3e: push 0xa0
0x40: sub
0x41: push
0x42: push 0xa0
0x44: cmp
jge 0x3e
0x47: print
0x48: push 0x86ba083db4a00e
0x4a: push 0x8f
0x4c: sub
0x4d: push
0x4e: push 0x8f
0x50: cmp
jge 0x4a
0x53: print
0x54: push 0x1ee6d244821e17e
0x56: push 0x93
0x58: sub
0x59: push
0x5a: push 0x93
0x5c: cmp
jge 0x56
0x5f: print
0x60: push 0x21f3e25788406b2
0x62: push 0x8a
0x64: sub
0x65: push
0x66: push 0x8a
0x68: cmp
jge 0x62
0x6b: print
0x6c: push 0x13c0021e70d77b4
0x6e: push 0xa3
0x70: sub
0x71: push
0x72: push 0xa3
0x74: cmp
jge 0x6e
0x77: print
0x78: push 0x27edd2385f658c6
0x7a: push 0xaa
0x7c: sub
0x7d: push
0x7e: push 0xaa
0x80: cmp
jge 0x7a
0x83: print
0x84: push 0xa07da21ef9e1b4
0x86: push 0x34
0x88: sub
0x89: push
0x8a: push 0x34
0x8c: cmp
jge 0x86
0x8f: print
0x90: push 0xd00e8519e9cc06
0x92: push 0x41
0x94: sub
0x95: push
0x96: push 0x41
0x98: cmp
jge 0x92
0x9b: print
0x9c: push 0xd6dfc3f1e11375
0x9e: push 0x78
0xa0: sub
0xa1: push
0xa2: push 0x78
0xa4: cmp
jge 0x9e
0xa7: print
0xa8: push 0xefaa53300da663
0xaa: push 0x8d
0xac: sub
0xad: push
0xae: push 0x8d
0xb0: cmp
jge 0xaa
0xb3: print
0xb4: push 0x7568123db27db8
0xb6: push 0x89
0xb8: sub
0xb9: push
0xba: push 0x89
0xbc: cmp
jge 0xb6
0xbf: print
0xc0: push 0xf174602422164a
0xc2: push 0x87
0xc4: sub
0xc5: push
0xc6: push 0x87
0xc8: cmp
jge 0xc2
0xcb: print
0xcc: push 0x9b991d46e343ee
0xce: push 0x75
0xd0: sub
0xd1: push
0xd2: push 0x75
0xd4: cmp
jge 0xce
0xd7: print
0xd8: push 0x16c43fb0f9b780
0xda: push 0x44
0xdc: sub
0xdd: push
0xde: push 0x44
0xe0: cmp
jge 0xda
0xe3: print
0xe4: push 0x10c7b1796d09c04
0xe6: push 0x44
0xe8: sub
0xe9: push
0xea: push 0x44
0xec: cmp
jge 0xe6
0xef: print
0xf0: push 0x5f5cfcf58c8717
0xf2: push 0x7a
0xf4: sub
0xf5: push
0xf6: push 0x7a
0xf8: cmp
jge 0xf2
0xfb: print
0xfc: push 0xd715fda1220ce0
0xfe: push 0x93
0x100: sub
0x101: push
0x102: push 0x93
0x104: cmp
jge 0xfe
0x107: print
'''