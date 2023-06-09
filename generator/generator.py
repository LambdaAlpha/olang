
class Char:
    def __init__(self) -> None:
        self.char = ""
        self.name = ""
        self.phoneme = ""
        self.syllable = ""


c1l = Char()
c1l.char = "-"
c1l.name = "1l"
c1l.phoneme = "k"
c1l.syllable = "ka"

c2l = Char()
c2l.char = "="
c2l.name = "2l"
c2l.phoneme = "g"
c2l.syllable = "ga"

c3l = Char()
c3l.char = "≡"
c3l.name = "3l"
c3l.phoneme = "p"
c3l.syllable = "pa"

cj1 = Char()
cj1.char = "|"
cj1.name = "j1"
cj1.phoneme = "b"
cj1.syllable = "ba"

ccl = Char()
ccl.char = "L"
ccl.name = "cl"
ccl.phoneme = "t"
ccl.syllable = "ta"

cad = Char()
cad.char = "+"
cad.name = "ad"
cad.phoneme = "d"
cad.syllable = "da"

ctt = Char()
ctt.char = "Ʇ"
ctt.name = "tt"
ctt.phoneme = "m"
ctt.syllable = "ma"

cct = Char()
cct.char = "T"
cct.name = "ct"
cct.phoneme = "n"
cct.syllable = "na"

cuu = Char()
cuu.char = "ʌ"
cuu.name = "uu"
cuu.phoneme = "h"
cuu.syllable = "ha"

cdd = Char()
cdd.char = "v"
cdd.name = "dd"
cdd.phoneme = "f"
cdd.syllable = "fa"

cll = Char()
cll.char = "<"
cll.name = "ll"
cll.phoneme = "l"
cll.syllable = "la"

crr = Char()
crr.char = ">"
crr.name = "rr"
crr.phoneme = "s"
crr.syllable = "sa"

ccn = Char()
ccn.char = "N"
ccn.name = "cn"
ccn.phoneme = "gl"
ccn.syllable = "gla"

ccy = Char()
ccy.char = "Y"
ccy.name = "cy"
ccy.phoneme = "bl"
ccy.syllable = "bla"

cua = Char()
cua.char = "𐋇"
cua.name = "ua"
cua.phoneme = "st"
cua.syllable = "sta"

c1x = Char()
c1x.char = "𐋁"
c1x.name = "1x"
c1x.phoneme = "sm"
c1x.syllable = "sma"

consonants = [c1l, c2l, c3l, cj1, ccl, cad, ctt, cct,
              cuu, cdd, cll, crr, ccn, ccy, cua, c1x]

ccs = Char()
ccs.char = "S"
ccs.name = "cs"
ccs.phoneme = "a"
ccs.syllable = "a"

ccj = Char()
ccj.char = "𝙹"
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
csh.phoneme = "o"
csh.syllable = "o"

cj3 = Char()
cj3.char = "3"
cj3.name = "j3"
cj3.phoneme = "ə"
cj3.syllable = "ə"

cst = Char()
cst.char = "t"
cst.name = "st"
cst.phoneme = "e"
cst.syllable = "e"

csy = Char()
csy.char = "𝗒"
csy.name = "sy"
csy.phoneme = "y"
csy.syllable = "y"

cco = Char()
cco.char = "O"
cco.name = "co"
cco.phoneme = "ia"
cco.syllable = "ia"

cj6 = Char()
cj6.char = "6"
cj6.name = "j6"
cj6.phoneme = "iu"
cj6.syllable = "iu"

csd = Char()
csd.char = "d"
csd.name = "sd"
csd.phoneme = "ie"
csd.syllable = "ie"

ccd = Char()
ccd.char = "D"
ccd.name = "cd"
ccd.phoneme = "ye"
ccd.syllable = "ye"

cse = Char()
cse.char = "e"
cse.name = "se"
cse.phoneme = "ua"
cse.syllable = "ua"

crh = Char()
crh.char = "ɤ"
crh.name = "rh"
crh.phoneme = "ui"
crh.syllable = "ui"

cfi = Char()
cfi.char = "𝜑"
cfi.name = "fi"
cfi.phoneme = "uo"
cfi.syllable = "io"

cj8 = Char()
cj8.char = "8"
cj8.name = "j8"
cj8.phoneme = "ai"
cj8.syllable = "ai"

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
