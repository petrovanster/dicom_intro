import pydicom
from pydicom.data import get_testdata_file
import matplotlib.pyplot as plt
from pydicom.uid import ExplicitVRLittleEndian
from pydicom.encaps import encapsulate
import io



def preview(ds:pydicom.Dataset):
    plt.imshow(ds.pixel_array, cmap=plt.cm.gray)
    plt.show()
    pass


if __name__=="__main__":
    ds = pydicom.dcmread(get_testdata_file('MR_small_jpeg_ls_lossless.dcm'))
    print(ds.file_meta)
    #preview(ds)

    ds.convert_pixel_data('gdcm')

    with io.BytesIO() as output:
        output.write(ds.pixel_array)
        frame = output.getvalue()

    ds.file_meta.TransferSyntaxUID = ExplicitVRLittleEndian    
    ds.PixelData = encapsulate([frame])
    
    ds.save_as("decoded.dcm")
    pass