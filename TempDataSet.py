import sys
import math

docstring = """ TempDataSet 
    Submitted by Carolyn Pyun
    Submitted:  3/23/21
    Manages temperature data, data encapsulated into this class.
"""


class TempDataSet:
    """ a class used to represent the Temperature Data Set

        Attributes
        _data_set : ??
            the data/ data set
            (Day of Week, Time of Day, Sensor Number, Reading Type, Value)
        _name : string
            name of dataset
        num_dataset_objects : int
            number of different objects
    """
    # number of TempDataSet objects
    num_dataset_objects = 0

    # initializer method
    def __init__(self):
        self._data_set = None
        self._name = "Unnamed"
        TempDataSet.num_dataset_objects += 1

    @property
    def get_name(self):
        return self._name

    # set the name
    def set_name(self, new_name):
        if len(new_name) < 3 or len(new_name) > 20:
            raise ValueError
        self._name = new_name
        return True

    def process_file(self, file_path):
        # open the file
        # try:
        #    my_file = open(file_path, 'r')
        # except FileNotFoundError:
        #    sys.exit()

        my_file = open(file_path, 'r')
        self._data_set = []
        for next_line in my_file:
            [day, time, sensor, reading, value] = next_line.split(",")
            if reading == "TEMP":
                day = int(day)
                time = float(time)
                time = math.floor(time * 24)
                value = float(value)
                sensor = int(sensor)
                data_tuple = (day, time, sensor, value)
                self._data_set.append(data_tuple)
        my_file.close()

        return True

    def get_summary_statistics(self, active_sensors):
        if active_sensors is None or self._data_set is None or len(active_sensors) == 0:
            return None
        else:
            active_sensors_temp = [i[3] for i in self._data_set if i[2] in active_sensors]
            stats = (min(active_sensors_temp), max(active_sensors_temp), sum(active_sensors_temp) / len(active_sensors_temp))
            # print(stats)
            return stats

    def get_avg_temperature_day_time(self, active_sensors, day, time):
        if active_sensors is None or self._data_set is None or len(active_sensors) == 0:
            return None
        else:
            active_sensors_temp = [i[3] for i in self._data_set if i[2] in active_sensors and
                                   i[0] == day and i[1] == time]
            return sum(active_sensors_temp) / len(active_sensors_temp)

    def get_num_temps(self, active_sensors, lower_bound, upper_bound):
        if active_sensors is None:
            return None
        else:
            return 0

    def get_loaded_temps(self):
        if self._data_set is None:
            return None
        else:
            return len(self._data_set)

    @classmethod
    def get_num_objects(cls):
        return cls.num_dataset_objects
