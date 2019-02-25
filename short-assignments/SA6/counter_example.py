


class Counter:
    def __init__(self, limit, initial = 0, min_digits = 1):
        self.limit = limit
        self.min_digits = min_digits

        if initial >= 0 and initial <= limit - 1:
            self.current_value = initial
        else:
            print("Invalid initial value. Counter value is now set to 1 minus the limit.")
            self.current_value = limit - 1
            print("Current Value is now: " + str(self.current_value))

    def get_value(self):
        return int(self.current_value)

    def __str__(self):
        length = len(str(self.current_value))
        num_zeroes = self.min_digits - length
        return str('0' * num_zeroes) + str(self.current_value)

    def tick(self):
        if self.current_value == 0:
            self.current_value = self.limit - 1
            return True
        else:
            self.current_value -= 1
            return False


