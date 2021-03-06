from unicodedata import decimal
import datahex
#파일 시그니쳐를 입력합니다
filesign={
    (0x89,0x50,0x4E,0x47,0x0D,0x0A,0x1A,0x0A):'png',
    (0xFF,0xD8,0xFF,0xE0,0x00,0x10,0x4A,0x46):'jfif',
    (0xD0,0xCF,0x11,0xE0,0xA1,0xB1,0x1A,0xE1):'hwp',
    (0x2E,0x20,0x20,0x20,0x20,0x20,0x20,0x20):'folder'
}
global fat
fat=datahex.data #이미지파일의 raw데이터를 저장하면 됩니다.

def BytesperSector():
    Bytesper=0x00
    Bytesper=Bytesper|fat[12]
    Bytesper= Bytesper<<8
    Bytesper=Bytesper|fat[11]
    Bytesper=Bytesper-1
    return Bytesper

#섹터별로 나눠서 fat32에 list로 저장합니다. 
#fat32[[섹터1], [섹터2]]
def divide_sector(Bytesper,fat):
    fat32=[]
    tmp=[]
    k=0
    count=0
    for i in range(len(fat)):
        if count!=Bytesper:
            count=count+1
            tmp.append(fat[i])
        elif count==Bytesper:
            fat32.append(tmp) 
            count=0
            tmp=[]
    return fat32

#만약 클러스터 첫번째가 파일시그니처 라면 000000 나올때 까지 검색 돌림
def find_filesign(fat32):
    for i in range(len(fat32)):
        tmp=[0]*8
        for k in range(8):
            tmp[k]=fat32[i][k]
        sign=tuple(tmp)
        if sign in filesign:
            print('파일시그니처는',filesign[sign],'위치는 섹터:',i)

Bytesper = BytesperSector()
fat32=divide_sector(Bytesper,fat)
print(find_filesign(fat32))
            
