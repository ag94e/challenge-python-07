DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Mentor',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Mariandrea',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def homeless_key(worker):
    homeless = worker.copy()
    homeless['homeless'] = (homeless['organization'] == '')
    return homeless

def old_key(old_people):
    old = old_people.copy()
    old['old'] = (old['age'] >= 30)
    return old

def run():

    all_python_devs = filter(lambda value: value['language'] == 'python',DATA)

    all_Platzi_workers =  filter(lambda value: value['organization'] == 'Platzi', DATA)
    
    adults = filter(lambda value: value['age'] >= 18, DATA)

    workers = list(map(homeless_key, DATA))
    
    old_people = list(map(old_key, DATA))

    print('Python devs: ')
    for dev in all_python_devs:
        print('-', dev['name'])
    print('\n\n')

    print('Platzi workers: ')
    for worker in all_Platzi_workers:
        print('-', worker['name'])
    print('\n\n')

    print('Adults: ')
    for adult in adults:
        print('-', adult['name'])
    print('\n\n')

    print('Workers: ')
    print(workers)
    print('\n\n')

    print('Old People: ')
    print(old_people)
    print('\n\n')

    # # Remember: when possible, use lambdas


if __name__ == '__main__':
    run()
