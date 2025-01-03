# import read_csv

class Shift:
    def __init__(self, name, needed, time, required, filled):
        self.name = name
        self.needed = {"Monday": False,"Tuesday": False,"Wednesday": False, "Thursday": False, "Friday": False, "Saturday": False}
        days_of_week = ["Monday","Tuesday","Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        if needed:
            for key in self.needed.keys():
                self.needed[key] = True
        else: # need is list, include error handling later
            for i in range(0,7):
                if needed[i]:
                    self.needed[days_of_week[i]] = True
        self.time = time # string representing the time range of shift
        self.required = required
        self.filled = 0

class Shifts:
    def __init__(self):
        # group of shifts
        self.types_of_shifts = [Shift("Opening Shift", True, '10:30-3:00',1, 0),
                                Shift("Morning Shift", True,'11:30-3:00',1, 0),
                                Shift("Closing Shift", True,'3:00-8:30', 2, 0)]
    # reset filled
    def reset_filled(self):
        for shift in self.types_of_shifts:
            shift.filled = 0

    def add_shift(self, name, needed, time, required):
        self.types_of_shifts.append(Shift(name, needed, time, required, 0))

    def remove_shift(self, name):
        for i in range(0, len(self.types_of_shifts)):
            if self.types_of_shifts[i].name == name:
                self.types_of_shifts.pop(i)
                return True
        return False

    def change_shift_name(self, old_name, new_name):
        for i in range(0, len(self.types_of_shifts)):
            if self.types_of_shifts[i].name == old_name:
                self.types_of_shifts[i].name = new_name
                return True
        return False

    def change_shift_time(self, name, new_time):
        for i in range(0, len(self.types_of_shifts)):
            if self.types_of_shifts[i].name == name:
                self.types_of_shifts[i].time = new_time
                return True
        return False

    def change_shift_requirement(self, old_required, new_required):
        for i in range(0, len(self.types_of_shifts)):
            if self.types_of_shifts[i].required == old_required:
                self.types_of_shifts[i].required = new_required
                return True
        return False

    def add_employee(self, name):
        for i in range(0, len(self.types_of_shifts)):
            if self.types_of_shifts[i].name == name and self.types_of_shifts[i].filled < self.types_of_shifts[i].required:
                self.types_of_shifts[i].filled += 1
                return True
            elif self.types_of_shifts[i].name == name:
                return False
        return False

    def remove_employee(self, name):
        for i in range(0, len(self.types_of_shifts)):
            if self.types_of_shifts[i].name == name and self.types_of_shifts[i].filled >= 0:
                self.types_of_shifts[i].filled -= 1
                return True
            elif self.types_of_shifts[i].name == name:
                return False
        return False