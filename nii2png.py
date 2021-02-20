import scipy, numpy, shutil, os, nibabel
import sys, getopt
import imageio
import extracting


def convert(inputfile):
    tmp_name = f"{inputfile}.nii"
    extracting.extract(inputfile, tmp_name)
    outputfile = f"{inputfile.split('/')[-1]}_folder"
    inputfile = tmp_name.split('/')[-1]
    print('Input file is ', inputfile)
    print('Output folder is ', outputfile)
    # set fn as your 4d nifti file
    image_array = nibabel.load(inputfile).get_data()
    # if 4D image inputted
    if len(image_array.shape) == 4:
        # set 4d array dimension values
        nx, ny, nz, nw = image_array.shape
        # set destination folder
        if not os.path.exists(outputfile):
            os.makedirs(outputfile)
        total_volumes = image_array.shape[3]
        total_slices = image_array.shape[2]
        # iterate through volumes
        for current_volume in range(0, total_volumes):
            slice_counter = 0
            # iterate through slices
            for current_slice in range(0, total_slices):
                if (slice_counter % 1) == 0 and ((current_volume == total_volumes // 2) or (current_volume == total_volumes // 2 - 1)):
                    data = numpy.rot90(image_array[:, :, current_slice, current_volume])
                    #alternate slices and save as png
                    image_name = inputfile[:-4] + "_" + str(current_volume) + ".png"
                    imageio.imwrite(image_name, data)

                    #move images to folder
                    src = image_name
                    shutil.move(src, outputfile)
                    slice_counter += 1

    # else if 3D image inputted
    elif len(image_array.shape) == 3:
        # set 4d array dimension values
        nx, ny, nz = image_array.shape

        # set destination folder
        if not os.path.exists(outputfile):
            os.makedirs(outputfile)

        total_slices = image_array.shape[2]

        slice_counter = 0
        # iterate through slices
        for current_slice in range(0, total_slices):
            # alternate slices
            if (slice_counter % 1) == 0:
                # rotate or no rotate
                data = numpy.rot90(image_array[:, :, current_slice])
                        

                #alternate slices and save as png
                if (slice_counter % 1) == 0 and ((current_slice == total_slices // 2) or (current_slice == total_slices // 2 - 1)):
                    image_name = inputfile[:-4] + "_z" + "{:0>3}".format(str(current_slice+1))+ ".png"
                    imageio.imwrite(image_name, data)

                    #move images to folder
                    src = image_name
                    shutil.move(src, outputfile)
                    slice_counter += 1
    else:
        pass  
