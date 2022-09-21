infile = open('info_security.txt', 'r')
outfile = open('encrypted.txt', 'w')

read = infile.read()
#symbols = ['!','@','#','$','%','^','&','*','?','(',')','~','<','>','/','|', '+','=',';',':','{','}','[',']','"',',']




codes = {'A':'!','a':'9','B':'@','b':'8','C':'#','c':'7',
        'D':'#','d':'6','E':'$','e':'5','F':'%','f':'4',
        'G':'^','g':'3','H':'&','h':'2','I':'*','i':'1',
        'J':'?','j':',','K':'(','k':'.','L':'(','l':'[',
        'M':'~','m':']','N':'<','n':'`','O':'>','o':"'",
        'P':'/','p':'a','Q':'|','q':'s','R':'+','r':'d',
        'S':'=','s':'f','T':';','t':'g','U':':','u':'h',
        'V':'{','v':'j','W':'}','w':'k','X':'[','x':'l',
        'Y':']','y':'q','Z':'"','z':'w'}


for i in read:
    if str(i) in codes:
        letter = codes[str(i)]
        outfile.write(letter)
    else:
        outfile.write(str(i))

outfile.close()