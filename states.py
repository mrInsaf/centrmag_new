from aiogram.fsm.state import State
from aiogram.fsm.state import StatesGroup


class StartState(StatesGroup):
    start_state = State()


class CreateAccount(StatesGroup):
    get_name_and_surname = State()
    get_email = State()
    get_phone = State()
    get_password = State()
    get_password_again = State()


class Login(StatesGroup):
    input_login = State()
    input_password = State()


class MakeOrder(StatesGroup):
    choose_product = State()
    choose_quantity = State()
    create_order = State()


class Logout(StatesGroup):
    confirm_logout = State()


class TrackOrder(StatesGroup):
    choose_order = State()
    track_order = State()


class Misc(StatesGroup):
    misc = State()