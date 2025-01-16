def AES_Sbox():
    Sbox = []
    for X in range(256):
        x = [(X>>i)&1 for i in range(8)]; y = [0]*8; g = [0]*100; r = [0]*200; t = [0]*1000
        T = [0]*1000; M = [0]*1000; L = [0]*100

        ################### Here is your code !! ###################
        t[0] = x[4] ^ x[2]
        t[1] = x[7] ^ x[1]
        t[2] = x[7] ^ x[4]
        t[3] = x[7] ^ x[2]
        t[4] = x[6] ^ x[5]
        t[5] = t[4] ^ x[0]
        t[6] = t[5] ^ x[4]
        t[7] = t[1] ^ t[0]
        t[8] = t[5] ^ x[7]
        t[9] = t[5] ^ x[1]
        t[10] = t[9] ^ t[3]
        t[11] = x[3] ^ t[7]
        t[12] = t[11] ^ x[2]
        t[13] = t[11] ^ x[6]
        t[14] = t[12] ^ x[0]
        t[15] = t[12] ^ t[4]
        t[16] = t[13] ^ t[2]
        t[17] = x[0] ^ t[16]
        t[18] = t[15] ^ t[16]
        t[19] = t[15] ^ t[3]
        t[20] = t[4] ^ t[16]
        t[21] = t[1] ^ t[20]
        t[22] = x[7] ^ t[20]
        g[0] = t[7] & t[12]
        g[1] = t[10] & t[14]
        t[23] = g[1] ^ g[0]
        g[2] = t[6] & x[0]
        t[24] = g[2] ^ g[0]
        g[3] = t[1] & t[20]
        g[4] = t[9] & t[5]
        t[25] = g[4] ^ g[3]
        g[5] = t[8] & t[17]
        t[26] = g[5] ^ g[3]
        g[6] = t[2] & t[16]
        g[7] = t[0] & t[18]
        t[27] = g[7] ^ g[6]
        g[8] = t[3] & t[15]
        t[28] = g[8] ^ g[6]
        t[29] = t[23] ^ t[27]
        t[30] = t[24] ^ t[28]
        t[31] = t[25] ^ t[27]
        t[32] = t[26] ^ t[28]
        t[33] = t[29] ^ t[13]
        t[34] = t[30] ^ t[19]
        t[35] = t[31] ^ t[21]
        t[36] = t[32] ^ t[22]
        g[9] = t[33] & t[35]
        t[37] = t[33] ^ t[34]
        t[38] = t[36] ^ g[9]
        g[10] = t[37] & t[38]
        t[39] = t[35] ^ t[36]
        t[40] = t[34] ^ g[9]
        g[11] = t[39] & t[40]
        g[12] = t[34] & t[36]
        t[41] = t[36] ^ g[12]
        g[13] = t[33] & t[41]
        t[42] = t[34] ^ g[12]
        g[14] = t[35] & t[42]
        t[43] = g[9] ^ t[39]
        t[44] = g[14] ^ t[43]
        t[45] = t[36] ^ g[11]
        t[46] = t[34] ^ t[33]
        t[47] = g[9] ^ t[46]
        t[48] = g[13] ^ t[47]
        t[49] = t[34] ^ g[10]
        t[50] = t[48] ^ t[44]
        t[51] = t[49] ^ t[45]
        t[52] = t[49] ^ t[48]
        t[53] = t[45] ^ t[44]
        t[54] = t[51] ^ t[50]
        g[15] = t[53] & t[12]
        g[16] = t[44] & t[14]
        g[17] = t[45] & x[0]
        g[18] = t[52] & t[20]
        g[19] = t[48] & t[5]
        g[20] = t[49] & t[17]
        g[21] = t[51] & t[16]
        g[22] = t[54] & t[18]
        g[23] = t[50] & t[15]
        g[24] = t[53] & t[7]
        g[25] = t[44] & t[10]
        g[26] = t[45] & t[6]
        g[27] = t[52] & t[1]
        g[28] = t[48] & t[9]
        g[29] = t[49] & t[8]
        g[30] = t[51] & t[2]
        g[31] = t[54] & t[0]
        g[32] = t[50] & t[3]
        t[55] = g[30] ^ g[31]
        t[56] = g[25] ^ g[26]
        t[57] = g[20] ^ g[28]
        t[58] = g[24] ^ g[25]
        t[59] = g[17] ^ g[27]
        t[60] = g[17] ^ g[20]
        t[61] = g[22] ^ g[23]
        t[62] = g[15] ^ g[18]
        t[63] = g[21] ^ g[22]
        t[64] = g[31] ^ g[32]
        t[65] = g[27] ^ t[57]
        t[66] = t[59] ^ t[62]
        t[67] = g[19] ^ t[55]
        t[68] = g[18] ^ t[63]
        t[69] = t[55] ^ t[66]
        t[70] = g[29] ^ t[66]
        t[71] = t[61] ^ t[67]
        t[72] = t[58] ^ t[67]
        t[73] = g[19] ^ t[68]
        t[74] = t[70] ^ t[71]
        t[75] = g[16] ^ t[72]
        y[7] = t[68] ^ t[72]
        t[76] = 1 ^ t[65]
        y[1] = t[71] ^ t[76]
        t[77] = 1 ^ t[57]
        y[0] = t[69] ^ t[77]
        t[78] = t[73] ^ t[74]
        y[4] = t[62] ^ t[75]
        y[3] = t[60] ^ t[75]
        y[2] = t[56] ^ t[74]
        t[79] = 1 ^ t[73]
        y[6] = y[4] ^ t[79]
        t[80] = 1 ^ t[64]
        y[5] = t[78] ^ t[80]
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
    