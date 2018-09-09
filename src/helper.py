from collections import defaultdict

def stock_store(file_path):
    '''
    Read the text file and store each entry in a
    dictionary with key as Time and value
    as another dictionary having key as Stock
    and value as Price
    '''
    dict_stock = defaultdict(dict)
    with open(file_path,'r') as f:
        for line in f:
            q = line.strip('\n').split('|')
            dict_stock[int(q[0])][q[1]] = float(q[2])
    return dict_stock

def max_hour(dict1):
    '''
    Run through the dictionary of actual.txt and finds the max hour entry
    '''
    max_value = next(iter(dict1.keys()))
    for i in dict1:
        if int(i) > max_value:
            max_value = int(i)
    return max_value

def min_hour(dict1):
    '''
    Run through the dictionary of actual.txt and finds the min hour entry
    '''
    min_value = next(iter(dict1.keys()))
    for i in dict1:
        if int(i) < min_value:
            min_value = int(i)
    return min_value

def sliding_windowsize(windowfile):
    '''
    Reads the window.txt file and returns the sliding window_size
    '''
    with open(windowfile,'r') as f:
        for line in f:
            window_size = line.strip('\n')
    return int(window_size[0])

def comparison(max_value,window_size,dict1,dict2,output_filepath):
    '''
    calculates the average error and writes to the
    output file with start and end hour
    '''
    start_hour = min_hour(dict1)
    end_hour = start_hour + (window_size - 1)
    while end_hour <= max_value:
        error = 0
        count = 0
        for i in range(start_hour,end_hour +1):
            for j in dict1[i]:
                if j in dict2[i]:
                    error += float(
                        format(
                            abs(dict1[i][j] - dict2[i][j]),'0.3f')
                    )
                    count += 1
        if count > 0:
            with open(output_filepath,'a') as f:
                f.write('{}|{}|{}\n'.format(
                    start_hour,
                    end_hour,
                    format(error/count, '0.2f')
                        )
                    )
        else:
            with open(output_filepath,'a') as f:
                f.write('{}|{}|{}\n'.format(start_hour,end_hour,'NA'))
        start_hour += 1
        end_hour = start_hour + (window_size - 1)


