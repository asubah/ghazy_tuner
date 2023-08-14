from opentuner.search import technique
import random


class Random_Search_Technique(technique.SequentialSearchTechnique):
    def __init__(self):

        #TODO: Get the number of kernels and put it in a variable
        self.num_of_kernels = 31
        self.manip = self.manipulator
        self.configuration = self.manip.random() # random seed


    def main_generator(self):

        yield self.configuration
        
        params = self.manip.params

        while True:

            idx = random.randint(1, self.num_of_kernels) - 1
            new_value = random.randint(params[idx].min_value, params[idx].max_value) * 32

            self.configuration[params[idx].name] = new_value

            yield self.configuration

 
technique.register(Random_Search_Technique())
