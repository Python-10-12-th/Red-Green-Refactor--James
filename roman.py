def convert_roman_numerals(s):	
    count =0
    for char in s:
        if char == "I":	 
            count+=1
        elif char == "V":
            count += 5
        return count