from kivymd.uix.carousel import MDCarousel
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.properties import NumericProperty, StringProperty, DictProperty
from kivymd.uix.fitimage import FitImage
from kivy.uix.image import AsyncImage

class CarouselSlide(MDRelativeLayout):

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.ids.
    #     # self.populate_images(images)
        # print(dir(images))
    def populate_images(self,images,app):
        for value in images.values():
            print('/\\'*40)
            print(value)
            print('/\\'*40)
            image = FitImage(
                source= '{}'.format(app.request_parm.route('media')+value),
                radius=[0,0,20,20]
            )
            print(self.ids)
            self.ids.carousel_head.add_widget(image)


