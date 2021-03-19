import scipy, numpy, shutil, os, nibabel
import sys, getopt
import imageio
import extracting # распаковка gzip архива


def convert(inputfile):
    tmp_name = f"{inputfile}.nii"
    extracting.extract(inputfile, tmp_name) # распаковка
    outputfile = f"{inputfile.split('/')[-1]}_folder"
    inputfile = tmp_name.split('/')[-1]
    print('Input file is ', inputfile)
    print('Output folder is ', outputfile)
    # загрузка nii файла в виде массива
    image_array = nibabel.load(inputfile).get_data()
    # проверка, что данные точно трёхмерные
    if len(image_array.shape) == 3:
        nx, ny, nz = image_array.shape
        if not os.path.exists(outputfile):
            os.makedirs(outputfile)

        total_slices = image_array.shape[2]

        slice_counter = 0
        for current_slice in range(0, total_slices):
            if (slice_counter % 1) == 0:
                data = numpy.rot90(image_array[:, :, current_slice])
                if (slice_counter % 1) == 0 and ((current_slice == total_slices // 2) or (current_slice == total_slices // 2 - 1)):
                    image_name = inputfile[:-4] + "_z" + "{:0>3}".format(str(current_slice+1))+ ".png"
                    imageio.imwrite(image_name, data)
                    src = image_name
                    shutil.move(src, outputfile)
                    slice_counter += 1
    else:
        pass  
