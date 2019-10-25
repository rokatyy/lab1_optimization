from dictionaries import Filter

groupmates = [
    {
        "name": "Василий",
        "group": "912-2",
        "age": 19,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": "Георгий",
        "group": "912-2",
        "age": 19,
        "marks": [3, 5, 4, 3, 5]
    }
]


class students:
    def __init__(self, students_list):
        self.students_list = students_list
        self.students_dict = {}
        self.convert_list_to_dict_with_unique_numbers()
        self.filter = Filter

    def convert_list_to_dict_with_unique_numbers(self):
        """
        This method converts students list to students dictionary where each student has unique identification number
        Args:
            students_list (list) - list of dictionaries
        Returns:
            students_dict (dict) - dict of dicts
        """
        for i in range(len(self.students_list)):
            self.students_dict[i + 1] = self.students_list[i]

    def return_all_students_above_average_value(self):
        """
        This method filter students by average rate
        Returns:
            students_above_average_dict (dict)
        """
        marks_dict = {}
        for i in self.students_dict: marks_dict[i] = sum(self.students_dict[i]["marks"]) / len(
            self.students_dict[i]["marks"])
        filtered_keys = self.filter(marks_dict).return_all_above_average_value()
        return {key: self.students_dict.get(key) for key in filtered_keys}

    def return_all_students_below_average_value(self):
        """
        This method filter students by average rate
        Returns:
            students_above_average_dict (dict)
        """
        marks_dict = {}
        for i in self.students_dict: marks_dict[i] = sum(self.students_dict[i]["marks"]) / len(
            self.students_dict[i]["marks"])
        filtered_keys = self.filter(marks_dict).return_all_below_average_value()
        return {key: self.students_dict.get(key) for key in filtered_keys}
