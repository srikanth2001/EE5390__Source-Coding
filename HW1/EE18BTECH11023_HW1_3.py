import numpy as np
#input txt file for question2 and question 3
ques_txt3 = 'ebcbbabebbeaecabbbaabbcbbabbbbbecbbacbecccbeecbcccbbbbccbcaaaabbeaccaaaabcbccabcaebdcacaabebcacbbbbecbbbbcaacaaaaaacccecaccbcacaabbcabccabcbcacdbabccacbcaaacccbbcbebabeeabaacbabbebbaacabaacdbcababcebbbabeccbaabaaabebccccceabbacbaacbcecaeecccbeecbebcaaeeaaabceaebbecacebbeabaabbbabcbacbacaecbcccbecaebcbbccaebeeeceeeeabcbcbbcbcbbbccabbcbbacbcaecbdabaacccadcecbeecbeacaabcebcbcbaccaeaababaeebccbabccaaecbbcbcaaabaacccabececbbacacebcbcbcebcbbacabbbaacbaaecabcaabacbbecacbeaebbccccbebecbccabecacabcbcbacbeacbbbacbbbccbaebcaabeeaeeaaabaaabbaaaabaabececbaceaebacaabeaccbaeebbaaebabbcbdcacecabddacbbcccaaccccababacacbbeecbeabacbccbcbbcccbcccbeeaacceebcecbbccaeaacaabbcbabbdacbeeceabababcaaaaccacbabbbacccccbacbcbbbcebabcaaabebacbaeabcababaeabcaebceaaeacabedaacbacaebaeaaaaccaacbbaacbcbaaaeccdcbccaccaecbbacbcaaecabebeaebabababacbebccbdcaecabbaabaabcceaeabbaceacebcdbabcbbabebbcebbcaabbccbbbcbbbcbbdecaceaaaecababbbbcbaaccecebbcecaecaeebaccaabacccbeacbecbebecaabacbebeacbbacbaebcaebeebcabcccbaccecbaccbaccccb'

L = ['a','b','c','d','e']  
c3a=0;c3b=0;c3c=0;c3d=0;c3e=0
C3 = [c3a,c3b,c3c,c3d,c3e]

for j in range(5):
    for i in ques_txt3:
        if i == L[j]:
            C3[j] = C3[j] + 1
P3=[C3[0]/1000,C3[1]/1000,C3[2]/1000,C3[3]/1000,C3[4]/1000]   #percentage of codewords for txt3
for i in range(5):
    print("percentage of", L[i], "occurrence in txt3 is ",P3[i])
En3 = 0
for j in range(len(P3)):
    En3 = En3 - P3[j]*np.log2(P3[j]) 
print("Entropy of input_txt3:",En3)
print('')


#Compression of input_txt3 by shannon code 
S_C3=""
for i in range(len(ques_txt3)):
    if (ques_txt3[i]== "a"):
        S_C3 += '10'
    elif (ques_txt3[i] == "b"):
        S_C3 += '00'
    elif (ques_txt3[i] == "c"):
        S_C3 += '01'
    elif (ques_txt3[i] == "d"):
        S_C3 += '1111110'
    elif (ques_txt3[i] == "e"):
        S_C3 += '110'
print("Compression of input_txt3 by shannon code : ",S_C3) 

print(len(S_C3)) 
#Verfiy3 = 0
#B3 = [2,2,2,7,3]
#for i in range(5):
#    Verfiy3 += P3[i]*B3[i]
#print(Verfiy3)
print('')

#Compression of input_txt3 by huffman code 
H_C3=""
for i in range(len(ques_txt3)):
    if (ques_txt3[i]== "a"):
        H_C3 += '110'
    elif (ques_txt3[i] == "b"):
        H_C3 += '0'
    elif (ques_txt3[i] == "c"):
        H_C3 += '10'
    elif (ques_txt3[i] == "d"):
        H_C3 += '1111'
    elif (ques_txt3[i] == "e"):
        H_C3 += '1110'
print("Compression of input_txt3 by Huffman code : ",H_C3)


print(len(H_C3))
#VerfiyH_C3 = 0
#BH_C3= [3,1,2,4,4]
#for i in range(5):
#    VerfiyH_C3 += P3[i]*BH_C3[i]
#print(VerfiyH_C3)
print('')

#Compression of input_txt3 by shannon-fano code 
SF_C3=""
for i in range(len(ques_txt3)):
    if (ques_txt3[i]== "a"):
        SF_C3 += '110'
    elif (ques_txt3[i] == "b"):
        SF_C3 += '000'
    elif (ques_txt3[i] == "c"):
        SF_C3 += '011'
    elif (ques_txt3[i] == "d"):
        SF_C3 += '11111110'
    elif (ques_txt3[i] == "e"):
        SF_C3 += '1110'
print("Compression of input_txt3 by shannon-fano code : ",SF_C3)

print(len(SF_C3)) 
#VerfiySF_3 = 0
#BSF_C3 = [3,3,3,8,4]
#for i in range(5):
#    VerfiySF_3 += P3[i]*BSF_C3[i]
#print(VerfiySF_3)
print('')

#Decompression of Input_txt3 by shannon codewords 
Sk3=0
Sn3=len(S_C3)    #length of Compressed input
D_SC3 =""        #Decompressed string 
while(Sk3 < len(S_C3)):
    if(S_C3[Sk3:Sk3+len('10')]=='10'):
        D_SC3 +='a'
        Sk3 = Sk3+len('10')
    elif(Sk3+len('00') <= Sn3 and S_C3[Sk3:Sk3+len('00')]=='00'):
        D_SC3 +='b'
        Sk3 = Sk3+len('00')
    elif(Sk3+len('01') <= Sn3 and S_C3[Sk3:Sk3+len('01')]=='01'):
        D_SC3 +='c'
        Sk3 = Sk3+len('01')
    elif(Sk3+len('1111110') <= Sn3 and S_C3[Sk3:Sk3+len('1111110')]=='1111110'):
        D_SC3 +='d'
        Sk3 = Sk3+len('1111110')
    elif(Sk3+len('110') <= Sn3 and S_C3[Sk3:Sk3+len('110')]=='110'):
        D_SC3 +='e'
        Sk3 = Sk3+len('110')    
if(ques_txt3==D_SC3):
    print("Decompression of Compressed input_tex3 is Successful by using Shannon codewards")
    print('Length of Decompression output:',len(D_SC3))
    print('Decompression of Compressed input_tex3 with shannon codewords : ',D_SC3) 
elif(ques_txt3!=D_SC3):
    print('Decompression of input_tex2 Incomplete')
 
print('')


#Decompression of Input_txt3 by Huffman codewords 
Hk3=0
Hn3=len(H_C3)    #length of Compressed input
D_HC3 =""        #Decompressed string 
while(Hk3 < len(H_C3)):
    if(H_C3[Hk3:Hk3+len('110')]=='110'):
        D_HC3 +='a'
        Hk3 = Hk3+len('110')
    elif(Hk3+len('0') <= Hn3 and H_C3[Hk3:Hk3+len('0')]=='0'):
        D_HC3 +='b'
        Hk3 = Hk3+len('0')
    elif(Hk3+len('10') <= Hn3 and H_C3[Hk3:Hk3+len('10')]=='10'):
        D_HC3 +='c'
        Hk3 = Hk3+len('10')
    elif(Hk3+len('1111') <= Hn3 and H_C3[Hk3:Hk3+len('1111')]=='1111'):
        D_HC3 +='d'
        Hk3 = Hk3+len('1111')
    elif(Hk3+len('1110') <= Hn3 and H_C3[Hk3:Hk3+len('1110')]=='1110'):
        D_HC3 +='e'
        Hk3 = Hk3+len('1110') 
if(ques_txt3==D_HC3):
    print("Decompression of Compressed input_tex3 is Successful by using Huffman codewards")
    print('Length of Decompression output:',len(D_HC3))
    print('Decompression of Compressed input_tex3 with Huffman codewards: ',D_HC3)  
elif(ques_txt3!=D_HC3):
    print('Decompression of input_tex2 Incomplete')

print('')    

#Decompression of Input_txt2 by shannon-fano codewords 
SFk3=0
SFn3=len(SF_C3)    #length of Compressed input
D_SFC3 =""        #Decompressed string 
while(SFk3 < len(SF_C3)):
    if(SF_C3[SFk3:SFk3+len('110')]=='110'):
        D_SFC3 +='a'
        SFk3 = SFk3+len('110')
    elif(SFk3+len('000') <= SFn3 and SF_C3[SFk3:SFk3+len('000')]=='000'):
        D_SFC3 +='b'
        SFk3 = SFk3+len('000')
    elif(SFk3+len('011') <= SFn3 and SF_C3[SFk3:SFk3+len('011')]=='011'):
        D_SFC3 +='c'
        SFk3 = SFk3+len('011')
    elif(SFk3+len('11111110') <= SFn3 and SF_C3[SFk3:SFk3+len('11111110')]=='11111110'):
        D_SFC3 +='d'
        SFk3 = SFk3+len('11111110')
    elif(SFk3+len('1110') <= SFn3 and SF_C3[SFk3:SFk3+len('1110')]=='1110'):
        D_SFC3 +='e'
        SFk3 = SFk3+len('1110')        
if(ques_txt3==D_SFC3):
    print("Decompression of Compressed input_tex3 is Successful by using Shannon-fano codewards")
    print('Length of Decompression output:',len(D_SFC3))
    print('Decompression of Compressed input_tex3 with shannon-fano codewords : ',D_SFC3)  
elif(ques_txt3!=D_SFC3):
    print('Decompression of input_tex2 Incomplete')
