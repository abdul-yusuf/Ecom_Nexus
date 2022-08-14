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

screen = {
    'home screen': {
        'model': HomeScreenModel,
        'controller': HomeScreenController,
    },
    'login screen': {
        'model': LoginScreenModel,
        'controller': LoginScreenController,
    },
    'signup screen': {
        'model': SignUpScreenModel,
        'controller': SignUpScreenController,
    },    
    'item detail screen': {
        'model': ItemDetailScreenModel,
        'controller': ItemDetailScreenController,
    },
}