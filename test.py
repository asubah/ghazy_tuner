    #!/usr/bin/env python

import opentuner
from opentuner import ConfigurationManipulator
from opentuner import IntegerParameter
from opentuner import MeasurementInterface
from opentuner import Result
from mytime import time_taken
import bt
import time

class GccFlagsTuner(MeasurementInterface):

  def manipulator(self):
    """
    Define the search space by creating a
    ConfigurationManipulator
    """
    manipulator = ConfigurationManipulator()
    manipulator.add_parameter(IntegerParameter('tpd', 2, 80))
    manipulator.add_parameter(IntegerParameter('bpd', 2, 80))
    return manipulator

  def run(self, desired_result, input, limit):
    """
    Compile and run a given configuration then
    return performance
    """

    cfg = desired_result.configuration.data

    gcc_cmd = f"make THREADS_PER_DIM={cfg['tpd']} BLOCKS_PER_DIM={cfg['bpd']}"
    #gcc_cmd += f"-DTHREADS_PER_DIM={cfg['tpd']} -DBLOCKS_PER_DIM={cfg['bpd']}"
    #gcc_cmd += ' -o test'

    compile_result = self.call_program(gcc_cmd)

    #print(f"Compile Results:\n\n{compile_result['stderr'].decode('ascii')}\n\n")

    assert compile_result['returncode'] == 0

    run_cmd = './run'

    t1 = time.time()
    run_result = self.call_program(run_cmd)

    print(f"Run Results = \n\noutput: {run_result['stdout'].decode('ascii')}\nerror: {run_result['stderr'].decode('ascii')}\n\n")

    try:
        assert run_result['returncode'] == 0
        t2 = time.time()

        time_taken = t2 - t1
    except:
        time_taken = 1000000

    print(f"\n==========\nthreads per dim = {cfg['tpd']}\nblocks per dim = {cfg['bpd']}\nTime Taken = {time_taken}\ttime taken by opentuner = {run_result['time']}\n==========\n")

    #self.call_program('make clean')

    return Result(time=run_result['time'])

  def save_final_config(self, configuration):
    """called at the end of tuning"""
    print("Optimal block size written to mmm_final_config.json:", configuration.data)
    self.manipulator().save_to_file(configuration.data, 'mmm_final_config.json')


if __name__ == '__main__':
  argparser = opentuner.default_argparser()
  GccFlagsTuner.main(argparser.parse_args())