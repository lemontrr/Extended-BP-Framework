def SNOW_g7():
    Sbox = []
    for X in range(256):
        x = [(X>>i)&1 for i in range(8)]
        xJJ = [0]*8; y = [0]*8; g = [0]*3
        x1 = [0]*8; x2 = [0]*8; x5 = [0]*8; x7 = [0]*8; xJJ = [0]*8
        x_ = [0]*4; y_ = [0]*4; t0 = [0]*4; t1 = [0]*4; t2 = [0]*4; t3 = [0]*4; d = [0]*9; e = [0]*7; c = [0]*4
        a0 = [0]*4; a1 = [0]*4; a2 = [0]*4; g = [0]*3; a0_5 = [0]*4; a1_5 = [0]*4; a2_5 = [0]*4; ABCDEFA = [0]*4; a1_2 = [0]*4; a1_4 = [0]*4; d = [0]*9; q= [0]*4; e = [0]*4; MK21 = [0]*4

        ################### Here is your code !! ###################
        t = [0]*259; r = [0]*90
        r[0] = x[0]
        r[18] = x[0]
        r[17] = x[6]
        r[11] = x[7]
        r[40] = x[7]
        t[0] = x[2] ^ x[4]
        t[1] = x[3] ^ x[7]
        t[2] = x[6] ^ x[7]
        r[5] = t[2]
        r[34] = t[2]
        t[3] = x[5] ^ t[1]
        r[7] = t[3]
        r[33] = t[3]
        t[4] = x[2] ^ t[3]
        r[2] = t[4]
        t[5] = x[3] ^ t[2]
        r[8] = t[5]
        r[35] = t[5]
        r[50] = t[5]
        g[17] = r[34] & r[35]
        t[6] = x[6] ^ t[0]
        r[13] = t[6]
        t[7] = t[3] ^ t[6]
        r[1] = t[7]
        r[22] = t[7]
        g[0] = r[0] & r[1]
        t[8] = x[1] ^ t[7]
        r[6] = t[8]
        g[3] = r[6] & r[7]
        t[9] = x[5] ^ t[2]
        r[23] = t[9]
        r[52] = t[9]
        g[11] = r[22] & r[23]
        t[10] = x[0] ^ x[1]
        t[11] = x[3] ^ x[5]
        r[29] = t[11]
        r[48] = t[11]
        t[12] = t[0] ^ t[11]
        r[28] = t[12]
        g[14] = r[28] & r[29]
        t[13] = x[1] ^ x[7]
        t[14] = t[6] ^ t[13]
        r[9] = t[14]
        r[19] = t[14]
        t[15] = x[4] ^ x[5]
        g[4] = r[8] & r[9]
        t[16] = t[0] ^ t[13]
        t[17] = t[5] ^ t[10]
        t[18] = t[1] ^ t[10]
        g[9] = r[18] & r[19]
        t[19] = x[5] ^ t[16]
        r[25] = t[19]
        t[20] = t[14] ^ t[15]
        r[64] = t[20]
        t[21] = x[3] ^ t[6]
        t[22] = g[4] ^ t[16]
        t[23] = g[17] ^ t[17]
        t[24] = g[0] ^ g[3]
        t[25] = x[0] ^ t[12]
        r[3] = t[25]
        g[1] = r[2] & r[3]
        t[26] = x[4] ^ x[6]
        r[30] = t[26]
        t[27] = x[2] ^ t[13]
        r[82] = t[27]
        t[28] = t[17] ^ t[27]
        t[29] = t[4] ^ g[14]
        t[30] = t[6] ^ t[15]
        r[14] = t[30]
        t[31] = x[4] ^ t[18]
        r[16] = t[31]
        g[8] = r[16] & r[17]
        t[32] = g[17] ^ g[14]
        t[33] = g[11] ^ g[8]
        t[34] = x[0] ^ t[26]
        r[24] = t[34]
        g[12] = r[24] & r[25]
        t[35] = g[3] ^ g[14]
        t[36] = g[3] ^ t[27]
        t[37] = t[23] ^ g[12]
        t[38] = g[4] ^ g[9]
        t[39] = t[12] ^ t[34]
        r[26] = t[39]
        t[40] = x[3] ^ t[16]
        r[27] = t[40]
        r[38] = t[40]
        g[13] = r[26] & r[27]
        t[41] = t[19] ^ g[13]
        t[42] = t[32] ^ g[12]
        t[43] = x[5] ^ x[6]
        r[31] = t[43]
        r[46] = t[43]
        g[15] = r[30] & r[31]
        t[44] = g[11] ^ g[15]
        t[45] = g[17] ^ t[21]
        t[46] = t[18] ^ t[43]
        r[15] = t[46]
        g[7] = r[14] & r[15]
        t[47] = g[4] ^ t[19]
        t[48] = t[41] ^ t[42]
        t[49] = x[4] ^ x[7]
        r[32] = t[49]
        g[16] = r[32] & r[33]
        t[50] = t[42] ^ t[44]
        t[51] = g[17] ^ g[9]
        t[52] = g[1] ^ g[16]
        t[53] = t[26] ^ t[44]
        t[54] = t[1] ^ t[16]
        r[36] = t[54]
        t[55] = x[1] ^ t[6]
        r[44] = t[55]
        t[56] = g[3] ^ t[47]
        r[49] = t[56]
        g[24] = r[48] & r[49]
        t[57] = g[0] ^ t[45]
        t[58] = x[1] ^ t[39]
        r[54] = t[58]
        t[59] = x[0] ^ t[15]
        r[56] = t[59]
        t[60] = t[5] ^ t[16]
        r[58] = t[60]
        t[61] = x[4] ^ t[46]
        r[60] = t[61]
        t[62] = t[16] ^ t[18]
        r[62] = t[62]
        t[63] = x[2] ^ t[49]
        r[66] = t[63]
        t[64] = x[2] ^ t[11]
        r[68] = t[64]
        t[65] = t[1] ^ t[15]
        r[70] = t[65]
        t[66] = x[5] ^ t[34]
        r[72] = t[66]
        t[67] = t[4] ^ t[10]
        r[74] = t[67]
        t[68] = x[3] ^ t[14]
        r[76] = t[68]
        t[69] = t[7] ^ t[59]
        r[78] = t[69]
        t[70] = t[2] ^ t[18]
        r[80] = t[70]
        t[71] = x[2] ^ t[65]
        r[84] = t[71]
        t[72] = x[2] ^ t[9]
        r[86] = t[72]
        t[73] = x[3] ^ t[26]
        r[88] = t[73]
        t[74] = x[1] ^ x[5]
        t[75] = t[0] ^ t[74]
        r[10] = t[75]
        r[21] = t[75]
        r[42] = t[75]
        g[5] = r[10] & r[11]
        t[76] = t[35] ^ g[5]
        t[77] = g[7] ^ g[16]
        t[78] = g[11] ^ g[12]
        t[79] = t[14] ^ g[5]
        t[80] = g[3] ^ t[79]
        r[47] = t[80]
        g[23] = r[46] & r[47]
        t[81] = t[50] ^ t[51]
        t[82] = t[32] ^ t[81]
        r[39] = t[82]
        g[19] = r[38] & r[39]
        t[83] = t[38] ^ t[79]
        t[84] = t[20] ^ t[51]
        t[85] = g[15] ^ g[5]
        t[86] = t[48] ^ t[83]
        r[65] = t[86]
        g[32] = r[64] & r[65]
        t[87] = t[0] ^ t[43]
        t[88] = t[18] ^ t[87]
        r[12] = t[88]
        g[6] = r[12] & r[13]
        t[89] = t[33] ^ t[37]
        t[90] = x[0] ^ x[2]
        t[91] = t[3] ^ t[90]
        r[4] = t[91]
        g[2] = r[4] & r[5]
        t[92] = g[8] ^ g[2]
        t[93] = g[0] ^ t[92]
        t[94] = t[52] ^ t[80]
        t[95] = g[9] ^ t[53]
        t[96] = t[38] ^ t[78]
        t[97] = t[77] ^ t[92]
        t[98] = t[14] ^ g[6]
        t[99] = t[93] ^ t[98]
        r[37] = t[99]
        g[18] = r[36] & r[37]
        t[100] = t[32] ^ g[18]
        t[101] = g[23] ^ t[94]
        t[102] = t[85] ^ g[2]
        t[103] = t[56] ^ t[99]
        r[43] = t[103]
        g[21] = r[42] & r[43]
        t[104] = t[57] ^ t[102]
        t[105] = t[43] ^ t[97]
        t[106] = t[94] ^ t[105]
        r[51] = t[106]
        g[25] = r[50] & r[51]
        t[107] = t[36] ^ t[85]
        t[108] = g[13] ^ g[2]
        t[109] = t[52] ^ g[5]
        t[110] = g[3] ^ t[38]
        t[111] = t[48] ^ t[110]
        r[83] = t[111]
        g[41] = r[82] & r[83]
        t[112] = g[18] ^ g[41]
        t[113] = t[15] ^ t[90]
        t[114] = t[5] ^ t[113]
        r[20] = t[114]
        g[10] = r[20] & r[21]
        t[115] = g[9] ^ g[10]
        t[116] = t[32] ^ g[10]
        t[117] = t[44] ^ t[115]
        t[118] = g[24] ^ t[107]
        t[119] = t[4] ^ g[10]
        t[120] = g[4] ^ t[109]
        t[121] = t[97] ^ t[120]
        r[53] = t[121]
        g[26] = r[52] & r[53]
        t[122] = t[108] ^ t[119]
        t[123] = t[50] ^ t[122]
        t[124] = t[15] ^ g[8]
        t[125] = t[77] ^ t[124]
        t[126] = t[117] ^ t[125]
        r[71] = t[126]
        g[35] = r[70] & r[71]
        t[127] = t[86] ^ t[126]
        r[59] = t[127]
        g[29] = r[58] & r[59]
        t[128] = g[15] ^ t[116]
        t[129] = t[80] ^ t[128]
        r[67] = t[129]
        g[33] = r[66] & r[67]
        t[130] = t[126] ^ t[129]
        r[69] = t[130]
        g[34] = r[68] & r[69]
        t[131] = g[32] ^ g[35]
        t[132] = g[6] ^ t[116]
        t[133] = t[16] ^ t[110]
        t[134] = t[89] ^ t[132]
        t[135] = t[133] ^ t[134]
        r[61] = t[135]
        g[30] = r[60] & r[61]
        t[136] = t[92] ^ t[124]
        t[137] = t[117] ^ t[136]
        t[138] = t[120] ^ t[137]
        r[89] = t[138]
        g[44] = r[88] & r[89]
        t[139] = t[56] ^ t[118]
        t[140] = t[43] ^ t[56]
        t[141] = g[29] ^ t[131]
        t[142] = g[19] ^ g[21]
        t[143] = t[32] ^ t[102]
        t[144] = t[109] ^ t[143]
        t[145] = t[95] ^ t[144]
        r[87] = t[145]
        g[43] = r[86] & r[87]
        t[146] = g[44] ^ g[43]
        t[147] = g[29] ^ g[34]
        t[148] = t[43] ^ g[15]
        t[149] = g[5] ^ t[148]
        t[150] = g[0] ^ g[2]
        t[151] = g[4] ^ t[149]
        t[152] = t[116] ^ t[151]
        r[85] = t[152]
        g[42] = r[84] & r[85]
        t[153] = g[35] ^ g[33]
        t[154] = t[121] ^ g[33]
        t[155] = g[19] ^ g[25]
        t[156] = g[25] ^ g[43]
        t[157] = g[15] ^ t[151]
        t[158] = t[99] ^ t[157]
        r[45] = t[158]
        g[22] = r[44] & r[45]
        t[159] = t[142] ^ t[146]
        t[160] = t[69] ^ t[122]
        t[161] = g[14] ^ t[25]
        t[162] = t[150] ^ t[161]
        t[163] = t[78] ^ t[115]
        t[164] = t[162] ^ t[163]
        r[79] = t[164]
        g[39] = r[78] & r[79]
        t[165] = g[19] ^ g[26]
        t[166] = t[140] ^ g[39]
        t[167] = g[44] ^ t[139]
        t[168] = t[111] ^ t[164]
        r[81] = t[168]
        g[40] = r[80] & r[81]
        t[169] = t[2] ^ g[42]
        t[170] = t[25] ^ g[13]
        t[171] = t[33] ^ t[170]
        t[172] = t[132] ^ t[171]
        t[173] = t[76] ^ t[172]
        r[63] = t[173]
        g[31] = r[62] & r[63]
        t[174] = g[39] ^ g[40]
        t[175] = t[52] ^ g[10]
        t[176] = t[110] ^ t[175]
        t[177] = g[17] ^ t[18]
        t[178] = t[85] ^ t[177]
        t[179] = g[14] ^ t[39]
        t[180] = t[41] ^ t[179]
        t[181] = g[0] ^ t[180]
        t[182] = t[176] ^ t[181]
        r[75] = t[182]
        g[37] = r[74] & r[75]
        t[183] = t[123] ^ g[42]
        t[184] = g[39] ^ t[169]
        t[185] = g[30] ^ t[184]
        t[186] = g[43] ^ t[154]
        t[187] = t[41] ^ t[77]
        t[188] = g[6] ^ t[179]
        t[189] = t[115] ^ t[188]
        t[190] = t[187] ^ t[189]
        r[57] = t[190]
        g[28] = r[56] & r[57]
        t[191] = t[154] ^ g[31]
        t[192] = t[147] ^ t[186]
        t[193] = g[22] ^ t[184]
        t[194] = t[101] ^ t[183]
        t[195] = t[141] ^ t[146]
        t[196] = g[42] ^ t[166]
        t[197] = g[29] ^ t[153]
        t[198] = t[96] ^ t[104]
        t[199] = t[185] ^ t[191]
        t[200] = t[165] ^ t[193]
        t[201] = t[8] ^ t[99]
        t[202] = g[37] ^ t[194]
        t[203] = g[24] ^ t[198]
        t[204] = t[116] ^ g[42]
        t[205] = g[41] ^ t[201]
        t[206] = g[30] ^ g[44]
        t[207] = g[18] ^ g[39]
        t[208] = t[112] ^ g[22]
        t[209] = g[34] ^ t[205]
        t[210] = t[155] ^ t[167]
        t[211] = g[40] ^ g[37]
        t[212] = t[197] ^ t[206]
        t[213] = x[6] ^ g[28]
        t[214] = t[156] ^ t[202]
        t[215] = t[52] ^ t[97]
        t[216] = t[140] ^ t[215]
        r[41] = t[216]
        g[20] = r[40] & r[41]
        t[217] = g[8] ^ g[6]
        t[218] = t[178] ^ t[217]
        t[219] = t[96] ^ t[218]
        r[55] = t[219]
        g[27] = r[54] & r[55]
        t[220] = t[3] ^ t[80]
        t[221] = t[7] ^ t[52]
        t[222] = t[80] ^ t[221]
        t[223] = t[123] ^ t[222]
        r[77] = t[223]
        g[38] = r[76] & r[77]
        t[224] = g[42] ^ t[220]
        t[225] = g[17] ^ t[25]
        t[226] = t[149] ^ t[225]
        t[227] = t[150] ^ t[226]
        t[228] = t[96] ^ t[227]
        r[73] = t[228]
        g[36] = r[72] & r[73]
        t[229] = g[27] ^ g[36]
        t[230] = g[38] ^ t[229]
        t[231] = g[20] ^ g[38]
        t[232] = t[209] ^ t[230]
        t[233] = t[195] ^ t[232]
        y[4] = t[233]
        t[234] = t[196] ^ t[230]
        t[235] = t[212] ^ t[234]
        y[6] = t[235]
        t[236] = t[213] ^ t[229]
        t[237] = t[211] ^ t[236]
        t[238] = t[199] ^ t[237]
        y[7] = t[238]
        t[239] = t[204] ^ g[36]
        t[240] = t[207] ^ t[239]
        t[241] = t[231] ^ t[240]
        t[242] = t[210] ^ t[241]
        y[2] = t[242]
        t[243] = t[203] ^ g[36]
        t[244] = g[38] ^ t[243]
        t[245] = t[208] ^ t[244]
        t[246] = t[159] ^ t[245]
        y[0] = t[246]
        t[247] = t[138] ^ g[36]
        t[248] = g[20] ^ t[247]
        t[249] = t[211] ^ t[248]
        t[250] = t[200] ^ t[249]
        y[3] = t[250]
        t[251] = g[18] ^ g[36]
        t[252] = g[26] ^ t[251]
        t[253] = t[231] ^ t[252]
        t[254] = t[214] ^ t[253]
        y[1] = t[254]
        t[255] = g[28] ^ t[224]
        t[256] = g[37] ^ t[255]
        t[257] = t[230] ^ t[256]
        t[258] = t[192] ^ t[257]
        y[5] = t[258]
        ################### Here is your code !! ###################


        Y = (y[7]<<7)|(y[6]<<6)|(y[5]<<5)|(y[4]<<4)|(y[3]<<3)|(y[2]<<2)|(y[1]<<1)|(y[0]<<0)
        Sbox.append(Y)
    return Sbox

def mul_GF28(x,y):
    x_ = [0]*4; y_ = [0]*4; z = [0]*8; t0 = [0]*4; t1 = [0]*4; t2 = [0]*4; t3 = [0]*4; d = [0]*9; e = [0]*7; c = [0]*4
    x_[0] = x[4]^x[0]
    x_[1] = x[5]^x[1]
    x_[2] = x[6]^x[2]
    x_[3] = x[7]^x[3]
    y_[0] = y[4]^y[0]
    y_[1] = y[5]^y[1]
    y_[2] = y[6]^y[2]
    y_[3] = y[7]^y[3]

    d[0] = x[4]&y[4]
    d[1] = (x[4]^x[5])&(y[4]^y[5])
    d[2] = x[5]&y[5]
    d[3] = (x[4]^x[6])&(y[4]^y[6])
    d[4] = (x[4]^x[5]^x[6]^x[7])&(y[4]^y[5]^y[6]^y[7])
    d[5] = (x[5]^x[7])&(y[5]^y[7])
    d[6] = x[6]&y[6]
    d[7] = (x[6]^x[7])&(y[6]^y[7])
    d[8] = x[7]&y[7]

    # f = 9
    t2[0] = d[0]^d[2]^d[5]^d[8]^d[7]
    t2[1] = d[0]^d[1]^d[2]^d[6]^d[7]
    t2[2] = d[0]^d[2]^d[3]^d[6]^d[8]
    t2[3] = d[0]^d[1]^d[3]^d[4]^d[6]

    d[0] = x_[0]&y_[0]
    d[1] = (x_[0]^x_[1])&(y_[0]^y_[1])
    d[2] = x_[1]&y_[1]
    d[3] = (x_[0]^x_[2])&(y_[0]^y_[2])
    d[4] = (x_[0]^x_[1]^x_[2]^x_[3])&(y_[0]^y_[1]^y_[2]^y_[3])
    d[5] = (x_[1]^x_[3])&(y_[1]^y_[3])
    d[6] = x_[2]&y_[2]
    d[7] = (x_[2]^x_[3])&(y_[2]^y_[3])
    d[8] = x_[3]&y_[3]

    # f = 9
    t1[0] = d[0]^d[2]^d[5]^d[8]^d[7]
    t1[1] = d[0]^d[1]^d[2]^d[6]^d[7]
    t1[2] = d[0]^d[2]^d[3]^d[6]^d[8]
    t1[3] = d[0]^d[1]^d[3]^d[4]^d[6]

    d[0] = x[0]&y[0]
    d[1] = (x[0]^x[1])&(y[0]^y[1])
    d[2] = x[1]&y[1]
    d[3] = (x[0]^x[2])&(y[0]^y[2])
    d[4] = (x[0]^x[1]^x[2]^x[3])&(y[0]^y[1]^y[2]^y[3])
    d[5] = (x[1]^x[3])&(y[1]^y[3])
    d[6] = x[2]&y[2]
    d[7] = (x[2]^x[3])&(y[2]^y[3])
    d[8] = x[3]&y[3]

    # f = 9
    t0[0] = d[0]^d[2]^d[5]^d[8]^d[7]
    t0[1] = d[0]^d[1]^d[2]^d[6]^d[7]
    t0[2] = d[0]^d[2]^d[3]^d[6]^d[8]
    t0[3] = d[0]^d[1]^d[3]^d[4]^d[6]

    t3[0] = t2[3]
    t3[1] = t2[0]
    t3[2] = t2[1]
    t3[3] = t2[2] ^ t2[3]

    # g = 18
    z[0] = t3[0]^t0[0]
    z[1] = t3[1]^t0[1]
    z[2] = t3[2]^t0[2]
    z[3] = t3[3]^t0[3]
    z[4] = t1[0]^t0[0]
    z[5] = t1[1]^t0[1]
    z[6] = t1[2]^t0[2]
    z[7] = t1[3]^t0[3]
    ###
    return z


if __name__ == '__main__':

    Sbox = SNOW_g7()
    
    SNOW_g7_original = [0, 1, 162, 207, 39, 52, 106, 19, 221, 247, 117, 71, 115, 82, 143, 176, 216, 180, 107, 21, 6, 108, 131, 253, 209, 67, 214, 34, 48, 189, 186, 87, 23, 42, 122, 196, 250, 136, 5, 242, 138, 9, 204, 184, 201, 28, 166, 130, 123, 175, 63, 22, 139, 4, 132, 240, 27, 164, 202, 252, 243, 14, 210, 160, 89, 208, 185, 173, 58, 154, 213, 238, 96, 104, 145, 112, 30, 38, 91, 140, 46, 226, 144, 191, 187, 74, 211, 199, 119, 239, 102, 105, 73, 245, 53, 24, 231, 225, 244, 128, 255, 141, 158, 152, 90, 72, 121, 109, 120, 7, 146, 237, 230, 33, 147, 88, 236, 75, 50, 159, 18, 20, 233, 151, 148, 235, 127, 126, 182, 83, 156, 79, 98, 78, 194, 222, 10, 49, 114, 11, 65, 170, 8, 167, 77, 155, 179, 45, 183, 188, 26, 95, 234, 55, 248, 25, 57, 32, 195, 224, 241, 125, 86, 3, 110, 118, 62, 249, 251, 60, 47, 69, 220, 150, 68, 165, 254, 197, 181, 41, 171, 16, 206, 212, 198, 99, 64, 54, 157, 161, 142, 103, 59, 81, 40, 133, 200, 80, 177, 232, 113, 111, 43, 134, 137, 124, 2, 66, 36, 85, 172, 100, 246, 97, 205, 229, 193, 17, 190, 163, 174, 129, 217, 61, 37, 149, 135, 31, 44, 51, 153, 168, 29, 76, 215, 218, 56, 223, 94, 227, 12, 35, 13, 116, 192, 84, 15, 203, 178, 169, 101, 92, 228, 93, 70, 219]
    if tuple(Sbox) != tuple(SNOW_g7_original):
        print('Wrong!!')
        for i in range(len(Sbox)):
            if Sbox[i] != SNOW_g7_original[i]:
                print(f'{i:2X}th value : {Sbox[i]:8b}({Sbox[i]:2X}) {SNOW_g7_original[i]:8b}({SNOW_g7_original[i]:2X})')
    else:
        print('Right!!')
    