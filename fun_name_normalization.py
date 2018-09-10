suffixes  =  ["DR ", "ESQ ", "JR ", "MD ", "MR ", "MRS ", "MS ", "PHD ", "REV ", "RN ", "SR ", "V ", "IV ", "III ", "II ", "I ",  " DR",  " ESQ",  " JR",  " MD", " MR", " MRS",  " MS",  " PHD",  " REV",  " RN",  " SR",  " V",  " IV",  " III",  " II",  " I"]
special_chars  =  [",", "-", "!", r"'","()", "&", ";", "+", "*", ".", r"/", ":", ";", "?", "="]

org_name = "Mr's William H Smith Jr"

name = org_name.upper()


print(name)

for special_char in special_chars:
    if special_char in name:
        name = name.replace(special_char, "")
print(name)

for suffixe in suffixes:
    if suffixe in name:
        name = name.replace(suffixe, "")


