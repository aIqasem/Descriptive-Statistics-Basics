import math
from op_list import op_list

class DescriptiveStatistics:
    @staticmethod
    def Median(n:list):
        if len(n) %2 == 0:
            m1_index = (len(n) / 2) - 1
            m2_index = m1_index + 1
            m = ( n[int(m1_index)] + n[int(m2_index)] ) / 2
        else:
            m_index = (len(n)+1) / 2 - 1
            m = n[int(m_index)]
        return m
    
    @staticmethod
    def five_number_summary(numbers:list):
        sorted_list = sorted(numbers)

        max = sorted_list[-1]
        min = sorted_list[0]

        if len(numbers) %2 == 0:
            m1_index = (len(sorted_list) / 2) - 1
            m2_index = m1_index + 1
            m = ( sorted_list[int(m1_index)] + sorted_list[int(m2_index)] ) / 2
            q1 = DescriptiveStatistics.Median(sorted_list[0:int(m1_index)+1])
            q3 = DescriptiveStatistics.Median(sorted_list[int(m2_index):])
        else:
            m_index = (len(numbers)+1) / 2 - 1
            m = sorted_list[int(m_index)]
            q1 = DescriptiveStatistics.Median(sorted_list[0:int(sorted_list.index(m))])
            q3 = DescriptiveStatistics.Median(sorted_list[int(sorted_list.index(m))+1:])

        return f"Five Number Summary:\n max: {max}\n min: {min}\n 1st quartile: {q1}\n 2nd quartile (Median): {m}\n 3rd quartile: {q3}\n range: {max-min}\n Interquartile range: {q3-q1}"
    

    def mean(numbers:list):
        sum = 0
        for i in range(len(numbers)):
            sum += numbers[i]
        return sum/len(numbers)
    
    def variance_p(numbers:list):
        mean = DescriptiveStatistics.mean(numbers)
        sum = 0
        for i in range(len(numbers)):
            sum += math.pow(numbers[i] - mean, 2)
        return sum/len(numbers)
    
    def standard_deviation_p(numbers:list):
        v = DescriptiveStatistics.variance(numbers)
        return math.pow(v,0.5)
    
    def mode(numbers:list):

        if op_list.same_elements(numbers):
            return f"no mode, the given list consists of equal elements (all elements = {numbers[0]})"
        
        d = {}
        for i in range(len(numbers)):
            d[numbers[i]] = d.get(numbers[i],0) + 1
        k_d = list(d.keys())
        v_d = list(d.values())
        max = sorted(v_d)[-1] # = mode value
        modes = []
        ind = [] #indexes of modes 

        for i in d:
            if d[i] == max:
                modes.append(i)
        for i in range(len(modes)):
            ind.append(op_list.indexOfmany(numbers,modes[i]))
        
        if len(modes) * max == len(numbers):
            return f"no mode, (all elements occurred {max} times)"

        if len(modes) > 1:
            re = f"mode value: {max}, modes are:\n"
            for i in range(len(modes)):
                re += f"{modes[i]} at: {ind[i]}\n"
            return re

        if len(modes) == 1:
            re = f"mode value: {max}, mode is:\n"
            for i in range(len(modes)):
                re += f"{modes[i]} at: {ind[i]}"
            return re