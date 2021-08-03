
def to_hex(dec):
    s = ""
    while (dec > 0):
        
        ostatak = dec % 16
        dec//=16
        if (ostatak == 10):
            s+='A'
        elif (ostatak == 11):
            s+='B'
        elif (ostatak == 12):
            s+='C'
        elif (ostatak == 13):
            s+='D'
        elif (ostatak == 14):
            s+='E'
        elif (ostatak == 15):
            s+='F'
        else:
            s+=str(ostatak)
    return s
        
def hex_color(red,green,blue):
    s1 = "#" + to_hex(red) + to_hex(green) + to_hex(blue)
    

    return s1
    
    

      
    