# The screen's dictionary contains the objects of the models and controllers
# of the screens of the application.

from Model.login_screen import LoginScreenModel
from Controller.login_screen import LoginScreenController
from Model.sign_up_screen import SignUpScreenModel
from Controller.sign_up_screen import SignUpScreenController
from Model.home_screen import HomeScreenModel
from Controller.home_screen import HomeScreenController
from Model.item_detail_screen import ItemDetailScreenModel
from Controller.item_detail_screen import ItemDetailScreenController
from Model.checkout_screen import CheckoutScreenModel
from Controller.checkout_screen import CheckoutScreenController
from Model.categories_screen import CategoriesScreenModel
from Controller.categories_screen import CategoriesScreenController
from Model.my_account_screen import MyAccountScreenModel
from Controller.my_account_screen import MyAccountScreenController
from Model.order_complete_screen import OrderCompleteScreenModel
from Controller.order_complete_screen import OrderCompleteScreenController
from Model.order_history_screen import OrderHistoryScreenModel
from Controller.order_history_screen import OrderHistoryScreenController

screen = {
    'home screen': {
        'model': HomeScreenModel,
        'controller': HomeScreenController,
    },
    'sign up screen': {
        'model': SignUpScreenModel,
        'controller': SignUpScreenController,
    },
    'checkout screen': {
        'model': CheckoutScreenModel,
        'controller': CheckoutScreenController,
    },
    'categories screen': {
        'model': CategoriesScreenModel,
        'controller': CategoriesScreenController,
    },
    'login screen': {
        'model': LoginScreenModel,
        'controller': LoginScreenController,
    },
    'item detail screen': {
        'model': ItemDetailScreenModel,
        'controller': ItemDetailScreenController,
    },
}