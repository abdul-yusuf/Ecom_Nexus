from View.base_screen import BaseScreenView

class SearchPageScreenView(BaseScreenView):
    def on_enter(self, *args):
        data = [
                    {
                        "quantity": "1",
                        "title": "Chicken",
                        "price": "₦200.00",
                        "discount_price": "₦200.00",
                        "slug": "chicken",
                        "description": "Healthy meat for old and young",
                        "image": "/media/chicken_EkZfxgX.png"
                    },
                    {
                        "quantity": "2",
                        "title": "Cow",
                        "price": "₦14000.00",
                        "discount_price": "₦35000.00",
                        "slug": "cow",
                        "description": "Big",
                        "image": "/media/cow_ey5Ipdx.png"
                    },
                    {
                        "quantity": "1",
                        "title": "Goat",
                        "price": "₦10000.00",
                        "discount_price": "null",
                        "slug": "goat",
                        "description": "Ipuson iuio free",
                        "image": "/media/goat_8w8yMpQ.png"
                    },
                    {
                        "quantity": "1",
                        "title": "Goat",
                        "price": "₦10000.00",
                        "discount_price": "₦90000.00",
                        "slug": "goat",
                        "description": "Ipuson iuio free",
                        "image": "/media/goat_8w8yMpQ.png"
                    },
                    {
                        "quantity": "1",
                        "title": "Goat",
                        "price": "₦10000.00",
                        "discount_price": "null",
                        "slug": "goat",
                        "description": "Ipuson iuio free",
                        "image": "/media/goat_8w8yMpQ.png"
                    },
                ]
        self.ids.view_1.data = data
        self.ids.search_fiel.text = self.app.screen_args[0]
        # print(self.app.screen_args[0])
    def model_is_changed(self) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
