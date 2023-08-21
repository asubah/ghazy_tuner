from opentuner.search import technique
import random


class Random_Search_Technique(technique.SequentialSearchTechnique):
    def __init__(self):
        super(Random_Search_Technique, self).__init__()

    def main_generator(self):

        manipulator = self.manipulator
        driver = self.driver
        config = driver.get_configuration(manipulator.random()) # random seed

        for kernel in config.data:
            config.data[kernel] = round(config.data[kernel] / 32)

        while True:

            random_key = random.choice(list(config.data.keys()))
            random_value = random.randint(1, 32) * 32

            config.data[random_key] = random_value

            config = driver.get_configuration(config.data)

            yield config
 
technique.register(Random_Search_Technique())