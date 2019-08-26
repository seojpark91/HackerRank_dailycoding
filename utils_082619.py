import glob
import os.path
import shutil


def hex_to_int(hex_num):
    """
    convert hex color codes to rgb decimal code
    
    parameter: hexidecimal number i.e.: "#c1a68f"
    """
    return [int(hex_num[i:i + 2], 16) for i in (1, 3, 5)]
    
def convert_to_min(millisec):
    """
    convert milliseconds to minutes and seconds and outputs string value
    """
    minutes, seconds = divmod(millisec / 1000, 60)
    return f'{minutes:0>2.0f}:{seconds:.2f}'
    
