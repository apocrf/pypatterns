import abc
import uuid


class AbstractUser(abc.ABC):
    @abc.abstractmethod
    def create(self) -> None:
        pass


class User(AbstractUser):
    """Обычный пользователь"""

    def create(self) -> None:
        print(f"User - {uuid.uuid4()} created")


class BusinessAdministrator(AbstractUser):
    """Пользователь Бизнес-администратор"""

    def create(self) -> None:
        print(f"Business Admin - {uuid.uuid4()} created")


class Administrator(AbstractUser):
    """Администратор"""

    def create(self) -> None:
        print(f"Admin - {uuid.uuid4()} created")


class UserFactory:
    @classmethod
    def create(cls, user_group: str) -> AbstractUser:
        """Создание пользователя

        Args:
            user_group (str): группа пользователя

        Raises:
            ValueError: Ошибка если группа пользователя не определена

        Returns:
            AbstractUser: экземпляр класса AbstractUser
        """
        user_groups = {
            "User": User,
            "BusinessAdministrator": BusinessAdministrator,
            "Administrator": Administrator,
        }
        try:
            return user_groups[user_group]()
        except KeyError:
            raise ValueError(f"Unknown user group: {user_group}")


user = UserFactory.create("BusinessAdministrator")
user.create()
