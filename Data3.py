def find_vowels_1(data, vowels='aeiou'):
    # return the number of occurrences of each vowel in a string
    return [(v, data.count(v)) for v in vowels]

print(find_vowels_1('chfkg'))
print(find_vowels_1('knvswem'))
print(find_vowels_1('uheoz'))
print(find_vowels_1('dyntlfe'))
print(find_vowels_1('vlzuj'))
print(find_vowels_1('joxwbsj'))


