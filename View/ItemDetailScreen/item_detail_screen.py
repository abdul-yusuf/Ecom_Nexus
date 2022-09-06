from cgitb import text
from View.base_screen import BaseScreenView
from .components import CarouselSlide
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelTwoLine
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import TwoLineIconListItem, IconLeftWidget

class ItemDetailScreenView(BaseScreenView):
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
class Content(MDBoxLayout):
    pass
# class ExpansionPanel(MDExpansionPanel):
#     # content=Content()# panel content
#     # content = MDBoxLayout(
#     #             TwoLineIconListItem(
#     #                 IconLeftWidget(
#     #                     icon='assets/images/boy-1.png',
#     #                     size=(45,45),
#     #                     size_hint=(None,None)),
#     #                 text='Abdulbari',
#     #                 secondary_text='A very good product'
#     #                 ),
#     #             TwoLineIconListItem(
#     #                 IconLeftWidget(
#     #                     icon='assets/images/boy-1.png',
#     #                     size=(45,45),
#     #                     size_hint=(None,None)),
#     #                 text='Abdulbari',
#     #                 secondary_text='A very good product'
#     #                 ),
#     #             TwoLineIconListItem(
#     #                 IconLeftWidget(
#     #                     icon='assets/images/boy-1.png',
#     #                     size=(45,45),
#     #                     size_hint=(None,None)),
#     #                 text='Abdulbari',
#     #                 secondary_text='A very good product'
#     #                 ),
#     #             adaptive_height='True',
#     #             orientation='vertical',
#     #             spacing=10
#     #         )

#     # MDBoxLayout(
#     #             adaptive_height = 'True'
#     #             TwoLineIconListItem(
#     #                 text='Abdulbari',
#     #                 secondary_text = 'A great product'
#     #             )
#     #         ) 
#     panel_cls = MDExpansionPanelTwoLine(
#                     text="Review",
#                     secondary_text='210 Reviews'
#                     )