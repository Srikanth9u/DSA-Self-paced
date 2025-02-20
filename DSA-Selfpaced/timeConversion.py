def timeConversion(s):
    # Write your code here
    sr = int(s[:2])  
    
    
    if s[-2:] == "PM" and sr != 12:
        sr += 12
    elif s[-2:] == "AM" and sr == 12:
        sr = 0

    return f"{sr:02}{s[2:8]}"
