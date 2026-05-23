def check_snt(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def xuly_tich(n):
    s = str(n)
    return len(s), max(s)

def dem_chan(n):
    count = 0
    for chu_so in str(n):
        if int(chu_so) % 2 == 0:
            count += 1
    return count