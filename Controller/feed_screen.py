import importlib

import View.FeedScreen.feed_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.FeedScreen.feed_screen)




class FeedScreenController:
    """
    The `FeedScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.feed_screen.FeedScreenModel
        self.view = View.FeedScreen.feed_screen.FeedScreenView(controller=self, model=self.model)

    def get_view(self) -> View.FeedScreen.feed_screen:
        return self.view
