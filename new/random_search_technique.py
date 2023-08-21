from opentuner.search import technique

class Random_Search_Technique(technique.SequentialSearchTechnique):
    def __init__(self):
        super(Random_Search_Technique, self).__init__()

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
        config = driver.get_configuration(manipulator.random()) # random seed

        for param in self.kernel_params:

            ctr = 0

            while ctr < 31:

                config.data[self.kernels[ctr]] = param[ctr]

                ctr += 1

            config = driver.get_configuration(config.data)
            yield config
            

 
technique.register(Random_Search_Technique())
