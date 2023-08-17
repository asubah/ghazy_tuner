from opentuner.search import technique
import random


class Random_Search_Technique(technique.SequentialSearchTechnique):
    def __init__(self):
        super(Random_Search_Technique, self).__init__()

        #TODO: Get the number of kernels and put it in a variable
        self.num_of_kernels = 31



        import pandas as pd

        df = pd.read_csv('data.csv')
        self.kernel_params = df.drop(columns=['throughput', 'Unnamed: 0'])
        self.kernel_params = self.kernel_params.values.tolist()

        with open('results/info.txt', 'r') as f:
            path = f.readline().strip()

        with open('results/' + path + '/kernels.txt', 'r') as file:

            self.kernels = []

            for line in file:

                self.kernels.append(line.strip())


    def main_generator(self):

        manipulator = self.manipulator
        driver = self.driver
        # manipulator.random()
        config = driver.get_configuration(manipulator.random()) # random seed

        print(f'\n\nfirst params = {self.kernel_params[0]}\n\n')
        print(f'\n\nkernels = {self.kernels}\n\n')

        print(f'\n\nsize of kernel params = {len(self.kernel_params[0])}\t\tsize of kernels = {len(self.kernels)}\n\n')

        # print(f"\n\nconfig: {dir(config.data)}\n\n")
        # print(f"\n\nconfig iter: {dir(config.data['findClus'])}\n\n")

        # print(f"\n\nconfig.data['findClus'] = {config.data['findClus']}\n\n")


        # print(f"\n\nconfig values: {dir(config.data.values)}\n\n")

       
        # yield self.configuration
        
        # params = self.manip.params

        # while True:

        #     idx = random.randint(1, self.num_of_kernels) - 1
        #     new_value = random.randint(params[idx].min_value, params[idx].max_value) * 32

        #     self.configuration[params[idx].name] = new_value

        #     yield self.configuration
        
        ctr = 0

        while True:

            for (kernel, param) in zip(self.kernels, self.kernel_params[ctr]):

                print(f"(kernel, param) = ({kernel}, {param})")

                config.data[kernel] = param
                # config[kernel] = param

            ctr += 1
            
            #yield self.configuration
            
            # config = driver.get_configuration(config)
            self.yield_nonblocking(config)

 
technique.register(Random_Search_Technique())
