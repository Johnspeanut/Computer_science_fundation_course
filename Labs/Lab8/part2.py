""" Student name:Team work
Team member: Jacqueline Guo, Yumeng An, Ruiqi Yang, Zihan Wang, Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Lab 8:
Part 2--write a new file that includes all positive reviews and another file
including negative reveiws. 
"""


def getReviewValue(line):
    '''
    Function -- getReviewValue
        Get review value from a line
    Parameters:
        line -- a string line with value at the end of the line
    Returns:
        Integer type value
    '''
    try:
        data = line.split("\t")
        return int(data[-1].strip())
    except IndexError:
        print("Error processing the file")
    except ValueError:
        print("Error processing the file")


def getComment(line):
    '''
    Function -- getComment
        Get comment from a line
    Parameters:
        line -- a string line with value at the end of the line
    Returns:
        String type comment
    '''
    try:
        data = line.split("0")
        data_remove = data[0].split("1")
        return data_remove[0].strip()
    except IndexError:
        print("Error processing the file")
    except ValueError:
        print("Error processing the file")


def main():
    isFile = False
    while not isFile:
        path = input("Enter the path to the IMDB dataset: ")
        dst_file_pos = open("positive2.txt", "w")
        dst_file_neg = open("negative2.txt", "w")
        try:
            with open(path, 'r') as file:
                isFile = True
                for line in file:
                    value = getReviewValue(line)
                    comment = getComment(line)
                    if value == 1:
                        dst_file_pos.write(comment + "\n")
                    else:
                        dst_file_neg.write(comment + "\n")
        except FileNotFoundError:
            print("File not found!")


if __name__ == "__main__":
    main()
