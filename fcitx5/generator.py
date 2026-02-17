#!/usr/bin/env python3
from pathlib import Path
from configparser import ConfigParser
import tomllib
import json
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


def load_punct(path) -> CodeInfo:
    data = None
    with open(path, "rb") as file:
        data = tomllib.load(file)

    letters = set()
    max_len = 0
    for key in data.keys():
        letters.update(key)
        max_len = max(max_len, len(key))

    return CodeInfo(codes=data, letters=letters, max_len=max_len)



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

    return CodeInfo(codes=result, letters=letters, max_len=max_len)


def write_table(path, info: CodeInfo):
    with open(path, "w") as file:
        json.dump({
            "key_code": "".join(sorted(info.letters)),
            "length": info.max_len,
            "data": info.codes
        }, file, indent=2)


wordlist = load_wordlist(DATA_DIR / "wordlist-2026.txt")

code_info = load_codes(DATA_DIR / "linku-common.toml", wordlist)
code_info.merge(load_codes(DATA_DIR / "linku-rare-trimmed.toml", wordlist, "x"))
code_info.merge(load_punct(DATA_DIR / "punct.toml"))

write_table(FCITX_DIR/"nasin-poki.json", code_info)
