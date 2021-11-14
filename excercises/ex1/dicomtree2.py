import pydicom



def recurse_tree(dataset, level = 0):
    # order the dicom tags
    for data_element in dataset:
        
        print(f"{'  ' * level} {str(data_element)}")
        if data_element.VR == "SQ":  # a sequence
            for dataset in data_element.value:
                recurse_tree(dataset, level + 1)

ds = pydicom.dcmread("data/democases/case1/case1_008.dcm")

recurse_tree(ds)