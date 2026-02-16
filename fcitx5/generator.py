from pathlib import Path
from configparser import ConfigParser
import tomllib
from dataclasses import dataclass

DATA_DIR = Path(__file__).parents[1] / "data"
FCITX_DIR = Path(__file__).parent

@dataclass
class CodeInfo:
    codes: dict[str, str]
    letters: list[str]
    max_len: int

def load_wordlist(path) -> dict[str, int]:
    result = {}
    with open(path) as file:
        for line in file:
            [nanpa, nimi] = line.strip().split()
            result[nimi.lower()] = chr(int(nanpa, base=16))
    return result

def load_codes(path, wordlist, prefix="") -> CodeInfo:
    result = {}

    parser = None
    with open(path, "rb") as file:
        parser = tomllib.load(file)

    letters = set()
    max_len = 0

    for (lawa, poki) in parser.items():
        # print(f"{lawa} -> {poki}")
        for (anpa, nimi) in poki.items():
            code = f"{prefix}{lawa}{anpa}"

            max_len = max(max_len, len(code))
            letters.update(code)
            result[code] = wordlist[nimi]
    
    letters = list(letters)
    letters.sort()

    return CodeInfo(codes=result, letters=letters, max_len=max_len)

def write_table(path, info: CodeInfo):
    with open(path, "w") as f:
        f.write(f"""\
Length={info.max_len}
Code=abcdefghijklmnopqrstuvwxyz

[Data]
""")
        for (code, char) in info.codes.items():
            f.write(f"{code}\t{char}\n")
    pass

wordlist = load_wordlist(DATA_DIR / "wordlist-2026.txt")
code_info = load_codes(DATA_DIR / "linku-common.toml", wordlist)
write_table(FCITX_DIR/"table/nasin-poki.txt", code_info)
