


def get_cats_info(path):
    
    cats_info = []

    with open(path, 'r') as file:
        data = file.read()

    for line in data.strip().split('\n'):

        id, name, age = line.split(',')

        cats_info.append(
            {
                'id': id,
                'name': name,
                'age': age,
            }
        )

    return cats_info



def main():
    cast_info = get_cats_info(path=r'D:\PyCharmProjects\goit-pycore-hw-04\Task2\cats_info.txt')
    print(cast_info)



if __name__ == "__main__":
    main()