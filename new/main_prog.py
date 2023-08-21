import subprocess

def cmssw_part_1():

    with open('./results/info.txt', 'w') as file:

        file.write('part_1')

    with open('results/part_1/data.csv', 'w') as f:
        f.write('throughput,findClus,RawToDigi_kernel,kernelLineFit3,kernelLineFit4,kernel_connect,getHits,kernel_find_ntuplets,fishbone,clusterChargeCut,calibDigis,countModules,kernelFastFit3,kernelFastFit4,kernelFastFit5,kernelLineFit5,kernel_fillHitDetIndices,kernel_mark_used,finalizeBulk,kernel_earlyDuplicateRemover,kernel_countMultiplicity,kernel_fillMultiplicity,kernel_checkOverflows,initDoublets,kernel_classifyTracks,kernel_fishboneCleaner,kernel_fastDuplicateRemover,kernel_countHitInTracks,kernel_fillHitInTracks,kernel_tripletCleaner,kernel_doStatsForHitInTracks,kernel_doStatsForTracks\n')


    subprocess.run(['python3', 'main_tuner.py', '--test-limit=1000', '-t=Random_Search_Technique'])
    subprocess.run(['python3', 'xgb_ml.py', 'results/part_1', '60'])

    with open('./results/part_1/result.txt', 'r') as f1 , open('./results/part_2/kernels.txt', 'w') as f2:

        for line in f1:
            f2.write(line)

def cmssw_part_2():

    with open('./results/info.txt', 'w') as file:

        file.write('part_2')

    with open('./results/part_2/data.csv', 'w') as f1, open('./results/part_2/kernels.txt', 'r') as f2:

        header = 'throughput'

        for line in f2:
            header += ',' + line.strip()
        
        header += '\n'

        f1.write(header)

    subprocess.run(['python3', 'main_tuner.py', '--test-limit=300', '-t=Random_Search_Technique'])
    subprocess.run(['python3', 'xgb_ml.py', 'results/part_2', '30'])

    with open('./results/part_2/result.txt', 'r') as f1 , open('./results/part_3/top_5_kernels.txt', 'w') as f2:

        for line in f1:
            f2.write(line)


if __name__ == '__main__':

    cmssw_part_1()

    print('\n\nPart one of the program is done. The files result.txt and data.csv have been produced in results/part_1\n\n')

    cmssw_part_2()

    print('\n\nPart one of the program is done. The files result.txt, data.csv and kernels.txt have been produced in results/part_2\n\n')
    print(f'\n\nThe top 5 kernels are in results/part_3\n\n')
