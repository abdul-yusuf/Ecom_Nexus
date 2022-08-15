import importlib

import View.CategoriesScreen.categories_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.CategoriesScreen.categories_screen)




class CategoriesScreenController:
    """
    The `CategoriesScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.categories_screen.CategoriesScreenModel
        self.view = View.CategoriesScreen.categories_screen.CategoriesScreenView(controller=self, model=self.model)

    def get_view(self) -> View.CategoriesScreen.categories_screen:
        return self.view
