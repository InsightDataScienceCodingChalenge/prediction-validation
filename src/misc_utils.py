'''
Parse command line arguments
'''

import argparse

def parse_command_line() -> argparse.Namespace:
    '''Return parsed arguments from the command line'''
    parser = argparse.ArgumentParser('script for parsing commandline args')

    parser.add_argument(
        '-input_file1_path',
        help='inputfilepath for sliding window_size',
        dest='input_window_path',
    )

    parser.add_argument(
        '-input_file2_path',
        help='inputfilepath for actual stock values',
        dest='input_actual_path'
    )

    parser.add_argument(
        '-input_file3_path',
        help='inputfilepath for predicted stock values',
        dest='input_predicted_path'
    )

    parser.add_argument(
        '-output_file_path',
        help='outputfilepath to generate average error values',
        dest='output_file_path',
    )
    return parser.parse_args()
