from collections import defaultdict

def stock_store(file_path):
    '''
    Read the text file and store each entry in a
    dictionary with key as Time and value
    as another dictionary having key as Stock
    and value as Price
    :param file_path --> path of the file of stock data
    '''
    dict_stock = defaultdict(dict)
    with open(file_path,'r') as f:
        for line in f:
            q = line.strip('\n').split('|')
            dict_stock[int(q[0])][q[1]] = float(q[2])
    return dict_stock

def max_hour(dictstock_actual):
    '''
    Run through the dictionary of actual.txt and finds the max hour entry
    :param dictstock_actual-->dictionary with stock entries of actual text file
    '''
    max_value = next(iter(dictstock_actual.keys()))
    for i in dictstock_actual:
        if int(i) > max_value:
            max_value = int(i)
    return max_value

def min_hour(dictstock_actual):
    '''
    Run through the dictionary of actual.txt and finds the min hour entry
    :param dictstock_actual-->dictionary with stock entries of actual text file
    '''
    min_value = next(iter(dictstock_actual.keys()))
    for i in dictstock_actual:
        if int(i) < min_value:
            min_value = int(i)
    return min_value

def sliding_windowsize(windowfile):
    '''
    Reads the window.txt file and returns the sliding window_size
    :param windowfile-->path of the sliding window text file.
    '''
    with open(windowfile,'r') as f:
        for line in f:
            window_size = line.strip('\n')
    return int(window_size[0])

def comparison(max_value,
               window_size,
               dictstock_actual,
               dictstock_predicted,
               output_filepath):
    '''
    calculates the average error and writes to the
    output file with start and end hour
    :param max_value --> maximum hour entry in the actual stock data file
    :param dictstock_actual --> dictionary having entries of actual text file
    :param dictstock_predicted --> dictionary having entries of predicted file
    :param output_filepath --> path of the output file to be generated
    '''
    start_hour = min_hour(dictstock_actual)
    end_hour = start_hour + (window_size - 1)
    while end_hour <= max_value:
        error = 0
        count = 0
        for i in range(start_hour,end_hour +1):
            for j in dictstock_actual[i]:
                if j in dictstock_predicted[i]:
                    error += float(
                        format(
                            abs(dictstock_actual[i][j] -
                                dictstock_predicted[i][j]),'0.3f')
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



