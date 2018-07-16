from collections_hierarchy.mixins import *


class List(ComparableMixin,
           SequenceMixin,
           RepresentableMixin,
           OperableMixin,
           ConstructibleMixin,
           IndexableMixin,
           AppendableMixin):
    DATA_DEFAULT_INITIAL = []

    def get_elements(self):
        # return self.data
        return getattr(self, self.DATA_ATTR_NAME)
    
    def count(self):
        return self.__len__()


class Dict(HashableMixin,
           ComparableMixin,
           SequenceMixin,
           RepresentableMixin,
           ConstructibleMixin):
    DATA_DEFAULT_INITIAL = {}

    def get_elements(self):
        return list(getattr(self, self.DATA_ATTR_NAME).keys())
        
    def count(self):
        return len(self.keys())
        
