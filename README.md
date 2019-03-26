# Cancerify
World's some of the most famous torture options, collected in one script. Pass an innocent text into this script, and get back the most cringiest text to look at.

Requires the 'emoji' package and the 'bidict' package.

# Starring
1. Random uppercase
2. Emojify
3. Lennify
4. Cancerous fonts
5. B-ify
6. n't-ify


# Usage:
Cancerify can be used in two ways: either as a command line script or from another Python script

## Using from command line
```python cancerify.py -f filename -c -l -b -e -n 30 -t -T antonym_file```

-f the filename from where to read the text, leave empty for reading from stdin

-l lennify, randomly insert lenny faces

-b b-fy, replace 'b' or 'B' with B emoji

-e emojify, insert randomly random number of emojis

-n max number of consecutive emojis

-c use cancerous fonts (currently greek and coptik)

-t Use n't-ify 

-T Antonym file

If no file is specified, Cancerify will read from stdin. Press Ctrl-D to stop.

## Using from another file:

First you have to import Cancerifier and CancerifierArgument

```
from cancerify import Cancerifier, CancerifierArgument
```

Next, instantiate a CancerifierArgument from a dictionary. The dictionary can have these arguments:

1.  use_emoji: True or False
2.  max_emoji: Number
3.  content: String which is to cancerify
4.  use_letters: True or False,
5.  use_lenny: True or False,
6.  max_lenny: Number,
7.  b-ify: True or False,
8.  prettify: True or False,
9.  oof-ify: True or False,
10. antonym: True or False,
11. antonym_file: Path to antonym file

Cancerify uses [Oxford Dictionary API](https://developer.oxforddictionaries.com/) to get the antonyms. The user can optionally specify a file of antonyms using the -T flag.<br>
The structure of the antonym file should be - 

```word1:antonym1, word2:antonym2, ... ```

In case of a word having more than one antonym in the API response, the last one would be used.

If a word has antonym in both the API response and the local file, the latter will be preferred.

**Note**: Currently Cancerify doesn't change in-word. So, it will change "day" to nightn't but won't change "saturday."<br>
The free plan of Oxford API limits 60 searches per minute. Cancerify will hit the API for first 60 words only (words are converted in sets, so this selection is kinda random)

# Example
**n't-ify** - 

Input: Go there

Antonym file: there:here

Output: CoMen't Heren't

# Sample text file:
What the fuck did you just fucking say about me, you little bitch? I’ll have you know I graduated top of my class in the Navy Seals, and I’ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I’m the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You’re fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that’s just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little “clever” comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn’t, you didn’t, and now you’re paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You’re fucking dead, kiddo.

```python cancerify.py -f filename -c -l -b -e -n 30 -t```
# Output
WHαt tHE fucK did ᘳ⨶ᨎ⨶ᘰ ( ͠° ͜ʖ °) yoΰ ( ͠° ͜ʖ °) (づ◔ ͜ʖ◔)づ ⤜(ʘ_ʘ)⤏ ( ͠° ͜ʖ °) ಠ_ಠ ಠ_ಠ (⌐■_■) ¯\_ツ_/¯ (づ◔ ͜ʖ◔)づ ᘳ⨶ᨎ⨶ᘰ ( ͡° ͜ʖ ͡° ) ( ͡° ͜ʖ ͡° ) ಠ_ಠ uϰfaiRn't FucKϊNG 👌 😩 😩 💧 🌟 😡 🌟 🙍 😩 👱 😎 😹 😹 👇 😎 🙌 👩 💤 😊 😒 💧 say prεcIsӚlyn't 😡 😊 🙏 😒 me, ΫOU LarGen't 🅱їtСh? ϊ’lL 😒 🌟 😎 😹 🙏 😌 🐘 🙍 🙍 👱 👄 🌟 🅱e 🙏 👇 🐷 🔥 👀 👇 😒 💀 😹 😒 👊 🙉 🙌 😌 👌 😊 💀 👇 🙏 😹 💧 😓 👌 👀 😺 😎 😆 😆 😺 🅱ereFt oFn't YӦΰ know i 😆 👀 😊 😒 👌 😆 😒 😌 😓 👄 😹 😹 😒 😹 😎 👄 😺 ✊ 💤 😆 💀 👀 😓 👱 🔥 😆 gЯѦdUatEd 🅱asεn'Т of 👩 ( ͠° ͜ʖ °) ¯\_ツ_/¯ ¯\_ツ_/¯ ¯\_ツ_/¯ (づ◔ ͜ʖ◔)づ ( ͡⎚ ͜ʖ ͡⎚) (⌐■_■) ⤜(ʘ_ʘ)⤏ My clASs oΰtSIdӚn'Т 😓 🙌 🙌 😎 😩 💦 👇 🙉 😌 👩 😎 😡 👀 👩 😌 💀👩 😆 🙏 💦 😌 👌 😩 👊 😊 The nαvΫ SeaLs, 😌 😹 🔥 😆 😩 🙌 💧 🐘 😌 🙌 🐷 😡 🙌 😒 👌 😒 😎 👱 👀 🙍 😌 👩 😡 👩 👄 ANd i’ve 🅱eӚn ΰNcoNϰecTedN't 😡 🌟 🙏 😌 👄 💧 🌟 👊 😌 🐷 👌 😆 👊 😡 💤 👇 😩 🐷 💧 👀 😌 😺 💦 😆 🌟 😎 👇 🙌 outsideϰ't rAren't 😎 🌟 😺 🙏 👀 😊 pU🅱lїcϰ'T raids On 👇 🌟 👱 💦 😓 🙌 😊 💦 💧 👱 😆 😺 👌 🐘 👌 💦 👇 😎 😒 💀 🙍 😒 😆 🙏 The unDeЯϩIde ofn'T 💀 😎 ✊ 🙉 😎 😎 😓 🔥 💀 👀 💦 😓 😆 🙌 💧 👩 🙌 💤 💧 👌 😺 😊 👌 💧 🔥 😺 👄 al-qUAeda, anD i 🅱e 🅱εrefT ofN'Т 🅱t 300 🐷 💤 😺 💧 💧 ✊ 🐷 💦 😆 😆 😩 👇 💀 👀 🌟 ಠ_ಠ ⤜(ʘ_ʘ)⤏ ϚϙNfirϻed kiLlS. i am (⌐■_■) (⌐■_■) ᘳ⨶ᨎ⨶ᘰ TrainEd outsIDeN't gorilLa harМonYn'Т anD i’ϻ tHε 🅱r OUtsIden't tHE pαrTialӤ't us arϻEd fӦrceS. yOu αrӚ sOmEtҤIӤgӤ'T ( ͡⎚ ͜ʖ ͡⎚) ⤜(ʘ_ʘ)⤏ ᘳ⨶ᨎ⨶ᘰ ( ͡° ͜ʖ ͡° ) Тo ( ͡⎚ ͜ʖ ͡⎚) ( ͡⎚ ͜ʖ ͡⎚) ᘳ⨶ᨎ⨶ᘰ ¯\_ツ_/¯ ( ͡° ͜ʖ ͡° ) ( ͡⎚ ͜ʖ ͡⎚) ಠ_ಠ me andn't unfAirn't tҤE sαmen'Т ТaRGεt. 👩 👄 👀 👀 🙏 💤 😎 💤 🙏 👇 👄 🔥 🙉 💧 🐷 😩 👊 😡 😡 💧 👄 😩 👇 💀 😩 i 🐷 🙌 💤 😩 🙍 👀 🙉 😩 😓 😌 🌟 👄 😹 💦 👩 🔥 👱 🐷 😆 😆👌 🐘 😎 👱 😒 👩 💦 👊 😆 (⌐■_■) ( ͠° ͜ʖ °) will wїpe you thE fucҠ inn't ϣitH 🙉 ✊ 👄 😒 PREcϊsiOn thӚ Likes (òᴥó) ( ͡⎚ ͜ʖ ͡⎚) ¯\_ツ_/¯ ( ͡⎚ ͜ʖ ͡⎚) ¯\_ツ_/¯ ಠ_ಠ ( ͡⎚ ͜ʖ ͡⎚) (⌐■_■) ( ͡° ͜ʖ ͡° ) ⤜(ʘ_ʘ)⤏ ( ͡° ͜ʖ ͡° ) ( ͡⎚ ͜ʖ ͡⎚) ( ͠° ͜ʖ °) ⤜(ʘ_ʘ)⤏ Ӧf wҤϊch 🙍 😡 🌟 💧 🙌 🙍 🐷 👊 😺 👀 💦 👇 👌 💧 😌 👊 👄 👄 ✊ 👊 😌 😆 👌 😹 💧 🙌 👄 🌟 😹 👇ᨎ⨶ᘰ ಠ_ಠ (づ◔ ͜ʖ◔)づ ⤜(ʘ_ʘ)⤏ (òᴥó) ( ͡° ͜ʖ ͡° ) ( ͠° ͜ʖ °) ⤜(ʘ_ʘ)⤏ (òᴥó) (òᴥó) ( ͡° ͜ʖ ͡° ) ಠ_ಠ (づ◔ ͜ʖ◔)づ (づ◔ ͜ʖ◔)づ ⤜(ʘ_ʘ)⤏ ᘳ⨶ᨎ⨶ᘰ ( ͡° ͜ʖ ͡° ) (⌐■_■) hAs 😊 😌 😺 💧 🌟 🙏 😓 😒🔥 😆 👄 👊 😩 forevern't ( ͡° ͜ʖ ͡° ) ( ͠° ͜ʖ °) ⤜(ʘ_ʘ)⤏ (òᴥó) (òᴥó) (づ◔ ͜ʖ◔)づ ⤜(ʘ_ʘ)⤏ (òᴥó) 🅱een 🙉 👱 😡 ( ͠° ͜ʖ °) ¯\_ツ_/¯ (òᴥó) ᘳ⨶ᨎ⨶ᘰ ಠ_ಠ ( ͡⎚ ͜ʖ ͡⎚) ¯\_ツ_/¯ (òᴥó) (づ◔ ͜ʖ◔)づ (づ◔ ͜ʖ◔)づ on 💦 😎 👱 👀 👩 😆 😎 🙍 😓 😺 😓 😎 💧 ✊ 🌟 😒 🐷 ✊ 🙉 🐘 😩 👇 🌟 ✊ 😎⨶ᨎ⨶ᘰ ¯\_ツ_/¯ ᘳ⨶ᨎ⨶ᘰ ( ͡° ͜ʖ ͡° ) ( ͡° ͜ʖ ͡° ) (òᴥó) (⌐■_■) (⌐■_■) (づ◔ ͜ʖ◔)づ ⤜(ʘ_ʘ)⤏ ⤜(ʘ_ʘ)⤏ (づ◔ ͜ʖ◔)づ (⌐■_■) (⌐■_■) ( ͠° ͜ʖ °) ⤜(ʘ_ʘ)⤏ (⌐■_■) UndersϊdE ofn't tHϊs Ӛarth, MaЯk mY fUCking (òᴥó) ಠ_ಠ ( ͡⎚ ͜ʖ ͡⎚) ( ͡⎚ ͜ʖ ͡⎚) ¯\_ツ_/¯ ( ͠° ͜ʖ °) ¯\_ツ_/¯ ( ͡⎚ ͜ʖ ͡⎚) ಠ_ಠ ᘳ⨶ᨎ⨶ᘰ ( ͠° ͜ʖ °) ( ͡⎚ ͜ʖ ͡⎚) ( ͠° ͜ʖ °) (òᴥó) (òᴥó) ( ͡° ͜ʖ ͡° ) ( ͠° ͜ʖ °) ⤜(ʘ_ʘ)⤏ (づ◔ ͜ʖ◔)づ ಠ_ಠ WӦrDs. you Leap їntӦ ( ͡⎚ ͜ʖ ͡⎚) ( ͡° ͜ʖ ͡° ) ( ͠° ͜ʖ °) ⤜(ʘ_ʘ)⤏ αCtionn'Т 👩 😊 you (づ◔ ͜ʖ◔)づ (づ◔ ͜ʖ◔)づ ( ͡⎚ ͜ʖ ͡⎚) ( ͡⎚ ͜ʖ ͡⎚) (òᴥó) ¯\_ツ_/¯ ( ͠° ͜ʖ °) ( ͠° ͜ʖ °) (⌐■_■) ( ͡⎚ ͜ʖ ͡⎚) ᘳ⨶ᨎ⨶ᘰ ( ͡° ͜ʖ ͡° ) (づ◔ ͜ʖ◔)づ (⌐■_■) ᘳ⨶ᨎ⨶ᘰ ᘳ⨶ᨎ⨶ᘰ (づ◔ ͜ʖ◔)づ caӤ 😆 😹 ✊ 👌 😆 😊 🙉 ✊ 👇 GiVeN'ϯ αway 💦 👌 👌 💦 🙉 😺 👌 😓 😆 😩 wiϯH SaYiϰG thaT shit to me (づ◔ ͜ʖ◔)づ ಠ_ಠ (づ◔ ͜ʖ◔)づ (⌐■_■) ( ͡⎚ ͜ʖ ͡⎚) ( ͡⎚ ͜ʖ ͡⎚) ( ͡⎚ ͜ʖ ͡⎚) (づ◔ ͜ʖ◔)づ 🅱elowӤ'ϯ thE iӤtӚRϰӚТ? LeaР ϊnto ActϊOӤn't 👄 💀 😌 🌟 aGain, FucKeR. as 💦 🌟 😊 💤 👱 👱 ✊ 👇 🔥 😓 😒 WE 💤 😩 😆 😆 🌟 🐷 😩 😓 ᘳ⨶ᨎ⨶ᘰ ಠ_ಠ ᘳ⨶ᨎ⨶ᘰ ( ͠° ͜ʖ °) (òᴥó) ( ͡⎚ ͜ʖ ͡⎚) ϩpeaκ i 🙏 💧 🔥 👄 💦 😹 🙏 👊 😹 😹 😓 😌 🐘 👩 😹 😎 💧 🙉 👩 😌 💤 👌 😡 👩 aМ (⌐■_■) ᘳ⨶ᨎ⨶ᘰ ᘳ⨶ᨎ⨶ᘰ ⤜(ʘ_ʘ)⤏ ( ͡⎚ ͜ʖ ͡⎚) (づ◔ ͜ʖ◔)づ ( ͠° ͜ʖ °) ಠ_ಠ ᘳ⨶ᨎ⨶ᘰ ಠ_ಠ coNtActiӤg 🙏 🙍 💀 😎 👀 😌 ✊ 😒 💧 💧 🙏 💀 👊 ✊ 😓 👄 👀 👄 💦 😊 🔥 😊 💦 😊 😊 😹 👀 my Рu🅱Licn't netwoRk oϜ 😺 😹 😓 ⤜(ʘ_ʘ)⤏ ⤜(ʘ_ʘ)⤏ ( ͠° ͜ʖ °) (⌐■_■) Spies 💤 👩 🌟 👱 😎 🙉 💀 💧 👇 👇 🌟 👄 👌 🙏 🙉 👩 👄 💤 🙌 😓 🙏 Acroϩs (òᴥó) ( ͡⎚ ͜ʖ ͡⎚) (⌐■_■) (⌐■_■) ⤜(ʘ_ʘ)⤏ thE USa 👀 👩 😺 😹 👀 👀 💦 😆 😺 🐘 🐘 🙍 😊 😓 😌 and 👀 🙌 💦 😺 💦 👄 👀 🔥 😓 👌 😌 👱 ✊ 💧 💦 🙏 👱 😊 😌 👌 👇 🙏 👄 😊 YOur ip ϊs nϙn-εӁiϩteӤceӤ't tЯacεD 🙉 ✊ 😺 💧 😺 🙏 👀 😊 💤 🙍 ✊ unjusТN't now ( ͠° ͜ʖ °) ⤜(ʘ_ʘ)⤏ ¯\_ツ_/¯ ᘳ⨶ᨎ⨶ᘰ ಠ_ಠ ᘳ⨶ᨎ⨶ᘰ (òᴥó) ( ͡⎚ ͜ʖ ͡⎚) (òᴥó) ಠ_ಠ ¯\_ツ_/¯ ( ͡⎚ ͜ʖ ͡⎚) ( ͡⎚ ͜ʖ ͡⎚) ( ͠° ͜ʖ °) ( ͠° ͜ʖ °) so yϙΰ 🙌 👌 👩 👀 🐘 👌 🐷 🙍 🙍 😒 👌 🐷 😌 💤 👇 🐘 😹 😡 🙏 🐷 😎 🌟 👇 🙍 😌 👇 😌 👊 🙍 inFeriϙrϰ'ϯ PЯePArE for 🌟 💤 😡 👱 😒 👌 😺 👩 😎 😊 😹 👀 💦 😓 😹 👌 😊 🌟 😌 👩 the sToRϻ, 👌 👊 👇 😎 😆 😆 💦 💤 😆 🐘 😌 👇 🙏 😩 👌 👀 😎 👌 😎 maggϙt. tHe storМ Tϧaϯ ಠ_ಠ ⤜(ʘ_ʘ)⤏ (⌐■_■) WїPεS inN'T ϯhe cheERfulN't lαrGEn'T tϧing Yoΰ cѦll 😊 😆 😹 😎 👩 😆 😺 🙏 💤 Ӯour 😎 😹 👊 👇 🐷 👄 💀 😡 👌 👄 🔥 💤 😡 🙉 ✊ 👊 💀 non-eχIStεnϚen'ϯ. yoU’re fUcKing liѶϊngn't, ( ͡⎚ ͜ʖ ͡⎚) ( ͠° ͜ʖ °) ( ͡⎚ ͜ʖ ͡⎚) (òᴥó) ⤜(ʘ_ʘ)⤏ ( ͡° ͜ʖ ͡° ) ( ͠° ͜ʖ °) (⌐■_■) (づ◔ ͜ʖ◔)づ ⤜(ʘ_ʘ)⤏ ಠ_ಠ ಠ_ಠ ( ͡° ͜ʖ ͡° ) ( ͡° ͜ʖ ͡° ) ( ͡° ͜ʖ ͡° ) (òᴥó) ¯\_ツ_/¯ κid. 👊 🙉 🙏 👱 😒 🙌 👱 😩 😓 👄 👊 ✊ 😩 💀 i can 🅱e ( ͡⎚ ͜ʖ ͡⎚) ( ͡⎚ ͜ʖ ͡⎚) ( ͡⎚ ͜ʖ ͡⎚) (òᴥó) ᘳ⨶ᨎ⨶ᘰ ᘳ⨶ᨎ⨶ᘰ (⌐■_■) ( ͡⎚ ͜ʖ ͡⎚) ( ͠° ͜ʖ °) (づ◔ ͜ʖ◔)づ anywhere, ANyϯїϻe, aNd i CAn fAСilitαTӚn't yϙu oUТsiDӚn't 🅱elӦwn't 😓 🙉 👇 🙉 👌 😒 😩 😓 👩 sEvεn huӤdred ( ͡⎚ ͜ʖ ͡⎚) ಠ_ಠ ಠ_ಠ ಠ_ಠ ( ͠° ͜ʖ °) ¯\_ツ_/¯ (づ◔ ͜ʖ◔)づ ( ͠° ͜ʖ °) (òᴥó) ¯\_ツ_/¯ WAyS, aϰD thaϯ’S unfairN't wITh (⌐■_■) ¯\_ツ_/¯ ( ͡° ͜ʖ ͡° ) (⌐■_■) ᘳ⨶ᨎ⨶ᘰ (⌐■_■) ಠ_ಠ ಠ_ಠ ( ͡⎚ ͜ʖ ͡⎚) ಠ_ಠ ϻy clothedN'ϯ Hαnds. 😒 💤 🙏 😹 😹 ✊ 😡 😆 😆 🙏 💀 🐷 🙍 💦 💀 😓 🙉 😡 👇 🙌 💤 👱 🐷 😓 👀 not ¯\_ツ_/¯ ( ͡° ͜ʖ ͡° ) ⤜(ʘ_ʘ)⤏ ¯\_ツ_/¯ (づ◔ ͜ʖ◔)づ ಠ_ಠ ಠ_ಠ onLy aϻ i ಠ_ಠ ( ͠° ͜ʖ °) (⌐■_■) ⤜(ʘ_ʘ)⤏ ( ͡⎚ ͜ʖ ͡⎚) (づ◔ ͜ʖ◔)づ (òᴥó) ᘳ⨶ᨎ⨶ᘰ (òᴥó) ( ͡⎚ ͜ʖ ͡⎚) ಠ_ಠ ( ͡° ͜ʖ ͡° ) ( ͡° ͜ʖ ͡° ) (づ◔ ͜ʖ◔)づ ¯\_ツ_/¯ exteϰSively 😹 😌 🔥 🔥 💦 😌 👌 👀 💤 😌 👱 👀 👀 🌟 😊 😓 😓 traiNeD 👊 💤 😊 💦 🙌 😺 🐷 😩 ✊ 👀 oUtsideϰ't proϯeCtedN't give oUtsїden't ( ͡⎚ ͜ʖ ͡⎚) ¯\_ツ_/¯ (⌐■_■) (òᴥó) ⤜(ʘ_ʘ)⤏ (⌐■_■) (づ◔ ͜ʖ◔)づ ( ͡⎚ ͜ʖ ͡⎚) ⤜(ʘ_ʘ)⤏ (⌐■_■) (òᴥó) TӦN't, anDn'ϯ 💤 👊 🙍 🌟 😓 😓 💦 😎 💤 🔥 🙏 i ⤜(ʘ_ʘ)⤏ (づ◔ ͜ʖ◔)づ ¯\_ツ_/¯ ᘳ⨶ᨎ⨶ᘰ ಠ_ಠ (づ◔ ͜ʖ◔)づ (づ◔ ͜ʖ◔)づ ⤜(ʘ_ʘ)⤏ ¯\_ツ_/¯ ( ͠° ͜ʖ °) (⌐■_■) ¯\_ツ_/¯ ( ͡⎚ ͜ʖ ͡⎚) ⤜(ʘ_ʘ)⤏ 🅱e 🅱εreϜt ofn't ¯\_ツ_/¯ ᘳ⨶ᨎ⨶ᘰ ¯\_ツ_/¯ ⤜(ʘ_ʘ)⤏ ( ͡⎚ ͜ʖ ͡⎚) ( ͠° ͜ʖ °) ¯\_ツ_/¯ ( ͠° ͜ʖ °) ¯\_ツ_/¯ (òᴥó) (òᴥó) ¯\_ツ_/¯ (づ◔ ͜ʖ◔)づ ᘳ⨶ᨎ⨶ᘰ ( ͡⎚ ͜ʖ ͡⎚) ಠ_ಠ (づ◔ ͜ʖ◔)づ ACceSs (òᴥó) to tϧe Partialn'Т arsεnal 💀 😌 🐘 😆 👌 🐘 💀 👇 🐘 😌 😎 🙌 💧 😹 😺 😓 ಠ_ಠ ᘳ⨶ᨎ⨶ᘰ (òᴥó) ϙF tҤe (づ◔ ͜ʖ◔)づ ( ͡° ͜ʖ ͡° ) (づ◔ ͜ʖ◔)づ ( ͠° ͜ʖ °) ( ͡⎚ ͜ʖ ͡⎚) sEPaRaTeDn'ϯ sTatεS freShwaterӤ'T 😎 💧 😡 👱 😹 👩 🙉 🙉 😆 🙏 😌 👇 👌 💤 😆 😊 😺 💤 (づ◔ ͜ʖ◔)づ (づ◔ ͜ʖ◔)づ ( ͡⎚ ͜ʖ ͡⎚) ( ͠° ͜ʖ °) (⌐■_■) ⤜(ʘ_ʘ)⤏ (òᴥó) ⤜(ʘ_ʘ)⤏ cOrps ( ͠° ͜ʖ °) ᘳ⨶ᨎ⨶ᘰ (づ◔ ͜ʖ◔)づ ᘳ⨶ᨎ⨶ᘰ anD i wilL uϩe It 🐷 😆 😓 💤 💤 👌 😩 💧 🐘 👱 🌟 ✊ 😎 😩 👇 💀 👌 👱 💦 🙏 😓 👀 😹 👩 👊 🙉 ТO ⤜(ʘ_ʘ)⤏ ( ͡⎚ ͜ʖ ͡⎚) ( ͠° ͜ʖ °) ಠ_ಠ (⌐■_■) (⌐■_■) (òᴥó) ( ͠° ͜ʖ °) ( ͡° ͜ʖ ͡° ) IϯS eMРТyӤ't EχtӚnТ ϯo 👄 😹 🙉 🐷 🙍 🐘 🙉 🙏 😺 💤 🐷 🙌 💦 🐘 💀 💤 🙉 😊 😊 😒 👱 💀 😆 👌 😩 💤 😡 🙌 😓 😊 Wiρe yOUr contEӤTeDn't Ѧss ReαSoNѦ🅱leN'ϯ Тhe 🅱AcK 😡 👌 ✊ 😩 🙏 💧 👱 💀 😹 💦 🙌 😒 🙏 😓 💤 💧 😡 ✊ 👀 🙌 💀 💀 😎 👇 👌 😎 On the UϰdεRsϊdӚ ofn't 🙉 😌 👊 🙍 😎 😌 😌 😆 💀 💦 😹 🙉 💧 👌 😡 🙏 😆 👊 😒 🙌 ton't 😌 🙉 👇 😩 😹 👀 🐷 👌 🙉 😺 ✊ 😓 🐘 🙌 😩 💦 💤 🙍 😎 😒 🔥 💧 👩 ⤜(ʘ_ʘ)⤏ ( ͡° ͜ʖ ͡° ) ( ͡⎚ ͜ʖ ͡⎚) ⤜(ʘ_ʘ)⤏ ⤜(ʘ_ʘ)⤏ (òᴥó) (òᴥó) ( ͡⎚ ͜ʖ ͡⎚) ⤜(ʘ_ʘ)⤏ ⤜(ʘ_ʘ)⤏ OF ¯\_ツ_/¯ ( ͠° ͜ʖ °) ⤜(ʘ_ʘ)⤏ ¯\_ツ_/¯ (⌐■_■) ( ͡⎚ ͜ʖ ͡⎚) (⌐■_■) ಠ_ಠ tϧe islAϰdn't, (づ◔ ͜ʖ◔)づ ⤜(ʘ_ʘ)⤏ (òᴥó) ¯\_ツ_/¯ ( ͡⎚ ͜ʖ ͡⎚) ¯\_ツ_/¯ ¯\_ツ_/¯ ӮӦU 💦 😒 😺 💤 💤 👀 😹 👌 ✊ 💦 👱 👱 🐷 ✊ 💦 😺 🙏 😊 😒 🙍 LaRgeӤ't sHїt. ( ͡⎚ ͜ʖ ͡⎚) (òᴥó) ಠ_ಠ (òᴥó) ⤜(ʘ_ʘ)⤏ (⌐■_■) ಠ_ಠ ( ͡⎚ ͜ʖ ͡⎚) ( ͡° ͜ʖ ͡° ) ⤜(ʘ_ʘ)⤏ ( ͡⎚ ͜ʖ ͡⎚) (づ◔ ͜ʖ◔)づ ⤜(ʘ_ʘ)⤏ ⤜(ʘ_ʘ)⤏ ( ͠° ͜ʖ °) UϰLӚϩSn't ӦnLy You 💧 😆 💀 cOuld 🅱e 🅱eЯeϜt oFϰ'T SeCretn'ϯ wҤaT HoLyӤ't ᘳ⨶ᨎ⨶ᘰ (づ◔ ͜ʖ◔)づ ⤜(ʘ_ʘ)⤏ (òᴥó) (òᴥó) ¯\_ツ_/¯ ¯\_ツ_/¯ ⤜(ʘ_ʘ)⤏ ЯӚTri🅱ution your 💧 👀 🙉 😒 🔥 😒 😹 👊 🙍 🔥 🐘 😹 👀 🙌 💀 👊 👌 🐘 💧 ✊ largeϰ't “cLEVεr” comMeNT ᘳ⨶ᨎ⨶ᘰ ᘳ⨶ᨎ⨶ᘰ (⌐■_■) ( ͡° ͜ʖ ͡° ) ಠ_ಠ ಠ_ಠ (òᴥó) (づ◔ ͜ʖ◔)づ ( ͡° ͜ʖ ͡° ) ( ͠° ͜ʖ °) (⌐■_■) ¯\_ツ_/¯ waS prEϚiϩelyn'Т ¯\_ツ_/¯ ( ͡° ͜ʖ ͡° ) ( ͡° ͜ʖ ͡° ) (òᴥó) ( ͡° ͜ʖ ͡° ) ಠ_ಠ ( ͡° ͜ʖ ͡° ) ( ͠° ͜ʖ °) ( ͡⎚ ͜ʖ ͡⎚) ಠ_ಠ ಠ_ಠ ¯\_ツ_/¯ (づ◔ ͜ʖ◔)づ ( ͡° ͜ʖ ͡° ) ಠ_ಠ (òᴥó) to aCcepTӤ't uPϰ't uРOϰ you, maΫ🅱Ӛ (òᴥó) ( ͡° ͜ʖ ͡° ) ( ͡° ͜ʖ ͡° ) ಠ_ಠ ᘳ⨶ᨎ⨶ᘰ (òᴥó) (づ◔ ͜ʖ◔)づ ᘳ⨶ᨎ⨶ᘰ ¯\_ツ_/¯ (⌐■_■) ᘳ⨶ᨎ⨶ᘰ (òᴥó) ᘳ⨶ᨎ⨶ᘰ (づ◔ ͜ʖ◔)づ ᘳ⨶ᨎ⨶ᘰ (⌐■_■) (⌐■_■) Ӯou would ( ͠° ͜ʖ °) ⤜(ʘ_ʘ)⤏ (づ◔ ͜ʖ◔)づ (づ◔ ͜ʖ◔)づ (づ◔ ͜ʖ◔)づ ( ͠° ͜ʖ °) (òᴥó) ( ͠° ͜ʖ °) 🅱e 👇 👇 😺 🅱eЯeϜT 👩 👄 💤 👄 ofn't hεlD Yϙur FuckinG 😊 🌟 TӦngUe. andӤ't ⤜(ʘ_ʘ)⤏ ᘳ⨶ᨎ⨶ᘰ ( ͡⎚ ͜ʖ ͡⎚) ( ͡° ͜ʖ ͡° ) (づ◔ ͜ʖ◔)づ ᘳ⨶ᨎ⨶ᘰ ಠ_ಠ ¯\_ツ_/¯ (òᴥó) ಠ_ಠ ¯\_ツ_/¯ (⌐■_■) ( ͡⎚ ͜ʖ ͡⎚) (òᴥó) (òᴥó) (づ◔ ͜ʖ◔)づ ¯\_ツ_/¯ ಠ_ಠ ( ͡° ͜ʖ ͡° ) yOU cӦUlDN’t, you diDn’t, aӤd ϰOw ( ͡⎚ ͜ʖ ͡⎚) ᘳ⨶ᨎ⨶ᘰ ( ͡° ͜ʖ ͡° ) ಠ_ಠ ᘳ⨶ᨎ⨶ᘰ ¯\_ツ_/¯ ( ͡° ͜ʖ ͡° ) (òᴥó) ᘳ⨶ᨎ⨶ᘰ ( ͡⎚ ͜ʖ ͡⎚) Ӯoΰ’Re ρѦying The adνѦntѦgӚN'Т, yOU (òᴥó) ( ͠° ͜ʖ °) ( ͡° ͜ʖ ͡° ) (òᴥó) ( ͠° ͜ʖ °) ಠ_ಠ (òᴥó) (⌐■_■) (òᴥó) (òᴥó) (òᴥó) ( ͠° ͜ʖ °) ( ͠° ͜ʖ °) ಠ_ಠ gϙdDѦmϰ 🙌 🙉 💀 😌 🙍 💀 😆 👄 👀 👊 💦 👌 👄 😒 😒 💀 👌 😎 👄 🌟 🐘 😆 🌟 😩 👌 🙍 😓 geӤiUSn'ϯ. i will shiT cѦlmnӚssn't Non't 🅱eloѠn't ಠ_ಠ ᘳ⨶ᨎ⨶ᘰ ⤜(ʘ_ʘ)⤏ (òᴥó) ( ͠° ͜ʖ °) ᘳ⨶ᨎ⨶ᘰ (づ◔ ͜ʖ◔)づ (づ◔ ͜ʖ◔)づ ⤜(ʘ_ʘ)⤏ ( ͠° ͜ʖ °) ( ͡⎚ ͜ʖ ͡⎚) ( ͡⎚ ͜ʖ ͡⎚) ( ͡⎚ ͜ʖ ͡⎚) YOu and 👌 😓 😎 🐷 💤 😎 🙍 🙌 👊 👀 👀 💀 👊 💀 👱 👌 🙍 ✊ 😌 👊 😹 😡 😒 👊 🌟 you wilι ( ͠° ͜ʖ °) ¯\_ツ_/¯ ¯\_ツ_/¯ (⌐■_■) ⤜(ʘ_ʘ)⤏ (づ◔ ͜ʖ◔)づ ಠ_ಠ ಠ_ಠ ᘳ⨶ᨎ⨶ᘰ (づ◔ ͜ʖ◔)づ ᘳ⨶ᨎ⨶ᘰ ⤜(ʘ_ʘ)⤏ ᘳ⨶ᨎ⨶ᘰ ( ͡° ͜ʖ ͡° ) ¯\_ツ_/¯ ( ͡° ͜ʖ ͡° ) (づ◔ ͜ʖ◔)づ (òᴥó) ( ͡⎚ ͜ʖ ͡⎚) ¯\_ツ_/¯ drαinn't ouTsiden'T it. ( ͠° ͜ʖ °) ( ͡° ͜ʖ ͡° ) (づ◔ ͜ʖ◔)づ ᘳ⨶ᨎ⨶ᘰ (⌐■_■) ಠ_ಠ yOu’Re FUckING 😊 LiviNGn't, kIddo.
# Bonus
Wait, I'm not that bad dude. So, there's another thing in cancerify - prettify.

# Prettify
Reverse the effect of cancerify. Pass the -x option and it will - 
1. Remove all unicode emojis.
2. Remove the lenny faces present. (only those which are known to the script)
3. Remove the cancerous fonts (only those which are known by the script)
4. Clear up consecutive spaces.
5. Add space after punctuations.
6. Fix the uppercase mess. This can be a little buggy. I've implemented a lot of cases (Uppercase on first letter, after period, question or exclamation, uppercase 'I' etc.) but of course there are more cases (e.g. Abbreviations, but not all, e.g. e.g.)
7. Replace the 'B' emojis with 'b'

Have fun!!
