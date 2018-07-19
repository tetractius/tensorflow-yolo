#!/usr/bin/env python

# import sys
import os
import argparse
import logging

log = logging.getLogger('preprocess_chinese_data')
log.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
general_format = \
    logging.Formatter(
        '%(asctime)s - %(thread)d - %(name)s - %(levelname)s: %(message)s')
streamHandler.setFormatter(general_format)
log.addHandler(streamHandler)

################################################################
# ATTENTION it is currently is hacked to prepare training data
# for AA-机
################################################################


def run():
    parser = argparse.ArgumentParser(
        description="Process chinese character to "
                    "create YOLO input files")

    parser.add_argument("--root_path",
                        type=str,
                        required=True,
                        help="Root path of the chinese data set")

    args = parser.parse_args()

    with open(os.path.join('data', 'chinese_labels.csv'), "w") \
            as csv_chinese_labels_file, \
            open(os.path.join('data', 'chinese_labels.yolo'), "w") \
                    as yolo_chinese_labels_file:

        header = ["SYMBOL",
                  "DEC_CODE_POINT",
                  "HEX_CODE_POINT",
                  "RELATIVE_PATH"]

        csv_chinese_labels_file.write(', '.join(header))

        # Path of CharactersTrimPad28, AA-机
        chinese_symbols_root = os.path.join(args.root_path,
                                            'CharactersTrimPad28',
                                            'AA-机')
        log.info("Preparing to walk through: ")
        log.info(chinese_symbols_root)

        for root, dirs, files in os.walk(chinese_symbols_root):

            process_chinese_symbol_record(csv_chinese_labels_file,
                                          files,
                                          root,
                                          yolo_chinese_labels_file,
                                          20,
                                          '机')

        # Path of CharactersTrimPad28, BB-饮
        chinese_symbols_root = os.path.join(args.root_path,
                                            'CharactersTrimPad28',
                                            'BB-饮')
        log.info("Preparing to walk through: ")
        log.info(chinese_symbols_root)

        for root, dirs, files in os.walk(chinese_symbols_root):

            process_chinese_symbol_record(csv_chinese_labels_file,
                                          files,
                                          root,
                                          yolo_chinese_labels_file,
                                          21,
                                          '饮')


def process_chinese_symbol_record(csv_chinese_labels_file,
                                  files,
                                  root,
                                  yolo_chinese_labels_file,
                                  yolo_hack_class_value,
                                  hack_symbol='机'):
    n_samples = len(files)
    print(n_samples)
    for file in files:
        file_path = os.path.join(root, file)
        symbol = os.path.split(root)[-1]
        symbol = hack_symbol
        if 1 != len(symbol):
            continue
        record = [str(symbol), str(ord(symbol)), str(hex(ord(symbol))),
                  file_path]
        csv_chinese_labels_file.write(', '.join(record) + '\n')
        yolo_chinese_labels_file.write('{} {} {} {} {} {} \n'
                                       .format(file_path,
                                               0, 0, 27, 27,
                                               yolo_hack_class_value))

        print(n_samples)
        n_samples -= 1


if __name__ == "__main__":
    run()
    pass

