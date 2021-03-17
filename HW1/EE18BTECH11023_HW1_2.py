import numpy as np
#input txt file for question2 and question 3
ques_txt2 = 'caaaacaacaaccbaaaaacccaaaaccabaaccaaccaaeccccacccacaccaaaaaaaaaadcacacaaacaaccaaaccacaaaaaaacccabeacaacacaacaccaacacaccacaaaaccccaaaaacacaaccacabccccccacaaacaaccaaaaccaaccacaacdaccaaaaaaaccaaaacacdaacbccaaccaaaccacaacccabaaacccaaaaaacaccaaaaaaaaaaccaaaccaacaaaccccccacaaccaaaacaaacaaaaaacaaacdcacccaaccaacaaaaaaaaaaadaacaabacaacccacaacaaaaaacacddaaaaaacccbacdcccacaaacccacabaabaaacaacaaccaacacacaacaaaaacccaadaacaccaacaacaadaacaacaacaccaaaaacaaaaaacabaccacaaaaaaaccccaaacaaaaaaaccaccccacacccacaccaaaccadccccaccaccaaaaaaaaacccacecaaadaaaaaabcacaacbccacccaaaccaaccccbccacacccaaacacaceaacaabaaaacacacacaaaaaaacccaaaccdbaacccacacaaacaccacaaccaaaadabcacacaaccaaaaccaaaceaaaadaaccaaacabacaacaacacacaaacaaaccaacacccaaaaaaccecaaadccaaacaaaaaacaccaaaaccaacacacaccaaacaaacdecacacccaacaccacaccaacaccacaaaadcdcaaccaeccaaaacaacaaacacaacdaaaccccaaaaccaaacccacccbaacaadaccaacbccaeaaaaacaacabccccaaccaaaacaaaaaaaaaaaaaaaacaaaaaacaaacaccaccaaaccaaadaaadcaaaaaabaccaecaacaaacaaacadcacaacccaaccaaaaaaacccaaacaccccaccaaa'

L = ['a','b','c','d','e']   
c2a=0;c2b=0;c2c=0;c2d=0;c2e=0  
C2 = [c2a,c2b,c2c,c2d,c2e]

for j in range(5):
    for i in ques_txt2:
        if i == L[j]:
            C2[j] = C2[j] + 1
P2=[C2[0]/1000,C2[1]/1000,C2[2]/1000,C2[3]/1000,C2[4]/1000]   #percentage of codewords for txt2
for i in range(5):
    print("percentage of", L[i], "occurrence in txt3 is ",P2[i])
En2 = 0
for j in range(len(P2)):
    En2 = En2 - P2[j]*np.log2(P2[j]) 
print("Entropy of input_txt2:",En2)
print('')

########################################################################################
#Compression of input_txt2 by shannon code 
S_C2=""
for i in range(len(ques_txt2)):
    if (ques_txt2[i]== "a"):
        S_C2 += '0'
    elif (ques_txt2[i] == "b"):
        S_C2 += '111101'
    elif (ques_txt2[i] == "c"):
        S_C2 += '10'
    elif (ques_txt2[i] == "d"):
        S_C2 += '111100'
    elif (ques_txt2[i] == "e"):
        S_C2 += '1111110'
print("Compression of input_txt2 by shannon code : ",S_C2)  

print(len(S_C2))
#Verfiy2 = 0
#B2 = [1,6,2,6,5]
#for i in range(5):
#    Verfiy2 += P2[i]*B2[i]
#print(Verfiy2)
print('')
######################################################################################
#Compression of input_txt2 by huffman code 
H_C2=""
for i in range(len(ques_txt2)):
    if (ques_txt2[i]== "a"):
        H_C2 += '0'
    elif (ques_txt2[i] == "b"):
        H_C2 += '1110'
    elif (ques_txt2[i] == "c"):
        H_C2 += '10'
    elif (ques_txt2[i] == "d"):
        H_C2 += '110'
    elif (ques_txt2[i] == "e"):
        H_C2 += '1111'
print("Compression of input_txt2 by Huffman code : ",H_C2)

print(len(H_C2))
#VerfiyH_C2 = 0
#BH_C2= [1,4,2,3,4,]
#for i in range(5):
#    VerfiyH_C2 += P2[i]*BH_C2[i]
#print(VerfiyH_C2)
print('')

###########################################################################################
#Compression of input_txt2 by shannon-fano code 
SF_C2=""
for i in range(len(ques_txt2)):
    if (ques_txt2[i]== "a"):
        SF_C2 += '00'
    elif (ques_txt2[i] == "b"):
        SF_C2 += '1111101'
    elif (ques_txt2[i] == "c"):
        SF_C2 += '110'
    elif (ques_txt2[i] == "d"):
        SF_C2 += '1111100'
    elif (ques_txt2[i] == "e"):
        SF_C2 += '11111110'
print("Compression of input_txt2 by shannon-fano code : ",SF_C2) 


print(len(SF_C2))
#VerfiySF_2 = 0
#BSF_C2 = [2,7,3,7,8]
#for i in range(5):
#    VerfiySF_2 += P2[i]*BSF_C2[i]
#print(VerfiySF_2)
print('')
#Decompression of Input_txt2 by shannon codewords 
Sk2=0
Sn2=len(S_C2)    #length of Compressed input
D_SC2 =""        #Decompressed string 
while(Sk2 < len(S_C2)):
    if(S_C2[Sk2:Sk2+1]=='0'):
        D_SC2 +='a'
        Sk2 = Sk2+1
    elif(Sk2+len('111101') <= Sn2 and S_C2[Sk2:Sk2+len('111101')]=='111101'):
        D_SC2 +='b'
        Sk2 = Sk2+len('111101')
    elif(Sk2+len('10') <= Sn2 and S_C2[Sk2:Sk2+len('10')]=='10'):
        D_SC2 +='c'
        Sk2 = Sk2+len('10')
    elif(Sk2+len('111100') <= Sn2 and S_C2[Sk2:Sk2+len('111100')]=='111100'):
        D_SC2 +='d'
        Sk2 = Sk2+len('111100')
    elif(Sk2+len('1111110') <= Sn2 and S_C2[Sk2:Sk2+len('1111110')]=='1111110'):
        D_SC2 +='e'
        Sk2 = Sk2+len('1111110')        
if(ques_txt2==D_SC2):
    print("Decompression of Compressed input_tex2 is Successful by using Shannon codewards")
    print('Length of Decompression output:',len(D_SC2))
    print('Decompression of Compressed input_tex2 with shannon codewords : ',D_SC2) 
elif(ques_txt2!=D_SC2):
    print('Decompression of input_tex2 Incomplete')
 
print('')

#Decompression of Input_txt2 by Huffman codewords 
Hk2=0
Hn2=len(H_C2)    #length of Compressed input
D_HC2 =""        #Decompressed string 
while(Hk2 < len(H_C2)):
    if(H_C2[Hk2:Hk2+1]=='0'):
        D_HC2 +='a'
        Hk2 = Hk2+1
    elif(Hk2+len('1110') <= Hn2 and H_C2[Hk2:Hk2+len('1110')]=='1110'):
        D_HC2 +='b'
        Hk2 = Hk2+len('1110')
    elif(Hk2+len('10') <= Hn2 and H_C2[Hk2:Hk2+len('10')]=='10'):
        D_HC2 +='c'
        Hk2 = Hk2+len('10')
    elif(Hk2+len('110') <= Hn2 and H_C2[Hk2:Hk2+len('110')]=='110'):
        D_HC2 +='d'
        Hk2 = Hk2+len('110')
    elif(Hk2+len('1111') <= Hn2 and H_C2[Hk2:Hk2+len('1111')]=='1111'):
        D_HC2 +='e'
        Hk2 = Hk2+len('1111')       
if(ques_txt2==D_HC2):
    print("Decompression of Compressed input_tex2 is Successful by using Huffman codewards")
    print('Length of Decompression output:',len(D_HC2))
    print('Decompression of Compressed input_tex2 with Huffman codewards: ',D_HC2)  
elif(ques_txt2!=D_HC2):
    print('Decompression of input_tex2 Incomplete')

print('')


#Decompression of Input_txt2 by shannon-fano codewords 
SFk2=0
SFn2=len(SF_C2)    #length of Compressed input
D_SFC2 =""        #Decompressed string 
while(SFk2 < len(SF_C2)):
    if(SF_C2[SFk2:SFk2+2]=='00'):
        D_SFC2 +='a'
        SFk2 = SFk2+2
    elif(SFk2+len('1111101') <= SFn2 and SF_C2[SFk2:SFk2+len('1111101')]=='1111101'):
        D_SFC2 +='b'
        SFk2 = SFk2+len('1111101')
    elif(SFk2+len('110') <= SFn2 and SF_C2[SFk2:SFk2+len('110')]=='110'):
        D_SFC2 +='c'
        SFk2 = SFk2+len('110')
    elif(SFk2+len('1111100') <= SFn2 and SF_C2[SFk2:SFk2+len('1111100')]=='1111100'):
        D_SFC2 +='d'
        SFk2 = SFk2+len('1111100')
    elif(SFk2+len('11111110') <= SFn2 and SF_C2[SFk2:SFk2+len('11111110')]=='11111110'):
        D_SFC2 +='e'
        SFk2 = SFk2+len('11111110')        
if(ques_txt2==D_SFC2):
    print("Decompression of Compressed input_tex2 is Successful by using Shannon-fano codewards")
    print('Length of Decompression output:',len(D_SFC2))
    print('Decompression of Compressed input_tex2 with shannon-fano codewords : ',D_SFC2) 
elif(ques_txt2!=D_SFC2):
    print('Decompression of input_tex2 Incomplete')
 
print('')