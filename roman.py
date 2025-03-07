def convert_roman_numerals(s):	
    count = 0

    for i in range(len(s)):
        if s[i] == "I":	 
            if i + 1 < len(s) and s[i + 1] == "V":
                count += 4
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

    return count
