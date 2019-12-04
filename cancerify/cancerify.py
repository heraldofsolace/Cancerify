import sys
import random
import emoji
import argparse
import requests
import re
import bidict

class CancerifierArgument:
    def __init__(self, args):
        map = {
            "use_emoji": ("use_emoji", False),
            "max_emoji": ("r", 20),
            "content": ("f", ""),
            "use_letters": ("use_letters", False),
            "use_lenny": ("use_lenny", False),
            "max_lenny": ("p", 20),
            "b-ify": ("use_b",False),
            "prettify": ("x", False),
            "oof-ify": ("oof", False),
            "antonym": ("nt", False),
            "antonym_file": ("ntfile", None),
            "zalgofy":("zalgofy", False),
            "zintup": ("zintup", 5),
            "zintmid": ("zintmid", 5),
            "zintdown": ("zintdown", 5),
            "zintrand": ("zintrand", True)
        }

        for k,v in map.items():
            if k in args:
                setattr(self, v[0], args[k])
            else:
                setattr(self, v[0], v[1])

class Cancerifier:
    @staticmethod
    def cancerify(args):
        app_key = 'caa9fa1fe35c4d61eda91becb49a14fc'
        app_id = '8db71754'
        result = ""
        #huge list of emojis (add more if you want from here https://www.webpagefx.com/tools/emoji-cheat-sheet/)
        #note: not all emojis are supported
        emoji_list = [':rage:',':laughing:',':blush:',':relieved:',':sweat:',':weary:',':sweat_drops:',':zzz:',
                ':fist:',':point_down:',':pray:',':person_with_blond_hair:',':smiley_cat:',':droplet:',':pig:',':elephant:',
                ':woman:',':hear_no_evil:',':eyes:',':unamused:',':sunglasses:',':star2:',':punch:',':raised_hands:',':joy_cat:',
                ':person_frowning:',':skull:',':lips:',':fire:',':ok_hand:']
        antonym_list = bidict.bidict()
        if args.ntfile:
            with open(args.ntfile) as f:
                l = f.read().strip().split(',')
                for i in l:
                    antonym_list[i.split(':')[0]] = i.split(':')[-1]

        #List of Lenny faces
        lenny_list = ['( \u0361\u00b0 \u035c\u0296 \u0361\u00b0 )', '(\u2310\u25a0_\u25a0)','\u1633\u2a36\u1a0e\u2a36\u1630','(\u00f2\u1d25\u00f3)','( \u0360\u00b0 \u035c\u0296 \u00b0)','( \u0361\u239a \u035c\u0296 \u0361\u239a)','\u00af\_\u30c4_/\u00af','\u0ca0_\u0ca0','\u291c(\u0298_\u0298)\u290f','(\u3065\u25d4 \u035c\u0296\u25d4)\u3065']
        #List of letters. All the entries 'look' like their English counterpart. Those I didn't find are left in English
        unicode_cyrillic_capital = ['\u0466', '\u0412', '\u0421', 'D', '\u04DA', 'F', 'G', '\u04A4', '\u0457', '\u0458', '\u04A0', 'L', '\u041C', '\u04E4', '\u04E6', '\u0420', 'Q', '\u042F', 'S', '\u0422', 'U', '\u0476', '\u0460', '\u04C1', '\u04EE', 'Z']

        unicode_greek_coptic  =['\u03B1', '\u03B2', '\u03DA', 'd', '\u03B5', '\u03DC', 'g', '\u03E7', '\u03CA', '\u03F3', '\u03BA', '\u03B9', '\u03FB', '\u03F0', '\u03D9', '\u03C1', '\u03E4', 'r', '\u03E9', '\u03EF', '\u03B0', '\u03BD', '\u03E3', '\u03C7', '\u03AB', '\u03B6']

        zalgo_marks_above = ['\u0300', '\u0301', '\u0302', '\u0303', '\u0304', '\u0305', '\u0306', '\u0307', '\u0308', '\u0309', '\u030A', '\u030B', '\u030C', '\u030D', '\u030E', '\u030F', 
                             '\u0310', '\u0311', '\u0312', '\u0313', '\u0314', '\u0315', '\u031A', '\u031B', '\u033D', '\u033E', '\u033F', '\u0340', '\u0341', '\u3042', '\u3043', '\u3044', '\u3046', '\u034A', '\u034B', 
                             '\u034C', '\u0350', '\u0351', '\u0352', '\u0357', '\u0358', '\u035B', '\u035D', '\u035E', '\u0360', '\u0361' ]
        
        zalgo_marks_below = ['\u0316', '\u0317', '\u0318', '\u0319', '\u031C', '\u031D', '\u031E', '\u031F', '\u0320', '\u0321', '\u0322', '\u0323', '\u0324', '\u0325', '\u0326', '\u0327', '\u0328', 
                             '\u0329', '\u032A', '\u032B', '\u032C', '\u032D', '\u032E', '\u032F', '\u0330', '\u0331', '\u0332', '\u0333', '\u0339', '\u033A', '\u033B', 
                             '\u033C', '\u0345', '\u0347', '\u0348', '\u0349', '\u034D', '\u034E', '\u0353', '\u0354', '\u0355', '\u0356', '\u0359', '\u035A', '\u035C', '\u035F', '\u0362' ]
        
        zalgo_marks_over = [ '\u0334', '\u0335', '\u0336', '\u0337', '\u0338' ]
        
        zalgo_marks_latin_above = [ '\u0363', '\u0364', '\u0365', '\u0366', '\u0367', '\u0368', '\u0369', '\u036A', '\u036B', '\u036C', '\u036D', '\u036E', '\u036F' ]
        
        zalgo_position_dict = { "up": zalgo_marks_above + zalgo_marks_latin_above, "mid": zalgo_marks_over, "down": zalgo_marks_below }
        #List of the list of letters
        letter_list = [unicode_cyrillic_capital, unicode_greek_coptic]

        new_text = ''
        if not args.x:

            t = args.f.lower()
            # Delimiters. Feel free to add more.
            unique_words = set(re.split(r' |\t|\n|\r|\r\n|\,|\.|\;|\-|\+', t))
            count = 0
            if args.nt:
                for word in unique_words:
                    # 60/min hit limit
                    if count < 60:
                        r = requests.get('https://od-api.oxforddictionaries.com:443/api/v1/entries/en/{}/antonyms'.format(word),headers = {'app_id':app_id, 'app_key':app_key})
                        antonym  = ''

                        if r.status_code == 200:
                            r = r.json()
                            try:
                                antonym = r['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['antonyms'][-1]['text']
                            except KeyError:
                                pass

                    if word in antonym_list.keys():
                        antonym = antonym_list[word]
                    if word in antonym_list.inv.keys():
                        antonym = antonym_list.inv[word]
                    if antonym != '':
                        t = re.sub(r'\b{}\b'.format(word), '{}n\'t'.format(antonym), t)
            for c in t:
                if c in ['B','b'] and args.use_b:
                    result += emoji.emojize(':b:',use_aliases=True)
                    continue
                #Don't bother about those who are not alphabets
                if random.randint(1,5) == 1 and args.use_letters and c.isalpha():
                    #Choose a list randomly and map the letter to proper index
                    result += letter_list[random.randint(0,1)][ord(c) - (65 if c.isupper() else 97)]
                    continue
                #Randomly convert to uppercase and print
                result += (c.upper() if random.randint(1,5)==2 and c.isalpha() else c)
                #Replace the spaces randomly with random number of emoji
                if random.randint(1,5) ==3 and c==' ' and args.use_emoji:
                    for i in range(random.randint(1,args.r)):
                        result += emoji.emojize(emoji_list[random.randint(0,len(emoji_list)-1)],use_aliases=True)
                #Replace the spaces randomly with random number of lennies
                if random.randint(1,5) == 4 and c == ' ' and args.use_lenny:
                    for i in range(random.randint(1,args.p)):
                        result += lenny_list[random.randint(0,len(lenny_list)-1)]
                #Replace the spaces randomly with oof
                if random.randint(1,5) == 5 and c == ' ' and args.oof:
                    result += ' oof '
                    
            # Zalgo-fy after everything else is done
            
        
            if args.zalgofy:
                intensities = { "up": args.zintup, "mid": args.zintmid, "down": args.zintdown }
                result__ = ""
                for c in result:
                    zalgo_counts = { k: 0 for k in zalgo_position_dict.keys() }
                    for position in zalgo_position_dict.keys():
                        zalgo_counts[position] = random.randint(0, intensities[position]) if args.zintrand else intensities[position]
                    result__ += c
                    
                    for position in zalgo_position_dict.keys():
                        chars = zalgo_position_dict[position]
                        count = intensities[position]
                        res_ = random.sample(chars, count)
                        random.shuffle(res_)
                        
                        result__ += ''.join(res_)
                result = result__
            return result
        else:
            #Prettify
            #Just assume that the following lines work, with a few bugs.
            #It will make life easier.

            text = [i for i in args.f]
            for i in range(len(text)):
                if text[i] in emoji.UNICODE_EMOJI:
                    if text[i] == emoji.emojize(':b:',use_aliases=True):
                        text[i] = 'B'
                    else:
                        text[i] = ' '
                for lists in letter_list:
                    if text[i] in lists:
                        text[i] = chr(lists.index(text[i]) + 65)

            for lenny in lenny_list:
                temp_lenny = [c for c in lenny]
                i = 0
                while i< len(text) - len(temp_lenny):
                    if text[i] == temp_lenny[0] and text[i:i+len(temp_lenny)] == temp_lenny:
                        del text[i:i+len(temp_lenny)]
                    else:
                        i += 1

            if text[0].isalpha():
                text[0] = text[0].upper()
            punc_list = ['.','?','!']
            for i in range(1, len(text)):
                if text[i].isalpha():
                    if text[i] == 'I':
                        if i != 0:
                            if text[i-1] == ' ' and (text[i+1] == ' ' or text[i+1] == "'"):
                                continue
                            else:
                                text[i] = text[i].lower()
                        else:
                            if text[i+1] == ' ' or text[i+1] == "'":
                                continue
                            else:
                                text[i] = text[i].lower()
                    else:
                        if text[i - 1] in punc_list:
                            text.insert(i,' ')

                        else:
                            text[i] = text[i].lower()

                elif text[i].isdigit():
                    continue
                else:
                    if i < len(text) - 1 and (ord(text[i]) not in [39,32,34]):
                        text.insert(i+1,' ')

            i = 0

            while i < len(text)-1:
                if text[i] == ' ' and text[i+1] == ' ':
                    del text[i]
                else:
                    i = i+1
            for i in range(len(text)-2):
                if text[i] in punc_list:
                    text[i+2] = text[i+2].upper()
            if text[-1] == '\n':
                del text[-1]

            return "".join(text)

