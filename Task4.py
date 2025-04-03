class Car:
    """
    Класс, представляющий автомобиль.
    """
    wheels: int = 4  # Колёса (атр. класса)
    default_color: str = "Белый" # цвет по дефолту (атр. класса)

    def __init__(self, model: str, year: int, color: str = default_color) -> None:
        """
        Инициализирует новый объект автомобиля.
        В аргументы передаётся модель, цвет, и дату выпуска
        """
        self.model = model
        self.year = year
        self.color = color
        self.is_engine_on = False
        self.current_speed = 0

    def start_engine(self) -> None:
        """
        Заводим двигатель
        """
        if not self.is_engine_on:
            self.is_engine_on = True
            print("Двигатель запущен.")
        else:
            print("Двигатель уже работает.")

    def stop_engine(self) -> None:
        """
        Глушим мотор
        """
        if self.is_engine_on:
            self.is_engine_on = False
            self.current_speed = 0
            print("Двигатель остановлен")
        else:
            print("Двигатель уже остановлен.")

    def accelerate(self, speed_increase: int) -> None:
        """
       Набираем скоость
        Аргумент: speed_increase - на сколько увеличить скорость?
        """
        if self.is_engine_on:
            self.current_speed += speed_increase
            print(f"Скорость увеличена до {self.current_speed} км/ч.")
        else:
            print("Двигатель нужно запустить!")

    def brake(self, speed_decrease: int) -> None:
        """
        Остановка авто, т.е. снижается у нас скорость
        Аргумент speed_decrease: на сколько уменьшить скорость
        """
        if self.is_engine_on:
            self.current_speed -= speed_decrease
            if self.current_speed < 0:
                self.current_speed = 0
            print(f"Скорость уменьшена до {self.current_speed} км/ч.")
        else:
            print("Ты и так на месте стоишь дядь, двигатель заглушен.")

    def __str__(self) -> str:
        """
        Вывод параметр авто. В аргументе цвет, модель, год
        """
        return f"{self.year} {self.model} ({self.color})"

    def __eq__(self, other: object) -> bool:
        """
        Сравнение автомобиля с другим. Аргумент - другой авто по тем параметрам, что ниже указано
        Аргумент - правдой будет, если авто равны сами по хар-кам, false в ином. По дефолту у нас гранта будет белой
        """
        if not isinstance(other, Car):
            return False
        return (self.model == other.model and
                self.year == other.year and
                self.color == other.color)
car1 = Car("Тойота Камри", 2020, "Матово-розовый")
car2 = Car("Бумер E34", 2022, "Чёрная как ночь")
car3 = Car("Камаз", 2020, "Оранжевый(рыжий)")
car4 = Car("Lada Iskra V16", 2025)
print(car1)
print(car4)

car1.start_engine()
car1.accelerate(50)
car1.brake(20)
car1.stop_engine()

print(car1 == car2)
print(car1 == car3)