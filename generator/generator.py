
consonants = {
    "-": "1l",
    "=": "2l",
    "Ξ": "3l",
    "|": "j1",
    "+": "ad",
    "Ʇ": "tt",
    "T": "ct",
    "ʌ": "uu",
    "v": "dd",
    "<": "ll",
    ">": "rr",
    "L": "cl",
    "N": "cn",
    "𐋇": "ua",
    "Y": "cy",
    "𐋁": "1x",
}

vowels = {
    "S": "cs",
    "J": "cj",
    "2": "j2",
    "r": "sr",
    "h": "sh",
    "3": "j3",
    "t": "st",
    "y": "sy",
    "O": "co",
    "6": "j6",
    "d": "sd",
    "D": "cd",
    "e": "se",
    "ɤ": "rh",
    "ɸ": "fi",
    "8": "j8",
}

punctuations = {
    "(": "lp",
    ")": "rp",
}


def generate_fonts(template: str, dest: str, *args):
    with open(template) as f:
        generated = f.read()
    for arg in args:
        if arg == "<":
            arg = "&lt;"
        elif arg == ">":
            arg = "&gt;"
        generated = generated.replace("▢", arg, 1)
    with open(dest, "w") as f:
        f.write(generated)


def generate_words(dest: str):
    with open(dest, "w"):
        pass


def generate_phrases(dest: str):
    with open(dest, "w"):
        pass


def generate_syllables(dest: str, permutation):
    with open(dest, "w") as f:
        for ((c, cname), (v, vname)) in permutation:
            f.write(f"# {cname}{vname}\n\n")
            f.write(f"![{cname}{vname}](fonts/{cname}{vname}.svg)\n\n")
            f.write(f"🔊 \n\n")


def generate_raticals(dest: str, permutation):
    with open(dest, "w") as f:
        for ((c, cname), (v, vname)) in permutation:
            f.write(f"# {cname}{vname}\n\n")
            f.write(f"![{cname}{vname}](../fonts/{cname}{vname}.svg)\n\n")
            f.write(f"[🔊](syllables.md#{cname}{vname})\n\n")


chars = consonants | vowels
permutation = [(c, v) for c in consonants.items() for v in vowels.items()]

for (k, v) in chars.items():
    generate_fonts("./font_templates/1234.svg", f"../fonts/{v}.svg", k)

for ((c, cname), (v, vname)) in permutation:
    generate_fonts("./font_templates/12-34.svg",
                   f"../fonts/{cname}{vname}.svg", c, v)
    generate_words(f"../words/{cname}{vname}.md")
    generate_phrases(f"../phrases/{cname}{vname}.md")

generate_syllables("../syllables.md", permutation)
generate_raticals("../words/radicals.md", permutation)
