""" Student name:Qiong Peng
NUID: 001559637
CS5001 Section 4, Fall 2020
Instructor: Dr.Abi Evans and Andrew Jelani
Lab 7
Part one: Decrypt an Unknown message
Develop an algorithm that can figure out meaning of original message. 
"""


def decrypt(str, shift, slide):
    '''
    Function -- decrypt
    Decrypt string type message given shift and slide
    Parameter:
    shift -- number of shift to left direction
    slide -- number of slide to left direction
    Return -- the decrypted message. String type.
    '''

    new_str = ""
    for i in range(len(str)):
        new_str += chr(ord(str[i]) - shift)
    slide_str =[None] * len(new_str)
    for j in range(len(new_str)):
        slide_str[j - slide] = new_str[j]
    return ''.join(slide_str)


def main():
    lst = ["*.glygo rsvvmw'w gshi avmxiw gsqqirxw efsyx *lmq", "aqwuvwem, kp c\
        p kphkpkvg nqqr, ykvj","sjajw ywzxy f htruzyjw dtz hfs’y ymwtb tzy f b\
            nsitb", "yko.vjg swguvkqp qh yjgvjgt eqorwvgtu ecp vjkpm ku nkmg \
            vjg swguvkqp qhyjgvjgt uwdoctkpgu ecp u",".ejwem pqttku ytkvgu dqq\
            ngcp gzrtguukqpu vjcv ctg dqvj vtwg cpf hcnug" ]
    for k in range(len(lst)):
        str = lst[k]
        print("**************************************************************")
        for i in range(1, 6):
            for j in range(1, 10):
                print(decrypt(str, i, j))
                print("i = ",i,"and j = ",j)

    # print(decrypt("tfbu nz tipsu", 1, 1))


if __name__ == "__main__":
    main()
