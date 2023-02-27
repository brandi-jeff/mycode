import crayons

print(crayons.red('red string'))

# Red White and Blue text
print(f"{crayons.red('red')} white {crayons.blue('blue')}")  # f-string (newest version of str templating)

crayons.disable() # disables the crayons package

#crayons is disabled shouldn't have colors
print(f"{crayons.red('red')} white {crayons.blue('blue')}") 

crayons.DISABLE_COLOR = False # enable the crayons package

#color is enabled so color will show
print(f"{crayons.red('red')} white {crayons.blue('blue')}") 

print(crayons.red('red string', bold=True))

print(crayons.yellow('yellow string', bold=True))

print(crayons.magenta('magenta string', bold=True))

print(crayons.white('white string', bold=True))

