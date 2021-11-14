import matplotlib.pyplot as plt
import pydicom
import sys

usage = "Usage: python preview.py dicom_filename"


def preview(file:str):
    ds = pydicom.dcmread(file)

    plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
    plt.show()
    pass


if __name__ == '__main__':

    if len(sys.argv) != 2:
        print("Please supply a dicom file name:\n")
        print(usage)
        sys.exit(-1)

    preview(sys.argv[1])