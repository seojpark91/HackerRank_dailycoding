def taumBday(b, w, bc, wc, z):
    return b*min(bc, wc+z) + w*min(wc,bc+z)

taumBday(10,10,1,1,1), taumBday(5,9,2,3,4), taumBday(3,6,9,1,1)