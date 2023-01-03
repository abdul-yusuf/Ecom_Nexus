
from kivy.properties import ColorProperty, NumericProperty, ObjectProperty
from typing import Union
from kivy.effects.scroll import ScrollEffect

class CustomRefreshScrollEffect(ScrollEffect):
    """
    This class is simply based on DampedScrollEffect.
    If you need any documentation please look at
    :class:`~kivy.effects.dampedscrolleffect`.
    """
    velocity = 10
    min_scroll_to_reload = NumericProperty("-100dp")
    """
    Minimum overscroll value to reload.

    :attr:`min_scroll_to_reload` is a :class:`~kivy.properties.NumericProperty`
    and defaults to `'-100dp'`.
    """

    def on_overscroll(
        self, instance_refresh_scroll_effect, overscroll: Union[int, float]
    ) -> bool:
        if overscroll < self.min_scroll_to_reload:
            scroll_view = self.target_widget.parent
            scroll_view._did_overscroll = True
            return True
        else:
            return False
