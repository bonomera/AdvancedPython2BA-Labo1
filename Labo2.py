import re
def Exo1():
    suite = input('Inserer le pattern a verifier')
    pattern = r"[+][0-9]{2}[ ][0-9]{3}[ ][0-9]{2}[ ][0-9]{2}[ ][0-9]{2}"
    p = re.compile(pattern)
    if p.match(suite) is not None:
        print("c'est le pattern a)")
    pattern1 = r"^[+-]?[0-9]*$"
    p = re.compile(pattern1)
    if p.match(suite) is not None:
        print("c'est le pattern b)")
    pattern2 = r"[1-9]?[0-9]{3}[a-zA-z]{3}|[1-9]?[a-zA-Z]{3}[0-9]{3}"
    p = re.compile(pattern2)    
    if p.match(suite) is not None:
        print("c'est le pattern c)")
    pattern3 = r"[A-Z]:\\"
    p = re.compile(pattern3)
    if p.match(suite) is not None:
        print("c'est le pattern d)")
    
def Exo2():
    f = open("Labo2.txt", "r")
    lines = f.readlines()
    count = 0
    for line in lines:
        listfinal = []
        count += 1
        if line == '\n':
                continue
        else:
            pattern1 = r"[+-]?[0-9]+"
            p = re.compile(pattern1)
            line2 = p.findall(line)
            for x in line2:
                if x == '':
                    line2.remove(x)
                else:
                    listfinal.append(x)
            print("Ligne ", count, " : ", ", ".join(map(str, listfinal)))

def Exo3():
    pattern = r"^(?P<protocol>[a-zA-Z]+)://(?P<domain>[a-zA-Z0-9.-]+)/(?P<path>.*)$"
    p = re.compile(pattern)
    suite = 'https://www.example.com/path/to/resource'
    m = p.match(suite) 
    if m is not None:
        print("Protocol:", m.group('protocol'))
        print("Domain:", m.group('domain'))
        print("Path:", m.group('path'))
        print("c'est le pattern a)")
    else:
        print("ce n'est pas le pattern a)")

def Exo4(numbgrid, y,x, suite):
    dicty = {1 : [r"(AS|SA)"],
            2 : [r"(EC|CD)[ABS]",r".[GROS]+",r"C?[KS]+"],
            3 : [r"[ARBRE](EN|SM)",r"(IS|HAS).*", r"(.)\1[^AEIOU]"]}
    dictx = {1: [r".*",r"[^AEIOU]+"], 
             2: [r"[^CBF]|(MC|XD)",r"[CRL]*[ACK]", r"[AEIOU]*S"], 
             3: [r"[BOU]|(OI|IO)", r"[FLE](SO|OS)", r".C*(RA|L)"]}
    pattern =    dicty[numbgrid][y]
    p = re.compile(pattern)
    m = p.match(suite)
    if m is not None:
        print("bonne expression en x")
        pattern1 = dictx[numbgrid][y]
        p1 = re.compile(pattern1)
        m1 = p1.match(suite)
        if m1 is not None:
            print("bonne expression en y({})".format(y))
        else:
            print("ce n'est pas la bonne expression en y({})".format(y))
    else:
        print("ce n'est pas la bonne expression en x")
