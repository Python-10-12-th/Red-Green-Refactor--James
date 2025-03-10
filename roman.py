def convert_roman_numerals(s):	
    count = 0

    for i in range(len(s)):
        if s[i] == "I":	 
            if i + 1 < len(s) and s[i + 1] == "V":
                count += 4
                continue
            if i + 1 < len(s) and s[i + 1] == "X":
                count += 9
                continue
            count += 1
        elif s[i] == "V":
            if i > 0 and s[i - 1] == "I":  
                continue  
            count += 5
        elif s[i] == "X":
            if i > 0 and s[i - 1] == "I":  
                continue  
            count += 10
        elif s[i] == "L":
            if i > 0 and s[i - 1] == "I":  
                continue  
            count += 50
        elif s[i] == "C":
             if i > 0 and s[i - 1] == "X":
                 continue  
             count += 100

    return count
