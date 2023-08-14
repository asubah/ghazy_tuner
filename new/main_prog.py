import subprocess

def cmssw_part_1():

    with open('./results/info.txt', 'w') as file:

        file.write('part_1')

    subprocess.run(['python3', 'main_tuner.py', '--test-limit=1000', '-t=Random_Search_Technique'])
    subprocess.run(['python3', 'xgb_ml.py', 'resluts/part_1', '100'])

    #TODO: put into part_2 the list of top 15 kernels

def cmssw_part_2():

    with open('./results/info.txt', 'w') as file:

        file.write('part_2')

    subprocess.run(['python3', 'main_tuner.py', '--test-limit=300', '-t=Random_Search_Technique'])
    subprocess.run(['python3', 'xgb_ml.py', 'resluts/part_2', '10'])

    #TODO: put into part_3 the top 5 kernels

def cmssw_part_3():

    pass

    #TODO: show what are the top 5 kernels


if __name__ == '__main__':

    cmssw_part_1()
    cmssw_part_2()
    cmssw_part_3()
