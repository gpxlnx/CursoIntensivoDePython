favorite_languages = {
    'jen': 'Python',
    'sarah': 'C',
    'edward': 'Ruby',
    'phil': 'Python'
}

print(f'\nThe following languages have been mentioned.\n')

for language in set(favorite_languages.values()):
    print(f'{language.title()}')
