class peps:
    def __init__(self, dict, route) -> None:
        self.dict = dict
        self.route = route
    
    def calls(self,route):
        return print(route)
    def calls2(self,dict):
        return print(dict)

v=peps(2,10)
v.calls(11)
v.calls2(12)