from View.base_screen import BaseScreenView
from .components import CarouselSlide
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelTwoLine
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import TwoLineIconListItem, IconLeftWidget
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

class ItemDetailScreenView(BaseScreenView):
    dialog = None
    def model_is_changed(self,*args, **kwargs) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
        print('*'*12,args,'*'*12)
        try:
            data = args[0]
            self.ids.carousel.source1 = data['images']['image1']
            self.ids.carousel.source2 = data['images']['image2']
            self.ids.carousel.source3 = data['images']['image3']
            self.ids.carousel.source4 = data['images']['image4']

            self.ids.price.text = '₦{}/kg'.format(data['price'])
            self.ids.title.text = data['title']
            self.ids.vendor.text = data['vendor']
        except KeyError or AttributeError:
            # self.ids.vendor.text = ''
            pass
    
    def show_alert_dialog(self):
        self.dialog_open=True

        if True:
            btnx = MDFlatButton(
                    text="View Cart",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    )
            btnd = MDFlatButton(
                    text="STAY",
                    theme_text_color="Custom",
                    text_color=self.theme_cls.primary_color,
                    )

            btnx.bind(on_release=lambda x: self.app.onNextScreen(self.name, 'home screen', 'switch_to', 'Cart screen'))
            # if self.dialog:
                # btnx.bind(on_release=lambda x: self.dialog.dismiss())
            
            self.dialog = MDDialog(
                text="Will you like to?",
                buttons=[
                    btnd,
                    btnx,
                ],
            )
            self.dialog_open=False
            self.dialog.open()
            btnx.bind(on_release=lambda x: self.dialog.dismiss())
            btnd.bind(on_release=lambda x: self.dialog.dismiss())
    
    def server_error(self, *args, **kwargs):
        self.app.create_toast(str(args[1]))

    def server_failed(self, *args, **kwargs):
        self.app.create_toast(str(args[0][1]))

class Content(MDBoxLayout):
    pass
# class ExpansionPanel(MDExpansionPanel):
    # """_summary_
    #  MDExpansionPanel(
    #         icon=os.path.join(images_path, "logo", "kivymd-icon-128.png"),
    #         content=Content(),
    #         panel_cls=MDExpansionPanelThreeLine(
    #             text="Text",
    #             secondary_text="Secondary text",
    #             tertiary_text="Tertiary text",
    #         )
    # Args:
    #     MDExpansionPanel (_type_): _description_
    # """
    # content=Content()# panel content

    # # content = MDBoxLayout(
    # #             TwoLineIconListItem(
    # #                 IconLeftWidget(
    # #                     icon='assets/images/boy-1.png',
    # #                     size=(45,45),
    # #                     size_hint=(None,None)),
    # #                 text='Abdulbari',
    # #                 secondary_text='A very good product'
    # #                 ),
    # #             TwoLineIconListItem(
    # #                 IconLeftWidget(
    # #                     icon='assets/images/boy-1.png',
    # #                     size=(45,45),
    # #                     size_hint=(None,None)),
    # #                 text='Abdulbari',
    # #                 secondary_text='A very good product'
    # #                 ),
    # #             TwoLineIconListItem(
    # #                 IconLeftWidget(
    # #                     icon='assets/images/boy-1.png',
    # #                     size=(45,45),
    # #                     size_hint=(None,None)),
    # #                 text='Abdulbari',
    # #                 secondary_text='A very good product'
    # #                 ),
    # #             adaptive_height='True',
    # #             orientation='vertical',
    # #             spacing=10
    # #         )

    # # MDBoxLayout(
    # #             TwoLineIconListItem(
    # #                 text='Abdulbari',
    # #                 secondary_text = 'A great product'
    # #             ),
    # #             adaptive_height = 'True'

    # #         ) 
    # panel_cls = MDExpansionPanelTwoLine(
    #                 text="Review",
    #                 secondary_text='210 Reviews'
    #                 )