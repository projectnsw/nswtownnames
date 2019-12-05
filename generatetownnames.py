import csv, shutil, os, sys

arg = sys.argv[1]

def main(arg):

    print("Generating town names...")
    if os.path.isfile(arg):
        newFileName = arg.split(".")[0] + ".nml"
        if os.path.isfile(newFileName): os.remove(newFileName)
        f=open(newFileName, '+w')
        with open(arg) as csvfile:
            namereader = csv.reader(csvfile)
            i = 0
            for row in namereader:
                if i == 0:
                    f.write('\t\ttext(\"{}\", 1)'.format(row[0].title()))
                    i = 1
                else:
                    f.write(',\n\t\ttext(\"{}\", 1)'.format(row[0].title()))
        f.close()
    else:
        print("csv file does not exist!")

if __name__ == "__main__":
    main(arg)