def Ascon_Sbox():
    Sbox = []
    for X in range(32):
        x = [(X>>i)&1 for i in range(5)][::-1]; y = [0]*5; g = [0]*100; r = [0]*200; t = [0]*1000

        ################### Here is your code !! ###################
        x[0] ^= x[4]; 
        x[4] ^= x[3]; 
        x[2] ^= x[1]; 

        t[0]  = x[0];  
        t[1]  = x[1];  
        t[2]  = x[2];  
        t[3]  = x[3];  
        t[4]  = x[4]; 

        t[0] = 1^ t[0]; 
        t[1] = 1^ t[1]; 
        t[2] = 1^ t[2]; 
        t[3] = 1^ t[3]; 
        t[4] = 1^ t[4]; 

        t[0] &= x[1]; 
        t[1] &= x[2]; 
        t[2] &= x[3]; 
        t[3] &= x[4]; 
        t[4] &= x[0];  

        x[0] ^= t[1]; 
        x[1] ^= t[2]; 
        x[2] ^= t[3]; 
        x[3] ^= t[4]; 
        x[4] ^= t[0]; 

        x[1] ^= x[0]; 
        x[0] ^= x[4]; 
        x[3] ^= x[2]; 
        x[2] = 1 ^ x[2]; 

        y[0]  = x[0];  
        y[1]  = x[1];  
        y[2]  = x[2];  
        y[3]  = x[3];  
        y[4]  = x[4]; 
        ################### Here is your code !! ###################

        Y = (y[0]<<4)|(y[1]<<3)|(y[2]<<2)|(y[3]<<1)|(y[4]<<0)
        
        Sbox.append(Y)
    return Sbox
if __name__ == "__main__":
    Sbox = Ascon_Sbox()
    
    Ascon_original = [4,0xb,0x1f,0x14,0x1a,0x15,0x9,0x2,0x1b,0x5,0x8,0x12,0x1d,0x3,0x6,0x1c,0x1e,0x13,0x7,0xe,0x0,0xd,0x11,0x18,0x10,0xc,0x1,0x19,0x16,0xa,0xf,0x17]
    if tuple(Sbox) != tuple(Ascon_original):
        print('Wrong!!')
        for i in range(len(Sbox)):
            if Sbox[i] != Ascon_original[i]:
                print(f'{i:2X}th value : {Sbox[i]:5b}({Sbox[i]:2X}) {Ascon_original[i]:5b}({Ascon_original[i]:2X})')
    else:
        print('Right!!')
    