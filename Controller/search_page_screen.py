import importlib

import View.SearchPageScreen.search_page_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.SearchPageScreen.search_page_screen)




class SearchPageScreenController:
    """
    The `SearchPageScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.search_page_screen.SearchPageScreenModel
        self.view = View.SearchPageScreen.search_page_screen.SearchPageScreenView(controller=self, model=self.model)

    def get_view(self) -> View.SearchPageScreen.search_page_screen:
        return self.view
