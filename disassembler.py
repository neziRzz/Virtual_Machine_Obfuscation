# bytecode =(0 or 1) 0x6 (2 byte operand) <=> push operand (if 0 then push byte and if 1 then push word) ins = 4 byte
# bytecode = 0x5 <=> shift right with the previous value on stack (if 0 then byte and if 1 then word)
# bytecode = 0x8 <=> logical and with the previous value on stack (if 0 then byte and if 1 then word)
# bytecode = 0x2 <=> add (if 0 then byte and if 1 then word)
# bytecode = 0x1 <=> xor (if 0 then byte and if 1 then word)
# bytecode = 0x0 <=> cmp 2 value on stack (if 0 then byte and if 1 then word)
# bytecode = 0x7 <=> pop from stack (if 0 then byte and if 1 then word)
# bytecode = 0x3 <=> sub 2 value from stack (if 0 then byte and if 1 then word)
# bytecode = 0x4 <=> shift left with the previous value on stack (if 0 then byte and if 1 then word)
# [rcx+18h] <virt.sp>
# rbx <virt.ins_pointer>
bytecode =[0x00, 0x06, 0x00, 0x01, 0x01, 0x06, 0x0C, 0x0D, 0x01, 0x06, 0x00, 0x08, 0x01, 0x05, 0x01, 0x06, 0x22, 0x38, 0x01, 0x06, 0xFF, 0x00, 0x01, 0x08, 0x01, 0x02, 0x01, 0x06, "input[1]", "input[0]", 0x01, 0x01, 0x01, 0x06, 0x69, 0x4E, 0x01, 0x00, 0x00, 0x07, 0x00, 0x00, 0x01, 0x06, 0x0C, 0x0D, 0x01, 0x06, 0x2D, 0x41, 0x01, 0x02, 0x01, 0x06, 0x00, 0x08, 0x01, 0x05, 0x01, 0x06, 0x22, 0x38, 0x01, 0x06, 0x55, 0x22, 0x01, 0x01, 0x01, 0x06, 0xFF, 0x00, 0x01, 0x08, 0x01, 0x02, 0x01, 0x06, "input[3]", "input[2]", 0x01, 0x01, 0x01, 0x06, 0x32, 0x6A, 0x01, 0x00, 0x00, 0x07, 0x00, 0x00, 0x01, 0x06, 0x49, 0x30, 0x01, 0x06, 0x00, 0x08, 0x01, 0x05, 0x01, 0x06, 0x3E, 0x5E, 0x01, 0x06, 0xFF, 0x00, 0x01, 0x08, 0x01, 0x02, 0x01, 0x06, "input[5]", "input[4]", 0x01, 0x01, 0x01, 0x06, 0x45, 0x0A, 0x01, 0x00, 0x00, 0x07, 0x00, 0x00, 0x01, 0x06, 0x3B, 0x20, 0x01, 0x06, 0x00, 0x08, 0x01, 0x05, 0x01, 0x06, 0x6B, 0x2D, 0x01, 0x06, 0xFF, 0x00, 0x01, 0x08, 0x01, 0x02, 0x01, 0x06, "input[7]", "input[6]", 0x01, 0x01, 0x01, 0x06, 0x5B, 0x78, 0x01, 0x00, 0x00, 0x07, 0x00, 0x00, 0x01, 0x06, 0x2B, 0x79, 0x01, 0x06, 0x00, 0x08, 0x01, 0x05, 0x01, 0x06, 0x70, 0x41, 0x01, 0x06, 0xFF, 0x00, 0x01, 0x08, 0x01, 0x02, 0x01, 0x06, "input[8]", "input[9]", 0x01, 0x01, 0x01, 0x06, 0x37, 0x45, 0x01, 0x00, 0x00, 0x07, 0x00, 0x00, 0x01, 0x06, 0x78, 0x79, 0x01, 0x06, 0x00, 0x08, 0x01, 0x05, 0x01, 0x06, 0x34, 0x41, 0x01, 0x06, 0xFF, 0x00, 0x01, 0x08, 0x01, 0x02, 0x01, 0x06, "input[10]", "input[11]", 0x01, 0x01, 0x01, 0x06, 0x55, 0x0A, 0x01, 0x00, 0x00, 0x07, 0x00, 0x00, 0x01, 0x06, 0x6A, 0x36, 0x01, 0x06, 0x00, 0x08, 0x01, 0x05, 0x01, 0x06, 0x2D, 0x01, 0x01, 0x06, 0xFF, 0x00, 0x01, 0x08, 0x01, 0x02, 0x01, 0x06, "input[13]", "input[12]", 0x01, 0x01, 0x01, 0x06, 0x58, 0x1E, 0x01, 0x00, 0x00, 0x07, 0x00, 0x00, 0x01, 0x06, 0x75, 0x1B, 0x01, 0x06, 0x00, 0x08, 0x01, 0x05, 0x01, 0x06, 0x3B, 0x17, 0x01, 0x06, 0xFF, 0x00, 0x01, 0x08, 0x01, 0x02, 0x01, 0x06, "input[15]", "input[14]", 0x01, 0x01, 0x01, 0x06, 0x0F, 0x19, 0x01, 0x00, 0x00, 0x07, 0x00, 0x00, 0x01, 0x06, 0x77, 0x7C, 0x01, 0x06, 0x00, 0x08, 0x01, 0x05, 0x01, 0x06, 0x45, 0x30, 0x01, 0x06, 0xFF, 0x00, 0x01, 0x08, 0x01, 0x02, 0x01, 0x06, "input[17]", "input[16]", 0x01, 0x01, 0x01, 0x06, 0x76, 0x03, 0x01, 0x00, 0x00, 0x07, 0x00, 0x00, 0x01, 0x06, 0x0F, 0x37, 0x01, 0x06, 0x00, 0x08, 0x01, 0x04, 0x01, 0x06, 0x3B, 0x23, 0x01, 0x06, 0x00, 0xFF, 0x01, 0x08, 0x01, 0x02, 0x01, 0x06, "input[19]", "input[18]", 0x01, 0x01, 0x01, 0x06, 0x4A, 0x12, 0x01, 0x00, 0x00, 0x07]
vip = 0 
print(len(bytecode))
while(vip<len(bytecode)):
    if(bytecode[vip+1] == 0x06):
        if(isinstance(bytecode[vip+2],str) or isinstance(bytecode[vip+3],str)):
            print(f"push {bytecode[vip+2],bytecode[vip+3]}")
            vip += 4
            continue
        print(f"push {hex((bytecode[vip+2]<<8) +bytecode[vip+3])}")
        vip +=4
        continue
    if(bytecode[vip+1] == 0x5):
        print("shr")
        vip +=2
        continue
    if(bytecode[vip+1] == 0x8):
        print("and")
        vip +=2
        continue
    if(bytecode[vip+1]==0x2):
        print("add")
        vip +=2
        continue
    if(bytecode[vip+1]==0x01):
        print("xor")
        vip +=2
        continue
    if(bytecode[vip+1]==0):
        print("cmp")
        vip+=2
        continue
    if(bytecode[vip+1]==0x07):
        print("pop")
        vip+=2
        continue
    if(bytecode[vip+1]==0x03):
        print("sub")
        vip+=2
        continue
    if(bytecode[vip+1]==0x4):
        print("shl")
        vip+=2
        continue
#push 0x1
#push 0xc0d
#push 0x8
#shr
#push 0x2238
#push 0xff00
#and
#add
#push ('input[1]', 'input[0]')
#xor
#push 0x694e
#cmp
#pop
#cmp
#push 0xc0d
#push 0x2d41
#add
#push 0x8
#shr
#push 0x2238
#push 0x5522
#xor
#push 0xff00
#and
#add
#push ('input[3]', 'input[2]')
#xor
#push 0x326a
#cmp
#pop
#cmp
#push 0x4930
#push 0x8
#shr
#push 0x3e5e
#push 0xff00
#and
#add
#push ('input[5]', 'input[4]')
#xor
#push 0x450a
#cmp
#pop
#cmp
#push 0x3b20
#push 0x8
#shr
#push 0x6b2d
#push 0xff00
#and
#add
#push ('input[7]', 'input[6]')
#xor
#push 0x5b78
#cmp
#pop
#cmp
#push 0x2b79
#push 0x8
#shr
#push 0x7041
#push 0xff00
#and
#add
#push ('input[8]', 'input[9]')
#xor
#push 0x3745
#cmp
#pop
#cmp
#push 0x7879
#push 0x8
#shr
#push 0x3441
#push 0xff00
#and
#add
#push ('input[10]', 'input[11]')
#xor
#push 0x550a
#cmp
#pop
#cmp
#push 0x6a36
#push 0x8
#shr
#push 0x2d01
#push 0xff00
#and
#add
#push ('input[13]', 'input[12]')
#xor
#push 0x581e
#cmp
#pop
#cmp
#push 0x751b
#push 0x8
#shr
#push 0x3b17
#push 0xff00
#and
#add
#push ('input[15]', 'input[14]')
#xor
#push 0xf19
#cmp
#pop
#cmp
#push 0x777c
#push 0x8
#shr
#push 0x4530
#push 0xff00
#and
#add
#push ('input[17]', 'input[16]')
#xor
#push 0x7603
#cmp
#pop
#cmp
#push 0xf37
#push 0x8
#shl
#push 0x3b23
#push 0xff
#and
#add
#push ('input[19]', 'input[18]')
#xor
#push 0x4a12
#cmp
#pop