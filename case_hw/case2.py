examination = {
    1:'Oh my Gosh (>ლ)\nSeriously!?\n\nYou ->\t○|￣|_ =3\n',
    2:'Hey, are you OK? I guess you are not in the mood today or my home work is so bad !?\n\n\t\tಠಿ_ಠ\n',
    3:'Okay, Not Problem.\n\n\t\t^______^\n',
    4:'Wow, I think you are so glad for my homework\n\n\t\to(〃＾▽＾〃)o\n',
    5:'Yahooo, Thank you dear\n\n\t\t\(@^0^@)/\n',
}

q = int(input('You must give a score between 1 and 5 for my homework -> '))
if q in range(1,6):
    print(examination[q].capitalize())
else:
    print('Errrror..............\n\n\t\t¯\_( ͡° ͜ʖ ͡°)_/¯\n')
