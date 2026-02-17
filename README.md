# nasin poki, a new input method for *sitelen pona*
There really aren't that many words in toki pona, but it is more than a few. Trying to assign [one key per letter](https://sona.pona.la/wiki/Sitelen_Pona_Keyboard_Layout) with two modifier keys is limited to 188 characters, and can get very messy and difficult to remember. Using a [shape-decomposition](https://sona.pona.la/wiki/Wakalito) system works well on mobile phones where space is at a premium, but becomes a bit cumbersome on desktop.

This IME assigns *two*-letter combinations to each word. The first letter corresponds to 1 of 24 *categories* (in toki pona: *poki*), and the second letter selects a particular word, either the first letter of that word, or a different letter if not the first.

## nasin lipu (organization)
- **design**: scripts and other planning documents used for planning categories out
- **data**: raw TOML files with the categories and punctuation mapping
- **fcitx5**: A Fcitx5 plugin using the tables in *data/*.

I am open to adding other support for other IME engines, though I will not be able to help maintain them.

## ken sina lon lipu mi (licensing)
GPLv3.