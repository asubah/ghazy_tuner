#!/usr/bin/env python

import opentuner
from opentuner import ConfigurationManipulator
from opentuner import IntegerParameter
from opentuner import MeasurementInterface
from opentuner import Result
import time
import random


time_taken = 0;

def binary_tuning():

    #objective   = self.objective
    #driver      = self.driver
    #manipulator = self.manipulator

    UPPER_LIMIT = random.randint(1000, 1500)
    LOWER_LIMIT = 32
    CURRENT_NUMBER = (UPPER_LIMIT + LOWER_LIMIT) // 2

    while True:

      yield UPPER_LIMIT
      TIME_TAKEN_BY_UPPER_LIMIT = time_taken

      yield LOWER_LIMIT
      TIME_TAKEN_BY_LOWER_LIMIT = time_taken

      if TIME_TAKEN_BY_UPPER_LIMIT < TIME_TAKEN_BY_LOWER_LIMIT:

        LOWER_LIMIT = CURRENT_NUMBER
        CURRENT_NUMBER = (LOWER_LIMIT + UPPER_LIMIT) // 2

      else:

        UPPER_LIMIT = CURRENT_NUMBER
        CURRENT_NUMBER = (LOWER_LIMIT + UPPER_LIMIT) // 2

      yield CURRENT_NUMBER


bt_gen = binary_tuning()

class GccFlagsTuner(MeasurementInterface):

  def manipulator(self):
    """
    Define the search space by creating a
    ConfigurationManipulator
    """
    manipulator = ConfigurationManipulator()
    manipulator.add_parameter(
      IntegerParameter('blockSize', 32, 1000))
    return manipulator

  def run(self, desired_result, input, limit):
    """
    Compile and run a given configuration then
    return performance
    """

    global time_taken

    cfg = desired_result.configuration.data
    cfg['blockSize'] = next(bt_gen)
    desired_result.configuration.data = cfg

    gcc_cmd = 'g++ test.cpp '
    gcc_cmd += f"-DBLOCK_SIZE={cfg['blockSize']}"
    gcc_cmd += ' -o test'

    compile_result = self.call_program(gcc_cmd)
    assert compile_result['returncode'] == 0

    run_cmd = './test'

    t1 = time.time()
    run_result = self.call_program(run_cmd)
    assert run_result['returncode'] == 0
    t2 = time.time()

    time_taken = t2 - t1

    print(f"\n==========\nBlock Size = {cfg['blockSize']}\nTime Taken = {time_taken}\n==========\n")

    return Result(time=run_result['time'])

  def save_final_config(self, configuration):
    """called at the end of tuning"""
    print("Optimal block size written to mmm_final_config.json:", configuration.data)
    self.manipulator().save_to_file(configuration.data, 'mmm_final_config.json')


if __name__ == '__main__':
  argparser = opentuner.default_argparser()
  GccFlagsTuner.main(argparser.parse_args())