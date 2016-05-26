class ComparableMixin(object):
    def __eq__(self, other):
        pass

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __ge__(self, other):
        pass


class SequenceMixin(object):
    def __iter__(self):
        pass

    def __next__(self):
        pass

    next = __next__

    def __len__(self):
        pass

    def __getitem__(self, key):
        pass

    def __setitem__(self, key, value):
        pass

    def __delitem__(self, key):
        pass

    def __contains__(self, item):
        pass


class RepresentableMixin(object):
    def __repr__(self):
        pass

    def __str__(self):
        pass


class ConstructibleMixin(object):
    DATA_ATTR_NAME = 'data'

    def __init__(self, initial=None):
        pass


class OperableMixin(object):
    def __add__(self, other):
        pass

    def __iadd__(self, other):
        pass


class AppendableMixin(object):
    def append(self, elem):
        pass


class HashableMixin(object):
    def keys(self):
        pass

    def values(self):
        pass

    def items(self):
        pass


class IndexableMixin(object):
    def index(self, x):
        pass
