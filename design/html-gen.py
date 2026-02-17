'''
Generates an HTML file with a table based on wordlists and category files.
'''

SP_MAPPING = {}
COLOR_MAPPING = {}

def load_words(filename):
    global SP_MAPPING
    with open(filename) as file:
        for line in file:
            [num, word] = line.strip().split("  ")
            num = int(num, base=16)
            SP_MAPPING[num] = word.lower()

def load_categories(filename):
    global COLOR_MAPPING
    with open(filename) as file:
        for line in file:
            [angle, *words] = line.strip().split(" ")
            for word in words:
                if word in COLOR_MAPPING:
                    raise ValueError(f"word {word} cannot be assigned to angle {angle} (has angle {COLOR_MAPPING[word]})")
                COLOR_MAPPING[word] = angle
            
            # print(f"{angle:>3}: {len(words):<2} | {'*' * (len(words) * 2)}")

load_words("wordlist-spk1.txt")
load_categories("categories-rare.txt")

with open("output.html", "w") as file:
    file.write("""\
<html>
<head>
<title>sitelen nasa a</title>
<link rel="stylesheet" href="test.css">
</head>
""")
    file.write("<body>\n<table>\n")
    for row in range(0xF1900, 0xF1A00, 0x010):
        file.write("<tr>")
        file.write(f"<th>U+{row:X}</th>")
        for col in range(0, 16):
            cp = row + col
            lookup = SP_MAPPING.get(cp) or ""
            angle = COLOR_MAPPING.get(lookup)
            angle = f" style=\"background-color: hsl({angle} 100% 85%);\"" if angle is not None else ""
            file.write(f"<th class=\"sitelen-pona\"{angle}>{lookup}</th>")
            pass
    
        file.write("</tr>\n")
        pass
    file.write("</table>\n</body>\n")
    file.write("</html>\n")