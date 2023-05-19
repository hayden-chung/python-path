from pathlib import Path 

# Creat a Path object from a string 
# path = Path('C:/Users/hayde/OneDrive - KingsWay School/CodeBricks')

# if path.exists():
#     print('Path exists')
# else: 
#     print('Path does not exist ')

# folder = Path('C:/Users/hayde/OneDrive - KingsWay School/CodeBricks/new_folder')
# if not folder.exists():


folder = Path('C:/Users/hayde/Documents')

# for file in folder.iterdir():
#     print(file.name)

path = Path('C:/Users/hayde/Documents')

for path in folder.iterdir():
    if path.is_file():
        print(f'{path} is a file')
    elif path.is_dir():
        print(f'{path} is a directory')
    else:
        print(f'{path} does not exist')

# Create a Path object from a variable 
# folder = 'C:/Users/Username/Documents'
# filename = 'my_file.txt'
# path = Path(folder) / filename

# # Checking if a path exists:
# path = Path('C:/Users/Username/Documents/my_file.txt')

