from typing import List

def add_contact() -> None:
    """Добавляет новую запись в телефонный справочник."""
    with open('phonebook.txt', 'a') as file:
        last_name: str = input('Фамилия: ')
        first_name: str = input('Имя: ')
        middle_name: str = input('Отчество: ')
        organization: str = input('Организация: ')
        work_phone: str = input('Рабочий телефон: ')
        personal_phone: str = input('Личный телефон: ')
        file.write(f'{last_name} {first_name} {middle_name} {organization} {work_phone} {personal_phone}\n')


def edit_contact() -> None:
    """Редактирует существующую запись в телефонном справочнике."""
    personal_phone: str = input('Введите телефон для редактирования данных: ')
    new_data: List[str] = []
    with open('phonebook.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            contact_data = line.strip().split()
            if contact_data[4] == personal_phone:
                print('Текущие данные:')
                print("Фамилия:", contact_data[0])
                print("Имя:", contact_data[1])
                print("Отчество:", contact_data[2])
                print("Организация:", contact_data[3])
                print("Рабочий телефон:", contact_data[4])
                print("Личный телефон:", contact_data[5])
                new_last_name: str = input('новая фамилия: ')
                new_first_name: str = input('новое имя: ')
                new_middle_name: str = input('новое отчество: ')
                new_organization: str = input('новая организация: ')
                new_work_phone: str = input('новый рабочий телефон: ')
                new_personal_phone: str = input('новый личный телефон: ')
                new_data.append(
                    f'{new_last_name} {new_first_name} {new_middle_name} {new_organization} {new_work_phone} {new_personal_phone}\n')
                print('данные успешно обновлены')
            else:
                new_data.append(line)
    with open('phonebook.txt', 'w') as file:
        file.writelines(new_data)


def display_contacts() -> None:
    """Выводит контакты из телефонного справочника на экран постранично."""
    page_size: int = int(input("Введите количество записей на странице: "))
    page_number: int = int(input("Введите номер страницы: "))
    with open("phonebook.txt", "r") as file:
        lines = file.readlines()
        total_contacts = len(lines)
        start_idx = (page_number - 1) * page_size
        end_idx = start_idx + page_size
        for line in lines[start_idx:end_idx]:
            contact_data = line.strip().split()
            print("Фамилия:", contact_data[0])
            print("Имя:", contact_data[1])
            print("Отчество:", contact_data[2])
            print("Организация:", contact_data[3])
            print("Рабочий телефон:", contact_data[4])
            print("Личный телефон:", contact_data[5])
            print("--------------------")
        print(f"Всего записей: {total_contacts}")


def search_contact() -> None:
    """Поиск контактов по заданным критериям."""
    search_term: str = input("Введите строку для поиска: ")
    with open('phonebook.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            if search_term in line:
                contact_data = line.strip().split()
                print("Фамилия:", contact_data[0])
                print("Имя:", contact_data[1])
                print("Отчество:", contact_data[2])
                print("Организация:", contact_data[3])
                print("Рабочий телефон:", contact_data[4])
                print("Личный телефон:", contact_data[5])
                print("--------------------")


def main():
    """Основная функция для взаимодействия с телефонным справочником."""
    while True:
        print("1. Добавить контакт")
        print("2. Редактировать контакт")
        print("3. Поиск контактов")
        print("4. Вывести контакты")
        print("5. Выход")

        choice = int(input("Выберите действие: "))
        if choice == 1:
            add_contact()
        elif choice == 2:
            edit_contact()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            display_contacts()
        elif choice == 5:
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()
