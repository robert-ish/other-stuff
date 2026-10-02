import re


def estimate_syllables(word):
    word = word.lower()

    # groups of vowel sounds
    groups = re.findall(r"[aeiouy]+", word)
    count = len(groups)

    # rough silent-e rule
    if (
        word.endswith("e")
        and not word.endswith(("le", "ye"))
        and count > 1
    ):
        count -= 1

    return max(1, count)


INPUT_FILE = "words.txt"
OUTPUT_FILE = "candidates.txt"

candidates = []

with open(INPUT_FILE, "r", encoding="utf-8") as file:
    for line in file:
        word = line.strip().lower()


        if not word.startswith("p"):
            continue

        if len(word) > 10:
            continue

        syllables = estimate_syllables(word)

        if syllables >= 3:
            continue

        candidates.append((word, len(word), syllables))


# sort shortest first, then alphabetically
candidates.sort(key=lambda x: (x[1], x[0]))


with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
    for word, length, syllables in candidates:
        file.write(
            f"{word}\n"
        )


print(f"Found {len(candidates)} candidates.")
print(f"Saved to {OUTPUT_FILE}")

print("\nFirst 50:")
for word, length, syllables in candidates[:50]:
    print(f"{word:<12} {length} letters, {syllables} syllables")
