class Heart:
    def __init__(self):
        self.state = "feeling good"

    def update_state(self, cardiac_output):
        if cardiac_output > 70:
            self.state = "high blood pressure"
        else:
            self.state = "feeling good"


class Brain:
    def __init__(self):
        self.state = "rested"

    def update_state(self, brain_load):
        if brain_load > 90:
            self.state = "tired"
        else:
            self.state = "rested"


class Person:
    def __init__(self, cardiac_output, brain_load):
        self.heart = Heart()
        self.brain = Brain()
        self.update_states(cardiac_output, brain_load)

    def update_states(self, cardiac_output, brain_load):
        self.heart.update_state(cardiac_output)
        self.brain.update_state(brain_load)


class Leg:
    def __init__(self, person, moving_speed):
        self.person = person
        self.moving_speed = moving_speed

    def run(self):
        print("Legs moving at speed:", self.moving_speed)
        if self.moving_speed > 10:
            print("Running")
        elif 5 <= self.moving_speed <= 10:
            print("Walking")
        else:
            print("Standing")


# Example usage
if __name__ == "__main__":
    person = Person(cardiac_output=75, brain_load=85)
    leg_instance = Leg(person, moving_speed=12)
    leg_instance.run()
