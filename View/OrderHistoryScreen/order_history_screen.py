from View.base_screen import BaseScreenView
from kivymd.uix.tab import MDTabsBase
from kivy.uix.scrollview import ScrollView

class OrderHistoryScreenView(BaseScreenView):
    def model_is_changed(self, *args, **kwargs) -> None:
        """
        Called whenever any change has occurred in the data model.
        The view in this method tracks these changes and updates the UI
        according to these changes.
        """
    def server_success(self, *args, **kwargs):
        data = args[0][1]
        in_process_data = []
        transit_data = []
        complete_data = []
        for item in data:
            item['id']=str(item['id'])
            if item['order_set'][0]['received']==False:
                in_process_data.append(item)
            if item['order_set'][0]['received']==False and item['order_set'][0]['being_delivered']:
                transit_data.append(item)
            if item['order_set'][0]['received']==True:
                complete_data.append(item)


        self.ids.view_1.data = in_process_data
        self.ids.view_2.data = transit_data
        self.ids.view_3.data = complete_data

    def server_error(self, *args, **kwargs):
        self.app.create_toast(str(args[1]))

    def server_failed(self, *args, **kwargs):
        self.app.create_toast(str(args[0][1]))

class TabsBase(ScrollView,MDTabsBase):
    pass