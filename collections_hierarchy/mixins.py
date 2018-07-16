from copy import deepcopy

class ComparableMixin(object):
    def __eq__(self, other):
        if hasattr(other, 'DATA_ATTR_NAME'):
            return getattr(self, self.DATA_ATTR_NAME) == getattr(other, other.DATA_ATTR_NAME)
        return getattr(self, self.DATA_ATTR_NAME) == other
    def __ne__(self, other):
        # Relies in __eq__
        return not self == other


class SequenceMixin(object):
    def __iter__(self):
        # if not hasattr(self, 'get_elements'):
        #     raise ValueError("get_elements method not found")
        # return (item for item in self.get_elements())
        self._count = 0
        return self
        

    def __next__(self):
        # return next(self)
        if not hasattr(self, 'get_elements'):
            raise ValueError("get_elements method not found")
        
        if not hasattr(self, '_count'):
            self._count = 0
        
        if self._count >= len(self.get_elements()):
            raise StopIteration
            
        self._count += 1
        
        return self.get_elements()[self._count - 1]
        

    next = __next__

    def __len__(self):
        # Will rely on the iterator
        # can't do len(self.data)
        count = 0
        for i in self:
            count += 1
        return count

    def __getitem__(self, key):
        return getattr(self, self.DATA_ATTR_NAME)[key]
        

    def __setitem__(self, key, value):
        getattr(self, self.DATA_ATTR_NAME)[key] = value

    def __delitem__(self, key):
        del getattr(self, self.DATA_ATTR_NAME)[key]
        
        

    def __contains__(self, item):
        # Will rely on the iterator
        return item in getattr(self, self.DATA_ATTR_NAME)


class RepresentableMixin(object):
    def __repr__(self):
        # Will rely on the iterator or __str__
        name = self.__class__.__name__
        data = getattr(self, self.DATA_ATTR_NAME)
        string = "{}({})".format(name, data)

    def __str__(self):
        # Will rely on the iterator
        return str(getattr(self, self.DATA_ATTR_NAME))


class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        setattr(self, self.DATA_ATTR_NAME,
                initial or self.DATA_DEFAULT_INITIAL)


class OperableMixin(object):
    def __add__(self, other):
        self_copy = deepcopy(self)
        getattr(self_copy, self.DATA_ATTR_NAME).extend(getattr(other, self.DATA_ATTR_NAME))
        return self_copy

    def __iadd__(self, other):
        getattr(self, self.DATA_ATTR_NAME).extend(getattr(other, self.DATA_ATTR_NAME))
        return self

class AppendableMixin(object):
    def append(self, elem):
        # Relies on DATA_ATTR_NAME = 'data'
        getattr(self, self.DATA_ATTR_NAME).append(elem)


class HashableMixin(object):
    def keys(self):
        return getattr(self, self.DATA_ATTR_NAME).keys()

    def values(self):
        return getattr(self, self.DATA_ATTR_NAME).values()

    def items(self):
        return getattr(self, self.DATA_ATTR_NAME).items()


class IndexableMixin(object):
    def index(self, x):
        count = 0
        for item in self:
            if item == x:
                return count
            count += 1
        raise ValueError