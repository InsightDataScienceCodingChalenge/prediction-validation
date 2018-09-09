from collections import defaultdict
from misc_utils import parse_command_line
from helper import stock_store,max_hour,sliding_windowsize,comparison


def main(windowfile_path,actualfile_path,predictedfile_path,output_file_path):
    '''
    It executes the whole algo step by step
    '''
    dictstock_actual = stock_store(actualfile_path)
    dictstock_predicted = stock_store(predictedfile_path)
    max_value = max_hour(dictstock_actual)
    window_size = sliding_windowsize(windowfile_path)
    comparison(max_value,
                window_size,
                dictstock_actual,
                dictstock_predicted,
                output_file_path)

if __name__ == "__main__":
    ARGS = parse_command_line()
    input_windowfile_path = ARGS.input_window_path
    input_actualfile_path = ARGS.input_actual_path
    input_predictedfile_path = ARGS.input_predicted_path
    output_file_path = ARGS.output_file_path
    main(input_windowfile_path,
         input_actualfile_path,
         input_predictedfile_path,
         output_file_path)


