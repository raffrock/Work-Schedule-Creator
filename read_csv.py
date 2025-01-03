# reads csv and converts into data frame with relevant names

import pandas as pd
import shifts_handler

class CsvToSchedule:
    shift_list = shifts_handler.Shifts()

    def __init__(self):
        # names of columns saved to change later if needed
        self.input_csv_name = "test1.csv"
        self.name = "Name"
        self.week = "Week"
        # self.availability = ["Monday","Tuesday","Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.availability = ["Availability [Monday]",
                             "Availability [Tuesday]",
                             "Availability [Wednesday]",
                             "Availability [Thursday]",
                             "Availability [Friday]",
                             "Availability [Saturday]",
                             "Availability [Sunday]"]
        self.num_of_shifts = "Number of Shifts Wanted"

        self.needed_columns = [self.name, self.week] + self.availability + [self.num_of_shifts]

        self.df = pd.read_csv(self.input_csv_name, usecols = self.needed_columns)
        self.df["Assigned"] = 0
        self.df["Assigned To"] = [] # holds name of employee(s)

        self.schedule = pd.DataFrame({
            "Names" : self.df[self.name],
        })
        for day in self.availability:
            self.schedule[day] = "" # string holding time range for representation

        # self.shift_list = shift_list

    def change_csv_name(self, new_name):
        self.input_csv_name = new_name

        self.convert_csv()

    def change_column_names(self, new_name, new_week, new_availability, new_num_of_shifts):
        self.name = new_name
        self.week = new_week
        self.availability = new_availability
        self.num_of_shifts = new_num_of_shifts

        self.needed_columns = [self.name, self.week] + self.availability + [self.num_of_shifts]

        self.convert_csv()

    def convert_csv(self):
        self.df = pd.read_csv(self.input_csv_name, usecols = self.needed_columns)
        self.df["Assigned"] = 0

    # first plan:
    # fill in days when there is only one person available
    def fill_one_available_first(self):
        for day in self.availability:
            for shift in self.shift_list.types_of_shifts:
                if shift.needed[day] and self.df[day].count(shift.name) == len(self.df[self.name])-1:
                    # add to sch df
                    employee_name = self.df.loc[self.df[day] == shift.name][0] # should return name
                    # employee_name = self.df.at[day][]
                    self.schedule.loc[self.schedule["Names"] == employee_name] = shift.time
                    # update that it is filled on shift and csv
                    self.df.at[employee_name]["Assigned"] += 1
                    self.shift_list.add_employee(shift.name)

    # fill the lowest availability from employees
    # then repeat until there is no one availability for a shift
    #   bc no one picked it or not enough shifts wanted to cover shifts needed
        # track number of employees available for each shift, auto fill if shift only has one person available
        # go by lowest availability to greatest, favoring those with high availability to shift filled ratio
            # this is to ensure everyone gets a shift bc if they have 5:3 and someone has 1:0, the person with 1 should get a shift
            # maybe rearrange to make sure everyone gets a shift
            # maybe cap the max number of shifts given to fit total shifts needed?

    # old notes:
        # check for availability day by day based on number of shifts and needed shifts
        # track if employees are assigned to more shifts than they can reasonably fill
