word = input("Enter a word: ")

vowels = "aeiouy"
syllable_count = 0
previous_char_vowel = False

for char in word.lower():
    if char in vowels:
        if not previous_char_vowel:
            syllable_count += 1
        previous_char_vowel = True
    else:
        previous_char_vowel = False

if word.lower().endswith("e") and syllable_count > 1:
    syllable_count -= 1

if syllable_count == 0:
    syllable_count = 1

print("Syllables:", syllable_count)