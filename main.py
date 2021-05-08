from deque import Deque, DequeException


def main() -> None:
    """Формат ввода.

    В первой строке записано количество команд n — целое число, не превосходящее 5000. Во второй строке записано
    число m — максимальный размер дека. Он не превосходит 1000. В следующих n строках записана одна из команд:

    * push_back(value) – добавить элемент в конец дека. Если в деке уже находится максимальное число элементов,
      вывести «error».
    * push_front(value) – добавить элемент в начало дека. Если в деке уже находится максимальное число элементов,
      вывести «error».
    * pop_front() – вывести первый элемент дека и удалить его. Если дек был пуст, то вывести «error».
    * pop_back() – вывести последний элемент дека и удалить его. Если дек был пуст, то вывести «error».
    * Value — целое число, по модулю не превосходящее 1000.
    """
    try:
        command_count, deque_size = int(input()), int(input())
        d = Deque(deque_size)
        for _ in range(command_count):
            current_command, _, numb = input().partition(' ')
            try:
                if numb:
                    getattr(d, current_command)(numb)
                else:
                    print(getattr(d, current_command)())
            except DequeException as e:
                print(f"Can't execute {current_command}: {e}")
            except AttributeError:
                print(f"{current_command} isn't the support command")

    except ValueError as e:
        print(f"Can't convert to number\n{e}")


if __name__ == '__main__':
    main()
