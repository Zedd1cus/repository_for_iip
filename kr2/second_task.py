from abc import ABC, abstractmethod


class NewsSystem:
    """Централизованная система наблюдения за новостями."""

    def __init__(self) -> None:
        self.__observers = set()

    # Подключить наблюдателя к системе новостей. (просто добавляем объект в списка).
    def attach(self, observer) -> None:
        self.__observers.add(observer)

    # Отключить наблюдателя от системы новостей. (просто удаляем объект из списка).
    def detach(self, observer) -> None:
        self.__observers.remove(observer)

    # Отправка уведомления\команды всем наблюдателям(камерам) о подписке пользователя на топик.
    # (Проходимся по списку объектов и вызываем нужный метод).
    def notify_subscribe(self) -> None:
        for observer in self.__observers:
            observer.subscribe()

    # Отправка уведомления\команды всем наблюдателям(камерам) о публикации новостей в топик.
    # (Проходимся по списку объектов и вызываем нужный метод).
    def notify_post_feed(self) -> None:
        for observer in self.__observers:
            observer.post_feed()


# Абстрактный класс наблюдателя.
# Косвенно указывает какие методы необходимо реализовать в его наследниках.
class AbstractObserver(ABC):
    @abstractmethod
    def create_topic(self, topic: str, feed_id: int) -> None:  # Абстрактный наблюдатель задает метод create_tipic
        pass

    @abstractmethod
    def subscribe(self) -> None:  # Абстрактный наблюдатель задает метод subscribe
        pass

    @abstractmethod
    def post_feed(self) -> None:  # Абстрактный наблюдатель задает метод post_feed
        pass


class News(AbstractObserver):
    """Наблюдения за новостями."""

    def __init__(self, user_id: int):
        self.user_id = user_id
        self.topic = None
        self.feed_id = None

    def create_topic(self, topic: str, feed_id: int) -> None:
        self.topic = topic
        self.feed_id = feed_id

    def subscribe(self) -> None:
        if self.verify_topic():
            print(f'Пользователь {self.user_id} подписался на новость "{self.feed_id}"')
        else:
            print(f'Пользователь {self.user_id} не подписался ни на одну новость')

    def post_feed(self) -> None:
        if self.verify_topic():
            print(f'Пользователь {self.user_id} получил новость "{self.feed_id}"')
        else:
            print(f'Пользователь {self.user_id} не получил ни одну новость')

    def verify_topic(self) -> bool:
        if self.topic == self.feed_id is None:
            return False
        else:
            return True


if __name__ == "__main__":
    user_1 = News(1)
    user_1.create_topic('Topic 1', 'feed_id 1')

    user_2 = News(2)
    user_2.create_topic('Topic 2', 'feed_id 2')

    user_3 = News(3)


    news_system = NewsSystem()

    news_system.attach(user_1)
    news_system.attach(user_2)
    news_system.attach(user_3)

    print('------------------------------------------------')

    news_system.notify_subscribe()

    print('------------------------------------------------')

    news_system.detach(user_2)

    news_system.notify_post_feed()

    print('------------------------------------------------')