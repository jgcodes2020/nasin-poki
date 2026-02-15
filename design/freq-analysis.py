import sqlite3
import datetime

def load_categories(filename):
    res = {}
    with open(filename) as file:
        for line in file:
            [key, *words] = line.strip().split(" ")
            res[key] = words
    return res


def db_tuple(n: int) -> str:
    return "(" + ("?, " * n)[:-2] + ")"

def date_ts(year: int, month: int) -> int:
    return int(datetime.datetime(year=year, month=month, day=1).timestamp())


def compare_data(dbname, categories: dict[int, list[str]]):
    hit_pairs = []

    with sqlite3.connect(dbname) as db:
        for (key, words) in categories.items():
            words_tuple = db_tuple(len(words))
            ids_cursor = db.execute(
                f"SELECT id FROM term WHERE text IN {words_tuple}", tuple(words))
            ids = [row[0] for row in ids_cursor]

            ts_thresh = date_ts(2022, 1)
            hits_cursor = db.execute(f"""
            SELECT SUM(hits) FROM yearly WHERE term_id IN {words_tuple} AND day > ?
            """, tuple(ids + [ts_thresh]))

            hits_total = hits_cursor.fetchall()[0][0]
            hit_pairs.append((key, hits_total // len(words)))
    
    hit_pairs.sort(key=lambda x: x[1], reverse=True)
    return hit_pairs


categories = load_categories("categories.txt")
hit_pairs = compare_data("2025-10-20-trimmed.sqlite", categories)

# write sorted categories out
with open("categories-sorted.txt", "w") as file:
    for (c, _) in hit_pairs:
        file.write(f"{c} {' '.join(categories[c])}\n")
    
