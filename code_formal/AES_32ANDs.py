def AES_Sbox():
    Sbox = []
    for X in range(256):
        x = [(X>>i)&1 for i in range(8)]; y = [0]*8; g = [0]*100; r = [0]*200; t = [0]*1000
        T = [0]*1000; M = [0]*1000; L = [0]*100

        ################### Here is your code !! ###################
        DJ_master = [0]*115
        DJ_master[0] = x[4] ^ x[2]
        DJ_master[1] = x[7] ^ x[1]
        DJ_master[2] = x[7] ^ x[4]
        DJ_master[3] = x[7] ^ x[2]
        DJ_master[4] = x[6] ^ x[5]
        DJ_master[5] = DJ_master[4] ^ x[0]
        DJ_master[6] = DJ_master[5] ^ x[4]
        DJ_master[7] = DJ_master[1] ^ DJ_master[0]
        DJ_master[8] = DJ_master[5] ^ x[7]
        DJ_master[9] = DJ_master[5] ^ x[1]
        DJ_master[10] = DJ_master[9] ^ DJ_master[3]
        DJ_master[11] = x[3] ^ DJ_master[7]
        DJ_master[12] = DJ_master[11] ^ x[2]
        DJ_master[13] = DJ_master[11] ^ x[6]
        DJ_master[14] = DJ_master[12] ^ x[0]
        DJ_master[15] = DJ_master[12] ^ DJ_master[4]
        DJ_master[16] = DJ_master[13] ^ DJ_master[2]
        DJ_master[17] = x[0] ^ DJ_master[16]
        DJ_master[18] = DJ_master[15] ^ DJ_master[16]
        DJ_master[19] = DJ_master[15] ^ DJ_master[3]
        DJ_master[20] = DJ_master[4] ^ DJ_master[16]
        DJ_master[21] = DJ_master[1] ^ DJ_master[20]
        DJ_master[22] = x[7] ^ DJ_master[20]
        DJ_master[23] = DJ_master[7] & DJ_master[12]
        DJ_master[24] = DJ_master[10] & DJ_master[14]
        DJ_master[25] = DJ_master[24] ^ DJ_master[23]
        DJ_master[26] = DJ_master[6] & x[0]
        DJ_master[27] = DJ_master[26] ^ DJ_master[23]
        DJ_master[28] = DJ_master[1] & DJ_master[20]
        DJ_master[29] = DJ_master[9] & DJ_master[5]
        DJ_master[30] = DJ_master[29] ^ DJ_master[28]
        DJ_master[31] = DJ_master[8] & DJ_master[17]
        DJ_master[32] = DJ_master[31] ^ DJ_master[28]
        DJ_master[33] = DJ_master[2] & DJ_master[16]
        DJ_master[34] = DJ_master[0] & DJ_master[18]
        DJ_master[35] = DJ_master[34] ^ DJ_master[33]
        DJ_master[36] = DJ_master[3] & DJ_master[15]
        DJ_master[37] = DJ_master[36] ^ DJ_master[33]
        DJ_master[38] = DJ_master[25] ^ DJ_master[35]
        DJ_master[39] = DJ_master[27] ^ DJ_master[37]
        DJ_master[40] = DJ_master[30] ^ DJ_master[35]
        DJ_master[41] = DJ_master[32] ^ DJ_master[37]
        DJ_master[42] = DJ_master[38] ^ DJ_master[13]
        DJ_master[43] = DJ_master[39] ^ DJ_master[19]
        DJ_master[44] = DJ_master[40] ^ DJ_master[21]
        DJ_master[45] = DJ_master[41] ^ DJ_master[22]
        DJ_master[46] = DJ_master[42] ^ DJ_master[43]
        DJ_master[47] = DJ_master[42] & DJ_master[44]
        DJ_master[48] = DJ_master[45] ^ DJ_master[47]
        DJ_master[49] = DJ_master[46] & DJ_master[48]
        DJ_master[50] = DJ_master[49] ^ DJ_master[43]
        DJ_master[51] = DJ_master[44] ^ DJ_master[45]
        DJ_master[52] = DJ_master[43] ^ DJ_master[47]
        DJ_master[53] = DJ_master[52] & DJ_master[51]
        DJ_master[54] = DJ_master[53] ^ DJ_master[45]
        DJ_master[55] = DJ_master[44] ^ DJ_master[54]
        DJ_master[56] = DJ_master[48] ^ DJ_master[54]
        DJ_master[57] = DJ_master[45] & DJ_master[56]
        DJ_master[58] = DJ_master[57] ^ DJ_master[55]
        DJ_master[59] = DJ_master[48] ^ DJ_master[57]
        DJ_master[60] = DJ_master[50] & DJ_master[59]
        DJ_master[61] = DJ_master[46] ^ DJ_master[60]
        DJ_master[62] = DJ_master[61] ^ DJ_master[58]
        DJ_master[63] = DJ_master[50] ^ DJ_master[54]
        DJ_master[64] = DJ_master[50] ^ DJ_master[61]
        DJ_master[65] = DJ_master[54] ^ DJ_master[58]
        DJ_master[66] = DJ_master[63] ^ DJ_master[62]
        DJ_master[67] = DJ_master[65] & DJ_master[12]
        DJ_master[68] = DJ_master[58] & DJ_master[14]
        DJ_master[69] = DJ_master[54] & x[0]
        DJ_master[70] = DJ_master[64] & DJ_master[20]
        DJ_master[71] = DJ_master[61] & DJ_master[5]
        DJ_master[72] = DJ_master[50] & DJ_master[17]
        DJ_master[73] = DJ_master[63] & DJ_master[16]
        DJ_master[74] = DJ_master[66] & DJ_master[18]
        DJ_master[75] = DJ_master[62] & DJ_master[15]
        DJ_master[76] = DJ_master[65] & DJ_master[7]
        DJ_master[77] = DJ_master[58] & DJ_master[10]
        DJ_master[78] = DJ_master[54] & DJ_master[6]
        DJ_master[79] = DJ_master[64] & DJ_master[1]
        DJ_master[80] = DJ_master[61] & DJ_master[9]
        DJ_master[81] = DJ_master[50] & DJ_master[8]
        DJ_master[82] = DJ_master[63] & DJ_master[2]
        DJ_master[83] = DJ_master[66] & DJ_master[0]
        DJ_master[84] = DJ_master[62] & DJ_master[3]
        DJ_master[85] = DJ_master[82] ^ DJ_master[83]
        DJ_master[86] = DJ_master[77] ^ DJ_master[78]
        DJ_master[87] = DJ_master[72] ^ DJ_master[80]
        DJ_master[88] = DJ_master[76] ^ DJ_master[77]
        DJ_master[89] = DJ_master[69] ^ DJ_master[79]
        DJ_master[90] = DJ_master[69] ^ DJ_master[72]
        DJ_master[91] = DJ_master[74] ^ DJ_master[75]
        DJ_master[92] = DJ_master[67] ^ DJ_master[70]
        DJ_master[93] = DJ_master[73] ^ DJ_master[74]
        DJ_master[94] = DJ_master[83] ^ DJ_master[84]
        DJ_master[95] = DJ_master[79] ^ DJ_master[87]
        DJ_master[96] = DJ_master[89] ^ DJ_master[92]
        DJ_master[97] = DJ_master[71] ^ DJ_master[85]
        DJ_master[98] = DJ_master[70] ^ DJ_master[93]
        DJ_master[99] = DJ_master[85] ^ DJ_master[96]
        DJ_master[100] = DJ_master[81] ^ DJ_master[96]
        DJ_master[101] = DJ_master[91] ^ DJ_master[97]
        DJ_master[102] = DJ_master[88] ^ DJ_master[97]
        DJ_master[103] = DJ_master[71] ^ DJ_master[98]
        DJ_master[104] = DJ_master[100] ^ DJ_master[101]
        DJ_master[105] = DJ_master[68] ^ DJ_master[102]
        DJ_master[107] = DJ_master[98] ^ DJ_master[102]
        y[7] = DJ_master[107]
        DJ_master[108] = DJ_master[95] ^ DJ_master[101] ^ 1
        y[1] = DJ_master[108]
        DJ_master[109] = DJ_master[87] ^ DJ_master[99] ^ 1
        y[0] = DJ_master[109]
        DJ_master[106] = DJ_master[103] ^ DJ_master[104]
        DJ_master[110] = DJ_master[92] ^ DJ_master[105]
        y[4] = DJ_master[110]
        DJ_master[111] = DJ_master[90] ^ DJ_master[105]
        y[3] = DJ_master[111]
        DJ_master[112] = DJ_master[86] ^ DJ_master[104]
        y[2] = DJ_master[112]
        DJ_master[113] = DJ_master[103] ^ DJ_master[110] ^ 1
        y[6] = DJ_master[113]
        DJ_master[114] = DJ_master[94] ^ DJ_master[106] ^ 1
        y[5] = DJ_master[114]
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
    