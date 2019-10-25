class Filter:
    def __init__(self, _dict):
        self._dict = _dict

    def return_all_above_average_value(self):
        """
        Returns list with keys where all values above average
        """
        average_rating = self.get_average_value()
        new_dict = {}
        for i in self._dict:
            if self._dict[i] >= average_rating:
                new_dict[i] = self._dict[i]
        return [*new_dict]

    def return_all_below_average_value(self):
        """
        Returns list with keys where all values below average
        """
        average_rating = self.get_average_value()
        new_dict = {}
        for i in self._dict:
            if self._dict[i] <= average_rating:
                new_dict[i] = self._dict[i]
        return [*new_dict]

    def get_average_value(self):
        """
        Returns average value
        """
        return sum([*self._dict.values()]) / len(self._dict)
