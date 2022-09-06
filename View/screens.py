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
from Model.track_order_screen import TrackOrderScreenModel
from Controller.track_order_screen import TrackOrderScreenController
from Model.search_page_screen import SearchPageScreenModel
from Controller.search_page_screen import SearchPageScreenController
from Model.email_verification_screen import EmailVerificationScreenModel
from Controller.email_verification_screen import EmailVerificationScreenController
from Model.forgot_password_screen import ForgotPasswordScreenModel
from Controller.forgot_password_screen import ForgotPasswordScreenController
from Model.q_r_scan_screen import QRScanScreenModel
from Controller.q_r_scan_screen import QRScanScreenController
from Model.feed_screen import FeedScreenModel
from Controller.feed_screen import FeedScreenController
from Model.addresses_screen import AddressesScreenModel
from Controller.addresses_screen import AddressesScreenController

screen = {
    
   'home screen': {
        'model': HomeScreenModel,
        'controller': HomeScreenController,
    },'addresses screen': {
        'model': AddressesScreenModel,
        'controller': AddressesScreenController,
    },
   'my account screen': {
        'model': MyAccountScreenModel,
        'controller': MyAccountScreenController,
    },
    'feed screen': {
        'model': FeedScreenModel,
        'controller': FeedScreenController,
    },
    'login screen': {
        'model': LoginScreenModel,
        'controller': LoginScreenController,
    },
   'email verification screen': {
        'model': EmailVerificationScreenModel,
        'controller': EmailVerificationScreenController,
    },
   'q r scan screen': {
        'model': QRScanScreenModel,
        'controller': QRScanScreenController,
    },
   'forgot password screen': {
        'model': ForgotPasswordScreenModel,
        'controller': ForgotPasswordScreenController,
    },
    'search page screen': {
        'model': SearchPageScreenModel,
        'controller': SearchPageScreenController,
    },
    'track order screen': {
        'model': TrackOrderScreenModel,
        'controller': TrackOrderScreenController,
    },
    'order history screen': {
        'model': OrderHistoryScreenModel,
        'controller': OrderHistoryScreenController,
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
    'item detail screen': {
        'model': ItemDetailScreenModel,
        'controller': ItemDetailScreenController,
    },

}