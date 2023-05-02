class op_list:

    @staticmethod
    def indexOfmany(l:list, element):
        ind = []
        for i in range(len(l)):
            if l[i] == element:
                ind.append(i)
        return ind
    
    @staticmethod
    def same_elements(l:list):
        for i in range(1,len(l)):
            if l[i] == l[i-1]:
                if i == len(l)-1:
                    return True
                continue
            else:
                return False