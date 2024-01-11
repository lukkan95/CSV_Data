import csv


PATH = "50_states.csv"


class StateData(object):

    def __init__(self):

        self.data_dict = 0
        self.list_of_states = []

    def create_list_from_csv(self):
        with open(PATH) as file:
            data = csv.reader(file)
            for row in data:
                self.list_of_states.append(row)