#!/usr/bin/env python3

import argparse
import random

onsets = [
  "b",
  "c",
  "d",
  "f",
  "g",
  "h",
  "j",
  "k",
  "l",
  "m",
  "n",
  "p",
  "r",
  "s",
  "t",
  "v",
  "w",
  "pl",
  "bl",
  "kl",
  "ɡl",
  "pr",
  "br",
  "tr",
  "dr",
  "kr",
  "ɡr",
  "tw",
  "dw",
  "ɡw",
  "kw",
  "pw",
  "fl",
  "sl",
  "dʒ",
  "θl",
  "fr",
  "θr",
  "ʃr",
  "hw",
  "sw",
  "θw",
  "vw",
  "pj",
  "bj",
  "tj",
  "dj",
  "kj",
  "ɡj",
  "mj",
  "nj",
  "fj",
  "vj",
  "θj",
  "sj",
  "zj",
  "hj",
  "lj",
  "sp",
  "st",
  "sk",
  "sm",
  "sn",
  "sf",
  "sθ",
  "spl",
  "skl",
  "spr",
  "str",
  "skr",
  "skw",
  "smj",
  "spj",
  "stj",
  "skj",
  "sfr",
]

nuclei = [
  "a",
  "e",
  "i",
  "o",
  "u",
  "oo",
  "ui",
  "oi",
  "ai",
  "ae",
  "ee",
  "ei",
  "ie",
]

codas = [
  "b",
  "c",
  "d",
  "f",
  "g",
  "k",
  "l",
  "m",
  "n",
  "p",
  "r",
  "s",
  "t",
  "v",
  "ŋ",
  "lp",
  "lb",
  "lt",
  "ld",
  "ltʃ",
  "ldʒ",
  "lk",
  "rp",
  "rb",
  "rt",
  "rd",
  "rtʃ",
  "rdʒ",
  "rk",
  "rɡ",
  "lf",
  "lv",
  "lθ",
  "ls",
  "lʃ",
  "rf",
  "rv",
  "rθ",
  "rs",
  "rz",
  "rʃ",
  "lm",
  "ln",
  "rm",
  "rn",
  "rl",
  "mp",
  "nt",
  "nd",
  "ntʃ",
  "ndʒ",
  "ŋk",
  "mf",
  "mθ",
  "nθ",
  "ns",
  "nz",
  "ŋθ",
  "ft",
  "sp",
  "st",
  "sk",
  "fθ",
  "pt",
  "kt",
  "pθ",
  "ps",
  "tθ",
  "ts",
  "dθ",
  "ks",
  "lpt",
  "lps",
  "lfθ",
  "lts",
  "lst",
  "lkt",
  "lks",
  "rmθ",
  "rpt",
  "rps",
  "rts",
  "rst",
  "rkt",
  "mpt",
  "mps",
  "ndθ",
  "ŋkt",
  "ŋks",
  "ŋkθ",
  "ksθ",
  "kst",
]

def gen_syllable(prob_onset=0.6, prob_coda=0.8):
  has_onset = random.random() < prob_onset
  onset = random.choice(onsets) if has_onset else ""
  has_coda = random.random() < prob_coda
  coda = random.choice(codas) if has_coda else ""
  nucleus = random.choice(nuclei)
  print((onset, nucleus, coda))
  return onset+nucleus+coda
  

def pick_probs(word_so_far, num_syllables):
  # longer words get shorter syllables
  # if the previous syllable of the word had no coda, this syllable must have an onset
  # so we don't get a pile of adjacent vowel sounds
  prob_onset = prob_coda = 1.2 / (1+num_syllables)
  if word_so_far and word_so_far[-1] in ['a','e','i','o','u']:
    prob_onset = 1.0
  return (prob_onset, prob_coda)

def gen_word():
  num_syllables = random.choice([1,1,1,1,2,2,3])
  outword = ""
  for _ in range(num_syllables):
    (prob_onset, prob_coda) = pick_probs(outword, num_syllables)
    outword += gen_syllable(prob_onset=prob_onset, prob_coda=prob_coda)
  return outword
  

def main():
  parser = argparse.ArgumentParser(description="Generate 'words' using english phonotactics")
  parser.add_argument("-n","--num_words", default=5, help="Number of 'words' to generate")
  args = parser.parse_args()
  for _ in range(args.num_words):
    print(gen_word())


if __name__ == "__main__":
  main()
