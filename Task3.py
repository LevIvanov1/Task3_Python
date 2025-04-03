def function_name(search: str, status: bool, *args: int, **kwargs: dict) -> list:
    """Функция обрабатывает аргументы на основе таких как search и status.
    Возвращает список, сформированный в соответствии с параметрами. Описание вот этих параметров:
        search: args или kwargs, определяет логику.
        status условие для обработки *args.
        *args представляет собой целые числа.
        **kwargs - это ключ-значение пары.
    """
    result: list = []
    result_2: str = ""

    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += f"{i}"
            return [result_2]
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += ("Key: {}, Value: {}; ".format(k, v))
        return [result_2]
    else:
        raise ValueError("Error for search")

