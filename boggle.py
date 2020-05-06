"""
Boggle game

Find words with 3 more letters, you can go in all 8 directions 
but you cannot repeat the same position

This solution finds random sequences of length n and checks
if the word is in the dictionary
"""

import numpy as np

np.random.seed(33)

abc = 'abcdefghijklmnopqrstuvwxyz'
assert len(abc) == 26

# a slighly better abc with more vowels and no q or vwxyz
abc = 'aabcdeefghiijklmnooprstuu'

def new_boggle():
  # global abc
  return np.random.choice([i for i in abc], 16, replace=False).reshape(4, 4)

print(new_boggle())

# read in the word file

f1 = open('google-10000-english.txt', 'r')

words = []

for line in f1:
  word = line.strip()
  if len(word) >= 3:
    words.append(word)

print(len(words))

def is_word(word):
  return word in words

print(is_word('shoe'))

def coord_to_word(coords):
  # translate coords into a word
  return ''.join([boggle[i, j] for (i, j) in coords])

boggle = new_boggle()
coords = [(1, 1), (2, 2), (3, 3)]
print(coord_to_word(coords))

def gen_coords(n=3):
  coords = [(np.random.choice(4, 1)[0], np.random.choice(4, 1)[0])]
  last = coords[-1]
  for _ in range(1, n):
    tries = 0
    # avoid it getting stuck
    while tries < 100:
      newx = last[0] + np.random.choice([-1, 1], 1)[0]
      newy = last[1] + np.random.choice([-1, 1], 1)[0]
      tries += 1
      if 0 <= newx < 4 and 0 <= newy < 4 and (newx, newy) not in coords:
        tries = 100
        coords.append((newx, newy))
        last = coords[-1]
  # recursive if it got stuck
  if len(coords) < n:
    coords = gen_coords(n)
  return coords

print(gen_coords(4))

print(boggle)

for n in range(3, 7):
  print("==========", n, "==========")
  for _ in range(1000):
    coords = gen_coords(n)
    word = coord_to_word(coords)
    if is_word(word):
      print(word)

  