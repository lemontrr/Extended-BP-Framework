def AES_Sbox():
    Sbox = []
    for X in range(256):
        x = [(X>>i)&1 for i in range(8)]; y = [0]*8; g = [0]*100; r = [0]*200; t = [0]*1000
        T = [0]*1000; M = [0]*1000; L = [0]*100

        ################### Here is your code !! ###################
        # U table
        y14 = x[4] ^ x[2]   
        y13 = x[7] ^ x[1]   
        y9 = x[7] ^ x[4]
        y8 = x[7] ^ x[2]    
        t0 = x[6] ^ x[5]    
        y1 = t0 ^ x[0]
        y4 = y1 ^ x[4]    
        y12 = y13 ^ y14 
        y2 = y1 ^ x[7]
        y5 = y1 ^ x[1]    
        y3 = y5 ^ y8    
        t1 = x[3] ^ y12
        y15 = t1 ^ x[2]   
        y20 = t1 ^ x[6]   
        y6 = y15 ^ x[0]
        y10 = y15 ^ t0  
        y11 = y20 ^ y9  
        y7 = x[0] ^ y11
        y17 = y10 ^ y11 
        y19 = y10 ^ y8  
        y16 = t0 ^ y11
        y21 = y13 ^ y16 
        y18 = x[7] ^ y16
        
        # non-linear part
        t2 = y12 & y15  
        t3 = y3 & y6    
        t4 = t3 ^ t2
        t5 = y4 & x[0]    
        t6 = t5 ^ t2    
        t7 = y13 & y16
        t8 = y5 & y1    
        t9 = t8 ^ t7    
        t10 = y2 & y7
        t11 = t10 ^ t7  
        t12 = y9 & y11  
        t13 = y14 & y17
        t14 = t13 ^ t12 
        t15 = y8 & y10  
        t16 = t15 ^ t12
        t17 = t4 ^ t14  
        t18 = t6 ^ t16  
        t19 = t9 ^ t14
        t20 = t11 ^ t16 
        t21 = t17 ^ y20 
        t22 = t18 ^ y19
        t23 = t19 ^ y21 
        t24 = t20 ^ y18
        t25 = t21 ^ t22 
        t26 = t21 & t23 
        t27 = t24 ^ t26
        t28 = t25 & t27 
        t29 = t28 ^ t22 
        t30 = t23 ^ t24
        t31 = t22 ^ t26 
        t32 = t31 & t30 
        t33 = t32 ^ t24
        t34 = t23 ^ t33 
        t35 = t27 ^ t33 
        t36 = t24 & t35
        t37 = t36 ^ t34 
        t38 = t27 ^ t36 
        t39 = t29 & t38
        t40 = t25 ^ t39
        t41 = t40 ^ t37 
        t42 = t29 ^ t33 
        t43 = t29 ^ t40
        t44 = t33 ^ t37 
        t45 = t42 ^ t41 
        z0 = t44 & y15
        z1 = t37 & y6   
        z2 = t33 & x[0]   
        z3 = t43 & y16
        z4 = t40 & y1   
        z5 = t29 & y7   
        z6 = t42 & y11
        z7 = t45 & y17  
        z8 = t41 & y10  
        z9 = t44 & y12
        z10 = t37 & y3  
        z11 = t33 & y4  
        z12 = t43 & y13
        z13 = t40 & y5  
        z14 = t29 & y2  
        z15 = t42 & y9
        z16 = t45 & y14 
        z17 = t41 & y8

        # B table
        t46 = z15 ^ z16 
        t47 = z10 ^ z11    
        t48 = z5 ^ z13
        t49 = z9 ^ z10  
        t50 = z2 ^ z12     
        t51 = z2 ^ z5
        t52 = z7 ^ z8   
        t53 = z0 ^ z3      
        t54 = z6 ^ z7
        t55 = z16 ^ z17 
        t56 = z12 ^ t48    
        t57 = t50 ^ t53
        t58 = z4 ^ t46  
        t59 = z3 ^ t54     
        t60 = t46 ^ t57
        t61 = z14 ^ t57 
        t62 = t52 ^ t58    
        t63 = t49 ^ t58
        t64 = z4 ^ t59  
        t65 = t61 ^ t62    
        t66 = z1 ^ t63
        y[7] = t59 ^ t63  
        y[1] = t56 ^ t62 ^ 1 
        y[0] = t48 ^ t60 ^ 1
        t67 = t64 ^ t65 
        y[4] = t53 ^ t66     
        y[3] = t51 ^ t66
        y[2] = t47 ^ t65  
        y[6] = t64 ^ y[4] ^ 1  
        y[5] = t55 ^ t67 ^ 1
        
        ################### Here is your code !! ###################

        Y = (y[7]<<7)|(y[6]<<6)|(y[5]<<5)|(y[4]<<4)|(y[3]<<3)|(y[2]<<2)|(y[1]<<1)|(y[0]<<0)
        
        Sbox.append(Y)
    return Sbox
if __name__ == "__main__":
    Sbox = AES_Sbox()
    
    AES_original = [0x63,0x7c,0x77,0x7b,0xf2,0x6b,0x6f,0xc5,0x30,0x01,0x67,0x2b,0xfe,0xd7,0xab,0x76,
                    0xca,0x82,0xc9,0x7d,0xfa,0x59,0x47,0xf0,0xad,0xd4,0xa2,0xaf,0x9c,0xa4,0x72,0xc0,
                    0xb7,0xfd,0x93,0x26,0x36,0x3f,0xf7,0xcc,0x34,0xa5,0xe5,0xf1,0x71,0xd8,0x31,0x15,
                    0x04,0xc7,0x23,0xc3,0x18,0x96,0x05,0x9a,0x07,0x12,0x80,0xe2,0xeb,0x27,0xb2,0x75,
                    0x09,0x83,0x2c,0x1a,0x1b,0x6e,0x5a,0xa0,0x52,0x3b,0xd6,0xb3,0x29,0xe3,0x2f,0x84,
                    0x53,0xd1,0x00,0xed,0x20,0xfc,0xb1,0x5b,0x6a,0xcb,0xbe,0x39,0x4a,0x4c,0x58,0xcf,
                    0xd0,0xef,0xaa,0xfb,0x43,0x4d,0x33,0x85,0x45,0xf9,0x02,0x7f,0x50,0x3c,0x9f,0xa8,
                    0x51,0xa3,0x40,0x8f,0x92,0x9d,0x38,0xf5,0xbc,0xb6,0xda,0x21,0x10,0xff,0xf3,0xd2,
                    0xcd,0x0c,0x13,0xec,0x5f,0x97,0x44,0x17,0xc4,0xa7,0x7e,0x3d,0x64,0x5d,0x19,0x73,
                    0x60,0x81,0x4f,0xdc,0x22,0x2a,0x90,0x88,0x46,0xee,0xb8,0x14,0xde,0x5e,0x0b,0xdb,
                    0xe0,0x32,0x3a,0x0a,0x49,0x06,0x24,0x5c,0xc2,0xd3,0xac,0x62,0x91,0x95,0xe4,0x79,
                    0xe7,0xc8,0x37,0x6d,0x8d,0xd5,0x4e,0xa9,0x6c,0x56,0xf4,0xea,0x65,0x7a,0xae,0x08,
                    0xba,0x78,0x25,0x2e,0x1c,0xa6,0xb4,0xc6,0xe8,0xdd,0x74,0x1f,0x4b,0xbd,0x8b,0x8a,
                    0x70,0x3e,0xb5,0x66,0x48,0x03,0xf6,0x0e,0x61,0x35,0x57,0xb9,0x86,0xc1,0x1d,0x9e,
                    0xe1,0xf8,0x98,0x11,0x69,0xd9,0x8e,0x94,0x9b,0x1e,0x87,0xe9,0xce,0x55,0x28,0xdf,
                    0x8c,0xa1,0x89,0x0d,0xbf,0xe6,0x42,0x68,0x41,0x99,0x2d,0x0f,0xb0,0x54,0xbb,0x16]
    if tuple(Sbox) != tuple(AES_original):
        print('Wrong!!')
        for i in range(len(Sbox)):
            if Sbox[i] != AES_original[i]:
                print(f'{i:2X}th value : {Sbox[i]:8b}({Sbox[i]:2X}) {AES_original[i]:8b}({AES_original[i]:2X})')
    else:
        print('Right!!')
    