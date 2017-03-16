import re


class RouteResolver:
    """
    Lookup the request route in the route table.
    """

    def __init__(self, route_table):
        self._route_table = route_table

    def resolve(self, uri):
        """
        Search the requested URI in the framework's route table.

        :Parameters:
        - `path`: the request URI

        ..Note:: If found it will return a tuple containing the HTTP verb, the action
        to be executed and also a list of parameter values sent as part of the
        route URL.
        """

        for route in self._route_table:
            m = re.compile(route)
            values = re.match(m, uri)

            if values != None:
                (verb, action) = self._route_table[route]
                return (verb, action, values.groups())
