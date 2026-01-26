class Dog:
    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
       
        self.arm_length = arm_length      
        self.leg_length = leg_length      
        self.num_eyes = num_eyes          
        self.has_tail = has_tail          
        self.is_furry = is_furry          

    def describe(self):
        print("This animal is a dog.")
        print(f"Arm length: {self.arm_length} units")
        print(f"Leg length: {self.leg_length} units")
        print(f"Number of eyes: {self.num_eyes}")

        if self.has_tail:
            print("It has a tail.")
        else:
            print("It does not have a tail.")

        if self.is_furry:
            print("It is furry.")
        else:
            print("It is not furry.")


def main():
    my_dog = Dog(
        arm_length=0.4,
        leg_length=0.8,
        num_eyes=2,
        has_tail=True,
        is_furry=True
    )

    my_dog.describe()


if __name__ == "__main__":
    main()
