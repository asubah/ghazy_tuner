import subprocess

def cmssw_part_1():

    with open('./results/info.txt', 'w') as file:

        file.write('part_1')

    with open('results/part_1/data.csv', 'w') as f:
        f.write('throughput,findClus,RawToDigi_kernel,kernelLineFit3,kernelLineFit4,kernel_connect,getHits,kernel_find_ntuplets,fishbone,clusterChargeCut,calibDigis,countModules,kernelFastFit3,kernelFastFit4,kernelFastFit5,kernelLineFit5,kernel_fillHitDetIndices,kernel_mark_used,finalizeBulk,kernel_earlyDuplicateRemover,kernel_countMultiplicity,kernel_fillMultiplicity,kernel_checkOverflows,initDoublets,kernel_classifyTracks,kernel_fishboneCleaner,kernel_fastDuplicateRemover,kernel_countHitInTracks,kernel_fillHitInTracks,kernel_tripletCleaner,kernel_doStatsForHitInTracks,kernel_doStatsForTracks\n')


    # subprocess.run(['python3', 'main_tuner.py', '--test-limit=1000', '-t=Random_Search_Technique'])
    subprocess.run(['python3', 'main_tuner.py', '--test-limit=230724', '-t=Random_Search_Technique'])
    subprocess.run(['python3', 'xgb_ml.py', 'resluts/part_1', '100'])


    #TODO: put into part_2 the list of top 15 kernels

    with open('./results/part_1/result.txt', 'r') as f1 and open('./results/part_2/kernels.txt', 'w') as f2:

        f2.write(f1.readline())

def cmssw_part_2():

    with open('./results/info.txt', 'w') as file:

        file.write('part_2')

    subprocess.run(['python3', 'main_tuner.py', '--test-limit=300', '-t=Random_Search_Technique'])
    subprocess.run(['python3', 'xgb_ml.py', 'resluts/part_2', '10'])

    #TODO: put into part_3 the top 5 kernels

    with open('./results/part_2/result.txt', 'r') as f1 and open('./results/part_3/kernels.txt', 'w') as f2:

        f2.write(f1.readline())

def cmssw_part_3():

    pass

    #TODO: show what are the top 5 kernels


if __name__ == '__main__':

    cmssw_part_1()
    # cmssw_part_2()
    # cmssw_part_3()
