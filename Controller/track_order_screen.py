import importlib

import View.TrackOrderScreen.track_order_screen

# We have to manually reload the view module in order to apply the
# changes made to the code on a subsequent hot reload.
# If you no longer need a hot reload, you can delete this instruction.
importlib.reload(View.TrackOrderScreen.track_order_screen)




class TrackOrderScreenController:
    """
    The `TrackOrderScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.track_order_screen.TrackOrderScreenModel
        self.view = View.TrackOrderScreen.track_order_screen.TrackOrderScreenView(controller=self, model=self.model)

    def get_view(self) -> View.TrackOrderScreen.track_order_screen:
        return self.view
