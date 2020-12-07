boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) != len(girls):
    print('Предупреждение, что кто-то может остаться без пары!')
elif len(boys) > 0:
    boys = sorted(boys)
    girls = sorted(girls)
    pairs = zip(boys, girls)
    print('Идеальные пары:')
    for pair in pairs:
        print(pair[0], 'и', pair[1])