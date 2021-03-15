 
while True:
    I_1,mileage = input().split(" ")
    I_h,I_m,I_sf = I_1.split(":")
    h= int(I_h)
    m= int(I_m)
    sf= float(I_sf)
    overmile = float(mileage) - 1052
    score = 410
    #if(overmile > 0):
    #    score += (overmile// 237 + 1)*80

    #深夜の走行は距離が1.25倍として扱う
    print(h,m,sf)
