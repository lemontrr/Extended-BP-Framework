def SNOW_g7():
    Sbox = []
    for X in range(256):
        x = [(X>>i)&1 for i in range(8)]
        xJJ = [0]*8; y = [0]*8; g = [0]*3
        x1 = [0]*8; x2 = [0]*8; x5 = [0]*8; x7 = [0]*8; xJJ = [0]*8
        x_ = [0]*4; y_ = [0]*4; t0 = [0]*4; t1 = [0]*4; t2 = [0]*4; t3 = [0]*4; d = [0]*9; e = [0]*7; c = [0]*4
        a0 = [0]*4; a1 = [0]*4; a2 = [0]*4; g = [0]*3; a0_5 = [0]*4; a1_5 = [0]*4; a2_5 = [0]*4; ABCDEFA = [0]*4; a1_2 = [0]*4; a1_4 = [0]*4; d = [0]*9; q= [0]*4; e = [0]*4; MK21 = [0]*4

        ################### Here is your code !! ###################
        a2[0] = x[4] ^ x[0]
        a2[1] = x[5] ^ x[1]
        a2[2] = x[6] ^ x[2]
        a2[3] = x[7] ^ x[3]
        g[0] = x[0] & x[1]
        DJ_Phd_0_ = x[1] ^ x[2]
        DJ_Phd_1_ = x[0] ^ x[1] ^ x[3]
        g[1] = DJ_Phd_0_ & DJ_Phd_1_
        DJ_Phd_2_ = x[0] ^ x[1] ^ x[2]
        g[2] = DJ_Phd_2_ & x[3]
        a0_5[0] = x[0] ^ x[1] ^ x[3] ^ g[0] ^ g[2]
        a0_5[1] = x[2] ^ g[1] ^ g[2]
        a0_5[2] = x[0] ^ x[0]
        DJ_Phd_49_ = x[4] & x[5]
        DJ_Phd_3_ = x[5] ^ x[6]
        DJ_Phd_4_ = x[4] ^ x[5] ^ x[7]
        DJ_Phd_50_ = DJ_Phd_3_ & DJ_Phd_4_
        DJ_Phd_5_ = x[4] ^ x[5] ^ x[6]
        DJ_Phd_51_ = DJ_Phd_5_ & x[7]
        a1_5[0] = x[4] ^ x[5] ^ x[7] ^ DJ_Phd_49_ ^ DJ_Phd_51_
        a1_5[1] = x[6] ^ DJ_Phd_50_ ^ DJ_Phd_51_
        DJ_Phd_52_ = a2[0] & a2[1]
        DJ_Phd_6_ = a2[1] ^ a2[2]
        DJ_Phd_7_ = a2[0] ^ a2[1] ^ a2[3]
        DJ_Phd_53_ = DJ_Phd_6_ & DJ_Phd_7_
        DJ_Phd_8_ = a2[0] ^ a2[1] ^ a2[2]
        DJ_Phd_54_ = DJ_Phd_8_ & a2[3]
        a2_5[0] = a2[0] ^ a2[1] ^ a2[3] ^ DJ_Phd_52_ ^ DJ_Phd_54_
        a2_5[1] = a2[2] ^ DJ_Phd_53_ ^ DJ_Phd_54_
        a1_2[0] = x[4] ^ x[6] ^ x[7]
        a1_2[2] = x[5] ^ x[7]
        a1_2[3] = x[6] ^ x[7]
        d[0] = x[0] & DJ_Phd_4_
        DJ_Phd_9_ = x[0] ^ x[1]
        d[1] = DJ_Phd_9_ & DJ_Phd_5_
        d[2] = x[1] & a1_2[3]
        DJ_Phd_11_ = x[0] ^ x[2]
        DJ_Phd_12_ = DJ_Phd_4_ ^ x[6]
        d[3] = DJ_Phd_11_ & DJ_Phd_12_
        DJ_Phd_13_ = x[0] ^ x[1] ^ x[2] ^ x[3]
        DJ_Phd_14_ = DJ_Phd_4_ ^ a1_2[3] ^ x[6] ^ DJ_Phd_3_
        d[4] = DJ_Phd_13_ & DJ_Phd_14_
        DJ_Phd_15_ = x[1] ^ x[3]
        d[5] = DJ_Phd_15_ & a1_2[2]
        d[6] = x[2] & x[6]
        DJ_Phd_17_ = x[2] ^ x[3]
        d[7] = DJ_Phd_17_ & x[5]
        d[8] = x[3] & DJ_Phd_3_
        ABCDEFA[0] = d[0] ^ d[2] ^ d[5] ^ d[8] ^ d[7]
        ABCDEFA[1] = d[0] ^ d[1] ^ d[2] ^ d[6] ^ d[7]
        ABCDEFA[2] = d[0] ^ d[2] ^ d[3] ^ d[6] ^ d[8]
        ABCDEFA[3] = d[0] ^ d[1] ^ d[3] ^ d[4] ^ d[6]
        q[1] = a1_5[0] ^ a1_5[1]
        MK21[1] = ABCDEFA[0] ^ ABCDEFA[3]
        MK21[2] = ABCDEFA[0] ^ ABCDEFA[1]
        x5[0] = a0_5[0] ^ a1_5[1] ^ ABCDEFA[2]
        x5[1] = a0_5[1] ^ a1_5[0] ^ MK21[1]
        x5[2] = a0_5[2] ^ a1_5[1] ^ MK21[2]
        x5[3] = a0_5[1] ^ a1_5[1] ^ ABCDEFA[1]
        x5[4] = a2_5[0] ^ a0_5[2] ^ a0_5[0]
        x5[5] = a2_5[1] ^ q[1] ^ a0_5[1]
        x5[7] = a2_5[1] ^ a1_5[1] ^ a0_5[1]
        x2[0] = x[0] ^ x[2] ^ x[3] ^ x[6] ^ x[7]
        x2[1] = x[3] ^ x[4] ^ x[6] ^ x[7]
        x2[2] = x[1] ^ x[3] ^ x[7]
        x2[3] = x[2] ^ x[3] ^ x[5] ^ x[6]
        x_[0] = a1_2[0] ^ x2[0]
        x_[1] = x[7] ^ x2[1]
        x_[2] = a1_2[2] ^ x2[2]
        x_[3] = a1_2[3] ^ x2[3]
        y_[0] = x5[4] ^ x5[0]
        y_[1] = x5[5] ^ x5[1]
        y_[2] = q[1] ^ x5[2]
        y_[3] = x5[7] ^ x5[3]
        DJ_Phd_55_ = a1_2[0] & x5[4]
        DJ_Phd_56_ = DJ_Phd_14_ & ABCDEFA[2]
        DJ_Phd_57_ = x[7] & x5[5]
        DJ_Phd_22_ = x5[4] ^ q[1]
        DJ_Phd_58_ = DJ_Phd_5_ & DJ_Phd_22_
        DJ_Phd_23_ = a1_2[0] ^ x[7] ^ a1_2[2] ^ a1_2[3]
        DJ_Phd_24_ = x5[4] ^ x5[5] ^ q[1] ^ x5[7]
        DJ_Phd_59_ = DJ_Phd_23_ & DJ_Phd_24_
        DJ_Phd_60_ = x[6] & a1_5[0]
        DJ_Phd_61_ = a1_2[2] & q[1]
        DJ_Phd_28_ = q[1] ^ x5[7]
        DJ_Phd_62_ = DJ_Phd_3_ & DJ_Phd_28_
        DJ_Phd_63_ = a1_2[3] & x5[7]
        t2[0] = DJ_Phd_55_ ^ DJ_Phd_57_ ^ DJ_Phd_60_ ^ DJ_Phd_63_ ^ DJ_Phd_62_
        t2[1] = DJ_Phd_55_ ^ DJ_Phd_56_ ^ DJ_Phd_57_ ^ DJ_Phd_61_ ^ DJ_Phd_62_
        t2[2] = DJ_Phd_55_ ^ DJ_Phd_57_ ^ DJ_Phd_58_ ^ DJ_Phd_61_ ^ DJ_Phd_63_
        t2[3] = DJ_Phd_55_ ^ DJ_Phd_56_ ^ DJ_Phd_58_ ^ DJ_Phd_59_ ^ DJ_Phd_61_
        DJ_Phd_64_ = x_[0] & y_[0]
        DJ_Phd_29_ = x_[0] ^ x_[1]
        DJ_Phd_30_ = y_[0] ^ y_[1]
        DJ_Phd_65_ = DJ_Phd_29_ & DJ_Phd_30_
        DJ_Phd_66_ = x_[1] & y_[1]
        DJ_Phd_31_ = x_[0] ^ x_[2]
        DJ_Phd_32_ = y_[0] ^ y_[2]
        DJ_Phd_67_ = DJ_Phd_31_ & DJ_Phd_32_
        DJ_Phd_33_ = x_[0] ^ x_[1] ^ x_[2] ^ x_[3]
        DJ_Phd_34_ = y_[0] ^ y_[1] ^ y_[2] ^ y_[3]
        DJ_Phd_68_ = DJ_Phd_33_ & DJ_Phd_34_
        DJ_Phd_35_ = x_[1] ^ x_[3]
        DJ_Phd_36_ = y_[1] ^ y_[3]
        DJ_Phd_69_ = DJ_Phd_35_ & DJ_Phd_36_
        DJ_Phd_70_ = x_[2] & y_[2]
        DJ_Phd_37_ = x_[2] ^ x_[3]
        DJ_Phd_38_ = y_[2] ^ y_[3]
        DJ_Phd_71_ = DJ_Phd_37_ & DJ_Phd_38_
        DJ_Phd_72_ = x_[3] & y_[3]
        t1[0] = DJ_Phd_64_ ^ DJ_Phd_66_ ^ DJ_Phd_69_ ^ DJ_Phd_72_ ^ DJ_Phd_71_
        t1[1] = DJ_Phd_64_ ^ DJ_Phd_65_ ^ DJ_Phd_66_ ^ DJ_Phd_70_ ^ DJ_Phd_71_
        t1[2] = DJ_Phd_64_ ^ DJ_Phd_66_ ^ DJ_Phd_67_ ^ DJ_Phd_70_ ^ DJ_Phd_72_
        t1[3] = DJ_Phd_64_ ^ DJ_Phd_65_ ^ DJ_Phd_67_ ^ DJ_Phd_68_ ^ DJ_Phd_70_
        DJ_Phd_73_ = x2[0] & x5[0]
        DJ_Phd_39_ = x2[0] ^ x2[1]
        DJ_Phd_40_ = x5[0] ^ x5[1]
        DJ_Phd_74_ = DJ_Phd_39_ & DJ_Phd_40_
        DJ_Phd_75_ = x2[1] & x5[1]
        DJ_Phd_41_ = x2[0] ^ x2[2]
        DJ_Phd_42_ = x5[0] ^ x5[2]
        DJ_Phd_76_ = DJ_Phd_41_ & DJ_Phd_42_
        DJ_Phd_43_ = x2[0] ^ x2[1] ^ x2[2] ^ x2[3]
        DJ_Phd_44_ = x5[0] ^ x5[1] ^ x5[2] ^ x5[3]
        DJ_Phd_77_ = DJ_Phd_43_ & DJ_Phd_44_
        DJ_Phd_45_ = x2[1] ^ x2[3]
        DJ_Phd_46_ = x5[1] ^ x5[3]
        DJ_Phd_78_ = DJ_Phd_45_ & DJ_Phd_46_
        DJ_Phd_79_ = x2[2] & x5[2]
        DJ_Phd_47_ = x2[2] ^ x2[3]
        DJ_Phd_48_ = x5[2] ^ x5[3]
        DJ_Phd_80_ = DJ_Phd_47_ & DJ_Phd_48_
        DJ_Phd_81_ = x2[3] & x5[3]
        t0[0] = DJ_Phd_73_ ^ DJ_Phd_75_ ^ DJ_Phd_78_ ^ DJ_Phd_81_ ^ DJ_Phd_80_
        t0[1] = DJ_Phd_73_ ^ DJ_Phd_74_ ^ DJ_Phd_75_ ^ DJ_Phd_79_ ^ DJ_Phd_80_
        t0[2] = DJ_Phd_73_ ^ DJ_Phd_75_ ^ DJ_Phd_76_ ^ DJ_Phd_79_ ^ DJ_Phd_81_
        t0[3] = DJ_Phd_73_ ^ DJ_Phd_74_ ^ DJ_Phd_76_ ^ DJ_Phd_77_ ^ DJ_Phd_79_
        t3[3] = t2[2] ^ t2[3]
        x7[0] = t2[3] ^ t0[0]
        x7[1] = t2[0] ^ t0[1]
        x7[2] = t2[1] ^ t0[2]
        x7[3] = t3[3] ^ t0[3]
        x7[4] = t1[0] ^ t0[0]
        x7[5] = t1[1] ^ t0[1]
        x7[6] = t1[2] ^ t0[2]
        x7[7] = t1[3] ^ t0[3]
        xJJ[0] = x7[0] ^ x5[0] ^ x[0]
        xJJ[1] = x7[1] ^ x5[1] ^ x[1]
        xJJ[2] = x7[2] ^ x5[2] ^ x[2]
        xJJ[3] = x7[3] ^ x5[3] ^ x[3]
        xJJ[4] = x7[4] ^ x5[4] ^ x[4]
        xJJ[5] = x7[5] ^ x5[5] ^ x[5]
        xJJ[6] = x7[6] ^ q[1] ^ x[6]
        xJJ[7] = x7[7] ^ x5[7] ^ x[7]
        y[1] = xJJ[1] ^ xJJ[4]
        y[2] = xJJ[1] ^ xJJ[2] ^ xJJ[5]
        y[3] = xJJ[3] ^ xJJ[5] ^ xJJ[6]
        y[4] = xJJ[2] ^ xJJ[3] ^ xJJ[7]
        y[5] = xJJ[3] ^ xJJ[6] ^ xJJ[7]
        y[6] = xJJ[3] ^ xJJ[7]
        y[0] = xJJ[0]
        y[7] = xJJ[7]
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
    