
class Char:
    def __init__(self) -> None:
        self.char = ""
        self.name = ""
        self.phoneme = ""
        self.syllable = ""


c1l = Char()
c1l.char = "-"
c1l.name = "1l"
c1l.phoneme = "m"
c1l.syllable = "ma"

c2l = Char()
c2l.char = "="
c2l.name = "2l"
c2l.phoneme = "k"
c2l.syllable = "ka"

c3l = Char()
c3l.char = "Ξ"
c3l.name = "3l"
c3l.phoneme = "j"
c3l.syllable = "ja"

cj1 = Char()
cj1.char = "|"
cj1.name = "j1"
cj1.phoneme = "p"
cj1.syllable = "pa"

cad = Char()
cad.char = "+"
cad.name = "ad"
cad.phoneme = "w"
cad.syllable = "wa"

ctt = Char()
ctt.char = "Ʇ"
ctt.name = "tt"
ctt.phoneme = "n"
ctt.syllable = "na"

cct = Char()
cct.char = "T"
cct.name = "ct"
cct.phoneme = "t"
cct.syllable = "ta"

cuu = Char()
cuu.char = "ʌ"
cuu.name = "uu"
cuu.phoneme = "l"
cuu.syllable = "la"

cdd = Char()
cdd.char = "v"
cdd.name = "dd"
cdd.phoneme = "s"
cdd.syllable = "sa"

cll = Char()
cll.char = "<"
cll.name = "ll"
cll.phoneme = "b"
cll.syllable = "ba"

crr = Char()
crr.char = ">"
crr.name = "rr"
crr.phoneme = "g"
crr.syllable = "ga"

ccl = Char()
ccl.char = "L"
ccl.name = "cl"
ccl.phoneme = "h"
ccl.syllable = "ha"

ccn = Char()
ccn.char = "N"
ccn.name = "cn"
ccn.phoneme = "d"
ccn.syllable = "da"

cua = Char()
cua.char = "𐋇"
cua.name = "ua"
cua.phoneme = "r"
cua.syllable = "ra"

ccy = Char()
ccy.char = "Y"
ccy.name = "cy"
ccy.phoneme = "f"
ccy.syllable = "fa"

c1x = Char()
c1x.char = "𐋁"
c1x.name = "1x"
c1x.phoneme = "tʃ"
c1x.syllable = "tʃa"

consonants = [c1l, c2l, c3l, cj1, cad, ctt, cct, cuu,
              cdd, cll, crr, ccl, ccn, cua, ccy, c1x]

ccs = Char()
ccs.char = "S"
ccs.name = "cs"
ccs.phoneme = "a"
ccs.syllable = "a"

ccj = Char()
ccj.char = "J"
ccj.name = "cj"
ccj.phoneme = "i"
ccj.syllable = "i"

cj2 = Char()
cj2.char = "2"
cj2.name = "j2"
cj2.phoneme = "u"
cj2.syllable = "u"

csr = Char()
csr.char = "r"
csr.name = "sr"
csr.phoneme = "ɔ"
csr.syllable = "ɔ"

csh = Char()
csh.char = "h"
csh.name = "sh"
csh.phoneme = "e"
csh.syllable = "e"

cj3 = Char()
cj3.char = "3"
cj3.name = "j3"
cj3.phoneme = "o"
cj3.syllable = "o"

cst = Char()
cst.char = "t"
cst.name = "st"
cst.phoneme = "ə"
cst.syllable = "ə"

csy = Char()
csy.char = "y"
csy.name = "sy"
csy.phoneme = "y"
csy.syllable = "y"

cco = Char()
cco.char = "O"
cco.name = "co"
cco.phoneme = "ai"
cco.syllable = "ai"

cj6 = Char()
cj6.char = "6"
cj6.name = "j6"
cj6.phoneme = "iu"
cj6.syllable = "iu"

csd = Char()
csd.char = "d"
csd.name = "sd"
csd.phoneme = "ua"
csd.syllable = "ua"

ccd = Char()
ccd.char = "D"
ccd.name = "cd"
ccd.phoneme = "au"
ccd.syllable = "au"

cse = Char()
cse.char = "e"
cse.name = "se"
cse.phoneme = "ui"
cse.syllable = "ui"

crh = Char()
crh.char = "ɤ"
crh.name = "rh"
crh.phoneme = "ia"
crh.syllable = "ia"

cfi = Char()
cfi.char = "ɸ"
cfi.name = "fi"
cfi.phoneme = "io"
cfi.syllable = "io"

cj8 = Char()
cj8.char = "8"
cj8.name = "j8"
cj8.phoneme = "oi"
cj8.syllable = "oi"

vowels = [ccs, ccj, cj2, csr, csh, cj3, cst, csy,
          cco, cj6, csd, ccd, cse, crh, cfi, cj8]

clp = Char()
clp.char = "("
clp.name = "lp"
clp.phoneme = ""
clp.syllable = ""

crp = Char()
crp.char = ")"
crp.name = "rp"
crp.phoneme = ""
crp.syllable = ""

punctuations = [clp, crp]

chars = consonants + vowels

cv_permutations = [[c, v] for c in consonants for v in vowels]


def generate_fonts(template: str, args: list[list[Char]]):
    with open(template) as f:
        template_svg = f.read()
    for arg in args:
        name = ""
        generated = template_svg
        for char in arg:
            escaped = char.char
            if escaped == "<":
                escaped = "&lt;"
            elif escaped == ">":
                escaped = "&gt;"
            generated = generated.replace("▢", escaped, 1)
            name += char.name
        with open(f"../fonts/{name}.svg", "w") as f:
            f.write(generated)


def generate_words(args: list[list[Char]]):
    for arg in args:
        dest = ""
        for char in arg:
            dest += char.name
        with open(f"../words/{dest}.md", "w"):
            pass


def generate_phrases(args: list[list[Char]]):
    for arg in args:
        dest = ""
        for char in arg:
            dest += char.name
        with open(f"../phrases/{dest}.md", "w"):
            pass


def generate_syllables(syllables: list[list[Char]]):
    with open("../syllables.md", "w") as f:
        for syllable in syllables:
            name = ""
            s = ""
            for char in syllable:
                name += char.name
                s += char.phoneme
            f.write(f"# {name}\n\n")
            f.write(f"![{name}](fonts/{name}.svg)\n\n")
            f.write(f"🔊 /{s}/\n\n")


def generate_raticals(args: list[list[Char]]):
    with open("../words/radicals.md", "w") as f:
        for arg in args:
            cname = arg[0].name
            vname = arg[1].name
            f.write(f"# {cname}{vname}\n\n")
            f.write(f"![{cname}{vname}](../fonts/{cname}{vname}.svg)\n\n")
            f.write(f"[🔊](../syllables.md#{cname}{vname})\n\n")


generate_fonts("./font_templates/1234.svg", [[c] for c in chars])
generate_fonts("./font_templates/12-34.svg", cv_permutations)
generate_words(cv_permutations)
generate_phrases(cv_permutations)
generate_syllables([[c] for c in vowels] + cv_permutations)
generate_raticals(cv_permutations)
