# The model implements the observer pattern. This means that the class must
# support adding, removing, and alerting observers. In this case, the model is
# completely independent of controllers and views. It is important that all
# registered observers implement a specific method that will be called by the
# model when they are notified (in this case, it is the `model_is_changed`
# method). For this, observers must be descendants of an abstract class,
# inheriting which, the `model_is_changed` method must be overridden.


class BaseScreenModel:
    """Implements a base class for model modules."""

    _observers = []

    def add_observer(self, observer) -> None:
        self._observers.append(observer)

    def remove_observer(self, observer) -> None:
        self._observers.remove(observer)

    def notify_observers(self, name_screen: str, *args, meths=None, **kwargs) -> None:
        """
        Method that will be called by the observer when the model data changes.

        :param name_screen:
            name of the view for which the method should be called
            :meth:`model_is_changed`.
        """
        print('passed2')
        for observer in self._observers:
            if observer.name == name_screen:
                if meths=='loading':
                    observer.server_processing(*args)
                    print('loading sending signal')
                if meths=='success':
                    observer.server_success(*args,**kwargs)
                    print('server success sending signal')
                if meths=='error':
                    observer.server_error(*args,**kwargs)
                    print('server error sending signal')
                if meths=='failed':
                    observer.server_failed(*args,**kwargs)
                    print('server failed sending signal')
                if meths=='cart_success':
                    observer.populate_cart(*args,**kwargs)
                    print('server cart populate sending signal')
                if meths=='payment_success':
                    observer.create_webview(*args,**kwargs)
                    print('server payment success sending signal')
                else:
                    observer.model_is_changed(*args,**kwargs)
                    print('model is changed sending signal')
                break
