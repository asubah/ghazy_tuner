import argparse
import opentuner
from opentuner import ConfigurationManipulator
from opentuner import IntegerParameter
from opentuner import MeasurementInterface
from opentuner import Result
import time

parser = argparse.ArgumentParser(parents=opentuner.argparsers())

parser.add_argument('--cmssw-config', type=str, 
                    help='location of cmssw config file')
parser.add_argument('--events', type=str, default="10300",
                    help='number of events per cmsRun job')
parser.add_argument('--repeats', type=str, default="3",
                    help='repeat each measurement N times')


class CMSSWTuner(MeasurementInterface):
    
    def __init__(self):

        self.base_dir = ''
        self.kernels = []

        with open('./results/info.txt', 'r') as f:
            self.base_dir += f.readline().strip()


    def manipulator(self):

        manipulator = ConfigurationManipulator()

        manipulator.add_parameter(IntegerParameter("number_of_jobs", 1, 4))
        manipulator.add_parameter(IntegerParameter("number_of_cpu_threads", 1, 32))
        manipulator.add_parameter(IntegerParameter("number_of_streams", 1, 24))

        with open(self.base_dir + '/kernels.txt', 'r') as f:
            for line in f:
                line = line.split(' ')

                manipulator.add_parameter(IntegerParameter(line[0], # kernel name
                                                            int(line[1]), # min value
                                                            int(line[2])) #max value
                                                        )

                self.kernels.append(line[0])

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

        results = f"{t2 - t1} "

        for kernel in self.kernels:

            results += f'{cfg[kernel]} '

        results = results.strip()

        with open(self.base_dir + '/data.txt', 'a') as f:
            f.write(results)


        return Result(time=run_result['time'])

if __name__ == '__main__':
    args = parser.parse_args()
    CMSSWTuner.main(args)

