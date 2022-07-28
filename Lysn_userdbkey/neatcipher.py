import hashlib


def mix1(android_id):
    sha = hashlib.sha256(android_id.encode()).hexdigest()
    strr = '754s8UlVo8[4X(2<D:y%!lf,Zl0obZoN'
    strrlen = len(strr)
    shalen = len(sha)
    x10 = 0 #어차피 값이 0이니
    x11 = 0 #어차피 값이 0이니
    x13 = shalen #한 글자씩 보는건데 아스키값이므로 0보다 무조건 크니 -1씩 하기로 함
    x9 = strrlen 
    x8 = 0
    w14 = '' #임시로 글자 저장 함
    W12 = 0x55555556
    tmp = True
    x25 = shalen + strrlen
    x20 =''
    while tmp == True:
        if (x8-3*(((W12*x8)>>32)+((W12*x8)>>63))) != 2:
            if x13>x10: #cmp x13, x10 다음 bcs에서 분기 하려면 x13<x10이어야 하는데 조건 만족하여 분기하면 안됨
                w14 = sha[0:1]
                sha = sha[1:] #주소 바뀐 것 표현
                x13=x13-1
            elif x9>=x11:
                w14 = strr[0:1]
                strr = strr[1:]
                #print(x9,x8, strr)
                x9=x9-1
        elif (x8-3*(((W12*x8)>>32)+((W12*x8)>>63))) == 2:
            if x9>=x11: #cmp x9, x11에서 bcc에서 분기 하려면 x9>x11이어야 함
                w14 = strr[0:1]
                strr = strr[1:]     
                #print(x9,x8, strr)
                x9=x9-1
            elif x13>=x10:
                w14 = sha[0:1]
                sha = sha[1:] #주소 바뀐 것 표현
                x13=x13-1
        x8=x8+1
        x20 = x20 + w14
        if x8 == x25:
            return x20
        
   
def mix2(result1):
    sha = hashlib.sha256(result1.encode()).hexdigest()
    strr = "xJ*v*:x|68ZZ'w!}TjI%!lf<w3tsVU\\v"
    strrlen = len(strr)
    shalen = len(sha)
    x10 = 0 #어차피 값이 0이니
    x11 = 0 #어차피 값이 0이니
    x12 = shalen #한 글자씩 보는건데 아스키값이므로 0보다 무조건 크니 -1씩 하기로 함
    x9 = strrlen 
    x8 = 0
    w14 = '' #임시로 글자 저장 함
    tmp = True
    x25 = shalen + strrlen
    x20 = ''
    while tmp == True:
        if x8<0:
            x8=x8+1
        w13=x8
        w13= x8-(x8&0xfffffffe)
        if w13 == 0:
            if x12>=x11:
                w13 = sha[0:1]
                sha = sha[1:] #주소 바뀐 것 표현
                x9=x9-1
            elif x9 >= x10:
                w13 = strr[0:1]
                strr = strr[1:]     
                x12=x12-1      
        elif w13 == 1:
            if x9>=x10:
                w13 = strr[0:1]
                strr = strr[1:]     
                x12=x12-1
            elif x12>=x11:
                w13 = sha[0:1]
                sha = sha[1:]
                x9=x9-1
        x20 = x20 + w13
        x8=x8+1
        if x25 == x8:
            return x20
        
def mix3(result2):
    sha = hashlib.sha256(result2.encode()).hexdigest()
    strr = "_;F*hJ2_7e4s8UlV<Ey5!L6\\$V*R|`Nx~x[zXH2|6(zO'7!f68Zj'w!]FqL9NB`z"
    strrlen = len(strr)
    shalen = len(sha)
    x10 = 0 #어차피 값이 0이니
    x11 = 0 #어차피 값이 0이니
    x13 = shalen #한 글자씩 보는건데 아스키값이므로 0보다 무조건 크니 -1씩 하기로 함
    x9 = strrlen 
    x8 = 0
    w14 = '' #임시로 글자 저장 함
    W12 = 0x55555556
    tmp = True
    x25 = shalen + strrlen
    x20 = ''
    while tmp == True:
        if (x8-3*(((W12*x8)>>32)+((W12*x8)>>63))) != 2:
            if x13>x10: #x13>=x10이 맞지만 그렇게 하면 null값이 호출 됨. null이랑 null이랑 비교 했을 때 같은 값으로 봐야 하나? 
                w14 = sha[0:1]
                sha = sha[1:] #주소 바뀐 것 표현
                print(x8,sha)
                x13=x13-1
            elif x9>=x11:
                w14 = strr[0:1]
                strr = strr[1:]
                #print(x9,x8, strr)
                x9=x9-1
        elif (x8-3*(((W12*x8)>>32)+((W12*x8)>>63))) == 2:
            if x9>=x11: #cmp x9, x11에서 bcc에서 분기 하려면 x9>x11이어야 함
                w14 = strr[0:1]
                strr = strr[1:]     
                #print(x9,x8, strr)
                x9=x9-1
            elif x13>=x10:
                w14 = sha[0:1]
                sha = sha[1:] #주소 바뀐 것 표현
                x13=x13-1
        x20 = x20 + w14
        x8=x8+1
        if x8 == x25:
            return x20
# null null일 때 CF 1로 봐야 올바르게 넘어감. 이게 맞나??
  