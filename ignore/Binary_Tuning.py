from opentuner.search import technique
from mytime import time_taken

class Binary_Tuning(technique.SequentialSearchTechnique):
    def main_generator(self):

        mp = self.manipulator.params
        params = []

        for idx, param in enumerate(mp):

            params.append({})

            params[idx]['max'] = param.max_value
            params[idx]['min'] = param.min_value
            params[idx]['middle'] = (params[idx]['min'] + params[idx]['max']) // 2

        while True:

            for idx, param in enumerate(mp):

                yield params[idx]['max']
            
            time_taken_from_upper_limit = time_taken

            for idx, param in enumerate(mp):

                yield params[idx]['min']

            time_taken_from_lower_limit = time_taken

            if time_taken_from_upper_limit < time_taken_from_lower_limit:

                for idx, param in enumerate(mp):

                    params[idx]['min'] = params[idx]['middle']
                    params[idx]['middle'] =  (params[idx]['min'] + params[idx]['max']) // 2
            
            else:

                for idx, param in enumerate(mp):
                    
                    params[idx]['max'] = params[idx]['middle']
                    params[idx]['middle'] = (params[idx]['min'] + params[idx]['max']) // 2

            for idx, param in enumerate(mp):

                yield params[idx]['middle']

technique.register(Binary_Tuning())