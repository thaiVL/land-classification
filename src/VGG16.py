import argparse

def parseargs():
    parser = argparse.ArgumentParser(prog="VGG16 Model",
                                     description="")
    parser.add_argument("-d", "--data_dir")
    parser.add_argument("-e", "--epoch")
    parser.add_argument("-b", "--batch_size")
    args = parser.parse_args()
    print(args.epoch)



if __name__ == "__main__":
    print(parseargs())