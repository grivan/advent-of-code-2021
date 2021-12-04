INPUT = "day3/day3.in"

from operator import add

def b2i(binary):
    return int(binary, 2)

def find_diag_gamma_ep(input_file):
    
    gamma = ""
    ep = ""
    
    total = 0
    ones = None
    
    with open(input_file) as diags:
        for diag in diags:
            total += 1
            diag = [int(x) for x in list(diag.rstrip())]
            
            # print(diag)
            
            if not ones:
                ones = diag
            else:
                ones = list(map(add, ones, diag))
                # print(ones)
            
    # print(ones)
    for d in ones:
        if 2*d > total:
            gamma += '1'
            ep += '0'
        else:
            gamma += '0'
            ep += '1'
            
    return b2i(gamma), b2i(ep)

def crit_filter(criteria, index, diags):
    return [diag for diag in diags if diag[index] == criteria]
    
def bit_criteria(index, diags, oxy=True):
    ones = sum([diag[index] for diag in diags])
    zeroes = len(diags) - ones
    
    if ones >= zeroes:
        if oxy: return 1
        else: return 0
    else:
        if oxy: return 0
        else: return 1
        
    
def life_support(input_file):
    
    co2 = None
    oxy = None
    
    with open(input_file) as diags:
        diags = [[int(x) for x in list(diag.rstrip())] for diag in diags]
    
    co2 = diags
    index = 0
    while(len(co2) > 1):
        bit_crit = bit_criteria(index, co2, oxy=False)
        co2 = crit_filter(bit_crit, index, co2)
        index+=1
        
    oxy = diags
    index = 0
    while(len(oxy) > 1):
        bit_crit = bit_criteria(index, oxy, oxy=True)
        oxy = crit_filter(bit_crit, index, oxy)
        index+=1
    
    return b2i("".join([str(i) for i in co2[0]])), b2i("".join([str(i) for i in oxy[0]]))

# gamma, ep = find_diag_gamma_ep(INPUT)
# print(gamma * ep)

co2, oxy = life_support(INPUT)
print(co2 * oxy)