#!/usr/bin/env python3
from pathlib import Path
from configparser import ConfigParser
import tomllib
from dataclasses import dataclass

DATA_DIR = Path(__file__).parents[1] / "data"
FCITX_DIR = Path(__file__).parent

@dataclass
class CodeInfo:
    codes: dict[str, str]
    letters: set[str]
    max_len: int

    def merge(self, other: CodeInfo):
        self.codes.update(other.codes)
        self.letters.update(other.letters)
        self.max_len = max(self.max_len, other.max_len)


def load_wordlist(path) -> dict[str, int]:
    result = {}
    with open(path) as file:
        for line in file:
            [nanpa, nimi] = line.strip().split()
            result[nimi.lower()] = chr(int(nanpa, base=16))
    return result

def load_punct(path) -> dict[str, str]:
    data = None
    with open(path, "rb") as file:
        data = tomllib.load(file)
    return data


def load_codes(path, wordlist, prefix="") -> CodeInfo:
    result = {}

    data = None
    with open(path, "rb") as file:
        data = tomllib.load(file)

    letters = set()
    max_len = 0

    for (lawa, poki) in data.items():
        # print(f"{lawa} -> {poki}")
        for (anpa, nimi) in poki.items():
            code = f"{prefix}{lawa}{anpa}"

            max_len = max(max_len, len(code))
            letters.update(code)
            result[code] = wordlist[nimi]
    
    letters = list(letters)
    letters.sort()

    return CodeInfo(codes=result, letters=letters, max_len=max_len)

def write_table(path, info: CodeInfo, punct: dict[str, str]):
    with open(path, "w") as f:
        f.write(f"""\
Length={info.max_len}
KeyCode={"".join(sorted(info.letters))}
[Data]
""")
        
        for (code, char) in info.codes.items():
            f.write(f"{code} {char}\n")
        for (code, char) in punct.items():
            f.write(f"{code} {char}\n")

    pass

wordlist = load_wordlist(DATA_DIR / "wordlist-2026.txt")
code_info = load_codes(DATA_DIR / "linku-common.toml", wordlist)
punct = load_punct(DATA_DIR / "punct.toml")
write_table(FCITX_DIR/"nasin-poki.txt", code_info, punct)
