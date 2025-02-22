def _normalize(key, value):
    if key == "select" or key == "expand":
        return ",".join(value)
    return value


class QueryOptions(object):

    @staticmethod
    def build(client_object, properties_to_include):
        """
        :param office365.runtime.client_object.ClientObject client_object: Client object
        :param list[str] properties_to_include: The list of properties to include
        """
        query = QueryOptions()
        for name in properties_to_include:
            val = client_object.get_property(name)
            from office365.runtime.client_object import ClientObject
            from office365.runtime.client_object_collection import ClientObjectCollection
            if isinstance(client_object, ClientObjectCollection) or \
                isinstance(val, ClientObject) or name == "Properties":
                query.expand.append(name)
            query.select.append(name)
        return query

    def __init__(self, select=None, expand=None, filter_expr=None, order_by=None, top=None, skip=None):
        """
        A query option is a set of query string parameters applied to a resource that can help control the amount
        of data being returned for the resource in the URL

        :param list[str] select: The $select system query option allows the clients to requests a limited set of
        properties for each entity or complex type.
        :param list[str] expand: The $expand system query option specifies the related resources to be included in
        line with retrieved resources.
        :param str filter_expr: The $filter system query option allows clients to filter a collection of resources
        that are addressed by a request URL.
        :param str order_by: The $orderby system query option allows clients to request resources in either ascending
        order using asc or descending order using desc
        :param int top: The $top system query option requests the number of items in the queried collection to
        be included in the result.
        :param int skip: The $skip query option requests the number of items in the queried collection that
        are to be skipped and not included in the result.
        """
        if expand is None:
            expand = []
        if select is None:
            select = []
        self.select = select
        self.expand = expand
        self.filter = filter_expr
        self.orderBy = order_by
        self.skip = skip
        self.top = top

    def __repr__(self):
        return self.to_url()

    def __str__(self):
        return self.to_url()

    @property
    def is_empty(self):
        result = {k: v for (k, v) in self.__dict__.items() if v is not None and v}
        return not result

    def reset(self):
        self.select = []
        self.expand = []
        self.filter = None
        self.orderBy = None
        self.skip = None
        self.top = None

    def to_url(self):
        """Convert query options to url
        :return: str
        """
        return '&'.join(['$%s=%s' % (key, _normalize(key, value))
                         for (key, value) in self.__dict__.items() if value is not None and value])
