# nasin poki, a new input method for *sitelen pona*
There really aren't that many words in toki pona, but it is more than a few. Trying to assign [one key per letter](https://sona.pona.la/wiki/Sitelen_Pona_Keyboard_Layout) with two modifier keys is limited to 188 characters, and can get very messy and difficult to remember. Using a [shape-decomposition](https://sona.pona.la/wiki/Wakalito) system works well on mobile phones where space is at a premium, but becomes a bit cumbersome on desktop.

This IME assigns *two*-letter combinations to each word. The first letter corresponds to 1 of 24 *categories* (in toki pona: *poki*), and the second letter selects a particular word, either the first letter of that word, or a different letter if not the first.

## poki ale (the categories)
Categories were laid out on the keyboard according to their frequency in [ilo Muni](https://github.com/gregdan3/ilo-muni) as of Oct. 2025: the more frequent categories lie on the home row, the less frequent categories are above and below. This table is mainly a summary of the categories, see the [data](https://github.com/jgcodes2020/nasin-poki/tree/main/data) folder for individual combinations. 

| **key** | **description** | **words** |
|:--:|--|--|
| **q** | animals | soweli, kijetesantakalu, waso, kala, akesi, pipi |
| **w** | body parts | lawa, lukin, kute, uta, luka, sijelo, noka |
| **e** | actions of living beings | alasa, moli, lape, mu, pakala, kipisi |
| **r** | abstract things | ijo, tenpo, open, pini, sin, poki |
| **t** | materials | kiwen, telo, ko, kon, ma |
| **y** | human relationships | mama, kulupu, utala, pana, jo |
| **u** | technology | ilo, tomo, supa, len, wawa, misikeke |
| **i** | shape, size | palisa, linja, leko, sike, lili, suli |
| **o** | sensations, the sky | kalama, suno, seli, lete, mun |
| **p** | food, agriculture | moku, kasi, kili, pan, soko, namako |
| **a** | people, society | jan, musi, mani, esun, pali |
| **s** | emotions, feelings | pilin, pona, ike, suwi, jaki, nasa, monsuta |
| **d** | speech and lore | sona, toki, lipu, sitelen, nimi, nasin |
| **f** | pronouns | mi, sina, ona, ni |
| **g** | word-like particles | a, n, o, kin, seme |
| **h** | location | lon, ala, tawa, tan, awen, kama |
| **j** | sentence particles | li, e, en, anu, pi, la |
| **k** | change and ability | ante, sama, wile, ken, kepeken |
| **l** | quantity | nanpa, wan, tu, mute, ale, taso |
| **z** | PREFIX: rare | \[reserved\] |
| **x** | PREFIX: uncommon | \[reserved\] |
| **c** | works by mama Sonja | pu, ku, su |
| **v** | directions | sinpin, monsi, sewi, anpa, poka |
| **b** | sexuality, gender | unpa, olin, meli, mije, tonsi |
| **n** | colours | kule, loje, jelo, laso, pimeja, walo |
| **m** | layers, surfaces | lupa, nena, insa, selo, weka |

Less frequent words (in particular, those added in the most recent UCSUR draft), are inputted using 3-letter combinations.

## nasin lipu (organization)
- **design**: scripts and other planning documents used for planning categories out
- **data**: raw TOML files with the categories and punctuation mapping
- **fcitx5**: A Fcitx5 plugin using the tables in *data/*.

I am open to adding other support for other IME engines, though I will not be able to help maintain them.

## ken sina lon lipu mi (licensing)
GPLv3.