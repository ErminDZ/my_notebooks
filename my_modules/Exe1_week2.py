import argparse
if __name__ == '__main__':
    parser= argparse.ArgumentParser(description='A program that downloads a URL and stores it locally')
    parser.add_argument('filePath', help='The File path to process')
    parser.add_argument('fileName',  help='The name of the file to process')
    args = parser.parse_args()
    print('FILE PATH:', args.filePath)
    print('FILE NAME:', args.fileName)
    

def print_file_content(file):
    import csv

    filename = 'something.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        
        for row in reader:
            print(' '.join(row))
            

def write_list_to_file(output_file, lst):
    import csv
    import platform


    if platform.system() == 'Windows':
        newline=''
    else:
        newline=None

    with open('output.csv', 'w', newline=newline) as output_file:
        output_writer = csv.writer(output_file)

        output_writer.writerow(['2015', '1', '0', '5100', '614,5'])
        output_writer.writerow(['2015', '1', '0', '5104', '2,3'])
        output_writer.writerow(['2015', '1', '0', '5106', '1'])
        output_writer.writerow(['2015', '1', '0', '5110', '1'])
        

def read_csv(input_file):
    import csv

    with open('input.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    print(data)

def testcli()
    import argparse
    
    if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A program that reads from one file and writes to another')
    parser.add_argument('url', help='The URL to process')
    parser.add_argument('-d', '--destination', help='The name of the file to store the url in')

    args = parser.parse_args()
    print('URL:', args.url)
    print('Destination:', args.destination)