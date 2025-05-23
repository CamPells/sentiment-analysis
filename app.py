lines = []

with open("transcript.txt", "r") as f:
    for line in f:
        cleaned = line.strip()
        if cleaned:  
            lines.append(cleaned)




for line in lines:
    
    speaker, text = line.split(":", 1)
    print(speaker,text)
