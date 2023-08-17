#!/usr/bin/env python

# import argparse
import opentuner
from opentuner import ConfigurationManipulator
from opentuner import IntegerParameter
from opentuner import MeasurementInterface
from opentuner import Result
import time
import json
import random_search_technique

ctr = 0

'''
parser = argparse.ArgumentParser(parents=opentuner.argparsers())

parser.add_argument('--cmssw-config', type=str, 
                    help='location of cmssw config file')
parser.add_argument('--events', type=str, default="10300",
                    help='number of events per cmsRun job')
parser.add_argument('--repeats', type=str, default="3",
                    help='repeat each measurement N times')

'''

base_dir = ''
kernels = []

with open('./results/info.txt', 'r') as f:
    base_dir += f.readline().strip()


import pandas as pd

df = pd.read_csv('data.csv')
tp = df['throughput']
tp = tp.values.tolist()


with open('results/' + base_dir + '/kernels.txt', 'r') as file:

    kernels = []

    for line in file:

        kernels.append(line.strip())


class CMSSWTuner(MeasurementInterface):
    
    # def __init__(self):

    #     self.base_dir = ''
    #     self.kernels = []

    #     with open('./results/info.txt', 'r') as f:
    #         self.base_dir += f.readline().strip()

        
    #     import pandas as pd

    #     df = pd.read_csv('data.csv')
    #     self.tp = df['throughput']
    #     self.tp = self.tp.values.tolist()


    #     with open('results/' + self.base_dir + '/kernels.txt', 'r') as file:

    #         self.kernels = []

    #         for line in file:

    #             self.kernels.append(line.strip())


    def manipulator(self):

        manipulator = ConfigurationManipulator()

        # manipulator.add_parameter(IntegerParameter("number_of_jobs", 1, 4))
        # manipulator.add_parameter(IntegerParameter("number_of_cpu_threads", 1, 32))
        # manipulator.add_parameter(IntegerParameter("number_of_streams", 1, 24))

        '''
        with open(self.base_dir + '/kernels.txt', 'r') as f and open('kernels.json') as jsn:

            kernel_info = json.load(jsn)

            for line in f:

                manipulator.add_parameter(IntegerParameter(line, # kernel name
                                                            int(kernel_info[line]['min']), # min value
                                                            int(kernel_info[line]['max'])) #max value
                                                        )

                self.kernels.append(line)

        '''


        manipulator.add_parameter(IntegerParameter("findClus", 1, 256))
        manipulator.add_parameter(IntegerParameter("RawToDigi_kernel", 1, 256))
        manipulator.add_parameter(IntegerParameter("kernelLineFit3", 1, 256))
        manipulator.add_parameter(IntegerParameter("kernelLineFit4", 1, 256))
        manipulator.add_parameter(IntegerParameter("kernel_connect", 1, 256))
        manipulator.add_parameter(IntegerParameter("getHits", 1, 256))
        manipulator.add_parameter(IntegerParameter("kernel_find_ntuplets", 1, 256))
        manipulator.add_parameter(IntegerParameter("fishbone", 1, 256))
        manipulator.add_parameter(IntegerParameter("clusterChargeCut", 1, 256))
        manipulator.add_parameter(IntegerParameter("calibDigis", 1, 256))
        manipulator.add_parameter(IntegerParameter("countModules", 1, 256))
        manipulator.add_parameter(IntegerParameter("kernelFastFit3", 1, 256))
        manipulator.add_parameter(IntegerParameter("kernelFastFit4", 1, 256))
        manipulator.add_parameter(IntegerParameter("kernelFastFit5", 1, 256))
        manipulator.add_parameter(IntegerParameter("kernelLineFit5", 1, 256))
        manipulator.add_parameter(IntegerParameter("kernel_fillHitDetIndices", 1, 256))
        manipulator.add_parameter(IntegerParameter("kernel_mark_used", 1, 256))
        manipulator.add_parameter(IntegerParameter("finalizeBulk", 1, 256))
        manipulator.add_parameter(IntegerParameter("kernel_earlyDuplicateRemover", 1, 256))
        manipulator.add_parameter(IntegerParameter("kernel_countMultiplicity", 1, 256))
        manipulator.add_parameter(IntegerParameter("kernel_fillMultiplicity", 1, 256))
        manipulator.add_parameter(IntegerParameter("kernel_checkOverflows", 1, 256))
        manipulator.add_parameter(IntegerParameter("initDoublets", 1, 256))
        manipulator.add_parameter(IntegerParameter("kernel_classifyTracks", 1, 256))
        manipulator.add_parameter(IntegerParameter("kernel_fishboneCleaner", 1, 256))
        manipulator.add_parameter(IntegerParameter("kernel_fastDuplicateRemover", 1, 256))
        manipulator.add_parameter(IntegerParameter("kernel_countHitInTracks", 1, 256))
        manipulator.add_parameter(IntegerParameter("kernel_fillHitInTracks", 1, 256))
        manipulator.add_parameter(IntegerParameter("kernel_tripletCleaner", 1, 256))
        manipulator.add_parameter(IntegerParameter("kernel_doStatsForHitInTracks", 1, 256))
        manipulator.add_parameter(IntegerParameter("kernel_doStatsForTracks", 1, 256))


        return manipulator

    def run(self, desired_result, input, limit):


        global ctr
        print(f'\n========== Round {ctr + 1} ==========\n')

        print('\nrun 0')

        cfg = desired_result.configuration.data

        '''
        cmd = [
               "/data/user/abmohame/CMSSW_12_6_0/run/patatrack-scripts/benchmark",
               self.args.cmssw_config,
               "-r", self.args.repeats,
               "-e", self.args.events,
               "-j", str(cfg["number_of_jobs"] * 2),
               "-t", str(cfg["number_of_cpu_threads"] * 2),
               "-s", str(cfg["number_of_streams"] * 2),
               "--no-warmup",
               "--no-io-benchmark",
               "--logdir", base_path + "benchmark_logs",
               "--benchmark-results", base_path + "benchmark_results"
               ]

        t1 = time.time()
        subprocess.run(cmd, encoding='UTF-8', capture_output=True)
        t2 = time.time()

        results = f"{t2 - t1} "

        for kernel in self.kernels:

            results += f'{cfg[kernel]} '

        results = results.strip()

        with open(self.base_dir + '/data.txt', 'a') as f:
            f.write(results)

        '''
        global kernel
        global tp

        print('\nrun 1')

        mytime = tp[ctr]
        ctr += 1

        data = f'{mytime} '
        for kernel in kernels:
            data += f"{cfg[kernel]} "

        data = data.strip() #to remove any spaces at the end
        data += '\n'

        print('\nrun 2')

        print(f'\n\n{data}\n\n')

        with open('results/' + base_dir + '/data.csv', 'a') as f:
            f.write(data)


        return Result(time=mytime)#run_result['time'])

if __name__ == '__main__':
    # args = parser.parse_args()
    # CMSSWTuner.main(args)

    print('\nmain 1')
    argparser = opentuner.default_argparser()
    print('\nmain 2')
    CMSSWTuner.main(argparser.parse_args())
    print('\nmain 3')

