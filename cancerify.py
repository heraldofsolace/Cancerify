import sys
import random
import emoji
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-e',action='store_true',dest='use_emoji',help='Use emojis',default=False)
parser.add_argument('--emojify',action='store_true',dest='use_emoji',help='Use emojis',default=False)
parser.add_argument('-n',action='store',dest='r',type=int,help='max number of emojis',default=20)
parser.add_argument('-f',action='store',dest='filename',help='File name',default='none')
parser.add_argument('-c', action = 'store_true',dest='use_letters',help = 'Use letters',default = False)
parser.add_argument('-l',action = 'store_true', dest='use_lenny', help='use lenny faces', default=False)
parser.add_argument('-p',action = 'store', dest = 'p', type=int, help = 'Max number of lennies', default = 20)
parser.add_argument('-b',action = 'store_true', dest = 'use_b', help = 'Replace "b" with B emoji', default=False)
args = parser.parse_args()
#huge list of emojis (add more if you want from here https://www.webpagefx.com/tools/emoji-cheat-sheet/)
#note: not all emojis are supported
emoji_list = [':rage:',':laughing:',':blush:',':relieved:',':sweat:',':weary:',':sweat_drops:',':zzz:',
        ':fist:',':point_down:',':pray:',':person_with_blond_hair:',':smiley_cat:',':droplet:',':pig:',':elephant:',
        ':woman:',':hear_no_evil:',':eyes:',':unamused:',':sunglasses:',':star2:',':punch:',':raised_hands:',':joy_cat:',
        ':person_frowning:',':skull:',':lips:',':fire:',':ok_hand:']

#List of Lenny faces
lenny_list = ['( \u0361\u00b0 \u035c\u0296 \u0361\u00b0 )', '(\u2310\u25a0_\u25a0)','\u1633\u2a36\u1a0e\u2a36\u1630','(\u00f2\u1d25\u00f3)','( \u0360\u00b0 \u035c\u0296 \u00b0)','( \u0361\u239a \u035c\u0296 \u0361\u239a)','\u00af\_\u30c4_/\u00af','\u0ca0_\u0ca0','\u291c(\u0298_\u0298)\u290f','(\u3065\u25d4 \u035c\u0296\u25d4)\u3065']
#List of letters. All the entries 'look' like their English counterpart. Those I didn't find are left in English
unicode_cyrillic_capital = ['\u0466', '\u0412', '\u0421', 'D', '\u04DA', 'F', 'G', '\u04A4', '\u0457', '\u0458', '\u04A0', 'L', '\u041C', '\u04E4', '\u04E6', '\u0420', 'Q', '\u042F', 'S', '\u0422', 'U', '\u0476', '\u0460', '\u04C1', '\u04EE', 'Z']

unicode_greek_coptic  =['\u03B1', '\u03B2', '\u03DA', 'd', '\u03B5', '\u03DC', 'g', '\u03E7', '\u03CA', '\u03F3', '\u03BA', '\u03B9', '\u03FB', '\u03F0', '\u03D9', '\u03C1', '\u03E4', 'r', '\u03E9', '\u03EF', '\u03B0', '\u03BD', '\u03E3', '\u03C7', '\u03AB', '\u03B6']

#List of the list of letters
letter_list = [unicode_cyrillic_capital, unicode_greek_coptic]
#Paste the text into a file
#Pass the filename as argument
if args.filename=='none':
    f = sys.stdin
else:
    f=open(args.filename)
while True:
    #read one character
    c=f.read(1)
    if not c:
        #EOF
        break
    if c in ['B','b'] and args.use_b:
        print(emoji.emojize(':b:',use_aliases=True),end='')
        continue
    #Don't bother about those who are not alphabets
    if random.randint(1,4) == 1 and args.use_letters and c.isalpha():
        #Choose a list randomly and map the letter to proper index
        print(letter_list[random.randint(0,1)][ord(c) - (65 if c.isupper() else 97)],end='') 
        continue
    #Randomly convert to uppercase and print
    print(c.upper() if random.randint(1,4)==2 and c.isalpha() else c,end='')
    #Replace the spaces randomly with random number of emoji
    if random.randint(1,4) ==3 and c==' ' and args.use_emoji:
        for i in range(random.randint(1,args.r)):
            print(emoji.emojize(emoji_list[random.randint(0,len(emoji_list)-1)],use_aliases=True),end=' ')
    #Replace the spaces randomly with random number of lennies
    if random.randint(1,4) == 4 and c == ' ' and args.use_lenny:
        for i in range(random.randint(1,args.p)):
            print(lenny_list[random.randint(0,len(lenny_list)-1)],end=' ')
