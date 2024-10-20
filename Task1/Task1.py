


def total_salary(path):
    total = 0
    workers = 0
    
    with open(path, 'r') as file:
        data = file.read()
    
    for line in data.strip().split('\n'):

        name, salary = line.split(',')

        total += int(salary)
        workers += 1

    average = total / workers

    return total, average




def main():
 
    total, average = total_salary(r'D:\PyCharmProjects\goit-pycore-hw-04\Task1\total_salary.txt')

    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

if __name__ == "__main__":
    main()