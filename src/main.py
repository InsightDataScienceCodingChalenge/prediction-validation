from collections import defaultdict
from misc_utils import parse_command_line
dict1 = defaultdict(dict)
dict2 = defaultdict(dict)

def stock_store(actualfile,predictedfile):
    '''
    Read the text file and store each entry in a dictionary with key as Time and value
    as another dictionary having key as Stock and value as Price
    '''
    with open(actualfile,'r') as f:
        for line in f:
            q = line.strip('\n').split('|')
            dict1[int(q[0])][q[1]] = float(q[2])
    with open(predictedfile,'r') as f:
        for line in f:
            s = line.strip('\n').split('|')
            dict2[int(s[0])][s[1]] = float(s[2])
    return dict1,dict2

def max_hour(dict1):
    '''
    Run through the dictionary of actual.txt and finds the max hour entry
    '''
    max = 1
    for i in dict1:
        if int(i) > max:
            max = int(i)
    return max

def sliding_windowsize(windowfile):
    '''
    Reads the window.txt file and returns the sliding window_size
    '''
    with open(windowfile,'r') as f:
        for line in f:
            window_size = line.strip('\n')
    return int(window_size[0])

def comparision(max,window_size,dict1,dict2,output_filepath):
    '''
    calculates the average error and writes to the output file with start and end hour
    '''
    start_hour = 1
    end_hour = start_hour + (window_size - 1)
    while end_hour <= max:
        error = 0
        count = 0
        for i in range(start_hour,end_hour +1):
            for j in dict1[i]:
                if j in dict2[i]:
                    error += round(abs(dict1[i][j] - dict2[i][j]),3)
                    count += 1
        if count > 0:
            with open(output_filepath,'a') as f:
                f.write('{}|{}|{}\n'.format(start_hour,end_hour,round(error/count,2)))
        else:
            with open(output_filepath,'a') as f:
                f.write('{}|{}|{}\n'.format(start_hour,end_hour,'NA'))
        start_hour += 1
        end_hour = start_hour + (window_size - 1)

def main(windowfile_path,actualfile_path,predictedfile_path,output_file_path):
    dict1,dict2 = stock_store(actualfile_path,predictedfile_path)
    max = max_hour(dict1)
    window_size = sliding_windowsize(windowfile_path)
    comparision(max,window_size,dict1,dict2,output_file_path)

if __name__ == "__main__":
    ARGS = parse_command_line()
    input_windowfile_path = ARGS.input_window_path
    input_actualfile_path = ARGS.input_actual_path
    input_predictedfile_path = ARGS.input_predicted_path
    output_file_path = ARGS.output_file_path
    main(input_windowfile_path,input_actualfile_path,input_predictedfile_path,output_file_path)


