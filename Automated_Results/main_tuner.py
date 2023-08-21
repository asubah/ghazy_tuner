#!/usr/bin/env python

import argparse
import opentuner
from opentuner import ConfigurationManipulator
from opentuner import IntegerParameter
from opentuner import MeasurementInterface
from opentuner import Result
import time
import json
import random_search_technique
import csv

parser = argparse.ArgumentParser(parents=opentuner.argparsers())

parser.add_argument('--cmssw-config', type=str, 
                    help='location of cmssw config file')
parser.add_argument('--events', type=str, default="10300",
                    help='number of events per cmsRun job')
parser.add_argument('--repeats', type=str, default="3",
                    help='repeat each measurement N times')


base_dir = ''


class CMSSWTuner(MeasurementInterface):


    def manipulator(self):

        with open('results/info.txt', 'r') as f:
            base_dir = f.readline().strip()

        manipulator = ConfigurationManipulator()

        manipulator.add_parameter(IntegerParameter("number_of_jobs", 1, 4))
        manipulator.add_parameter(IntegerParameter("number_of_cpu_threads", 1, 32))
        manipulator.add_parameter(IntegerParameter("number_of_streams", 1, 24))

        with open(self.base_dir + '/kernels.txt', 'r') as f and open('kernels.json') as jsn:

            kernel_info = json.load(jsn)

            for line in f:

                # manipulator.add_parameter(IntegerParameter(line, # kernel name
                #                                            int(kernel_info[line]['min']), # min value
                #                                            int(kernel_info[line]['max'])) #max value
                #                                           )
                # kernels.append(line)

                manipulator.add_parameter(IntegerParameter(line, # kernel name
                                                           1, # min value
                                                           1024 #max value
                                                          )
                )           


        return manipulator

    def run(self, desired_result, input, limit):

        cfg = desired_result.configuration.data

        
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

        data = []

        data.append(t2 - t1)

        for kernel in cfg:
            data.append(cfg[kernel])

        with open('results/' + base_dir + 'data.csv', 'a') as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(data)


        return Result(time=mytime)#run_result['time'])

if __name__ == '__main__':

    argparser = opentuner.default_argparser()
    CMSSWTuner.main(argparser.parse_args())