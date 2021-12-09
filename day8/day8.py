INPUT = "day8/day8.in"

with open(INPUT) as infile:
    
    uniques = {8: 7, 4: 4, 1: 2, 7: 3}
    
    grand_total_pt1 = 0
    grand_total_pt2 = 0
                
    for line in infile:
        isignal, out = line.rstrip().split('|')
        signal = ["".join(sorted(i)) for i in isignal.split()]
        output = ["".join(sorted(i)) for i in out.split()]
        digits = {}

        # PART 1
        total = 0
        for o in output:
            for i in uniques:
                if len(o) == uniques[i]:
                    total+=1
        
        # PART 2
        for sig in signal:
            for i in uniques:
                if len(sig) == uniques[i]:
                    digits[i] = sig
        
        # 6 + 1 = 8
        for sig in signal:
            if len(sig) == 6 and sig not in digits.values():
                if len(set(sig + digits[1])) == 7:
                    digits[6] = sig
        
        # 4 + 0 = 8
        for sig in signal:
            if len(sig) == 6 and sig not in digits.values():
                if len(set(sig + digits[4])) == 7:
                    digits[0] = sig
        
        # last 6 digit must be 9
        for sig in signal:
            if len(sig) == 6 and sig not in digits.values():
                digits[9] = sig
                
        # the remaining are 5 segments each and two must differ by ONLY 1
        fives = [sig for sig in signal if len(sig) == 5]
        for five in fives:
            if len(set(five) - set(digits[1])) == 3:
                digits[3] = five
        
        # 2 + 9 = 8
        for five in fives:
            if five not in digits.values():
                if len(set(five + digits[9])) == 7:
                    digits[2] = five
                    
        for five in fives:
            if five not in digits.values():
                digits[5] = five
        
        digits_rev = {}
        for key, value in digits.items():
            digits_rev[value] = key
            
        output_digit = ''
        for digit in output:
            output_digit += str(digits_rev[digit])
        
        grand_total_pt2+=int(output_digit)
        grand_total_pt1+=total
        
    print(grand_total_pt1)
    print(grand_total_pt2)