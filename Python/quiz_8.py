# DO *NOT* WRITE YOUR NAME TO MAINTAIN ANONYMITY FOR PLAGIARISM DETECTION


# Assignments to a CircularList object will only involve integer indexes.
#
# When the index is an integer, it is interpreted modulo the length
# of the list.
#
# When working with slices:
# - The last argument of a slice cannot be equal to 0.
# - When the last argument of a slice is not given, it is set to 1.
# - When the first argument of a slice is not given, it is set to
#   0 or to -1 depending on the sign of the last argument.
# - When the second argument of a slice is not given, it is set to
#   len(list) or to -len(list) -1 depending on the sign of the last argument.
# - Denoting by L the CircularList object, returns a list consisting of
#   all elements of the form L[i modulo len(L)] for i ranging between first
#   (included) and second (excluded) arguments of slice, in steps given by
#   third argument of slice.

class CircularList(list):
    def __init__(self, *data):
        """Initialize the class"""
        super(CircularList, self).__init__()
        for d in data:
            self.append(d)

    def __getitem__(self, index):
        """Get sliced items from class"""
        if isinstance(index, slice):
            return [self[i] for i in self._rangeify(index)]
        elif isinstance(index, int):
            index = int(index) % self.__len__()
            return super(CircularList, self).__getitem__(index)
        else:
            raise TypeError("Invalid argument type.")

    def _rangeify(self, slice):
        """Convert slice to a range"""
        start, stop, step = slice.start, slice.stop, slice.step
        if step is None:
            step = 1
        if start is None and step >= 0:
            start = 0
        elif start is None and step < 0:
            start = -1
        if stop is None and step >= 0:
            stop = self.__len__()
        elif stop is None and step < 0:
            stop = -self.__len__() - 1
        return range(start, stop, step)

    def __setitem__(self, index, item):
        index = int(index) % self.__len__()
        super(CircularList, self).__setitem__(index, item)
