from PIL import Image
import os
import numpy as np
import math
import matplotlib.pyplot as plt
from natsort import natsorted
import sys

#Specify paths

base_folder = r"/net/ustc_01/users/lich/muon/results"
t0_untitled = base_folder +"/"+sys.argv[1]                             # general results folder
t0_titled = r"/home/svenetia"+"/"+sys.argv[1] 
summary_folder = r"/home/svenetia"+"/"+sys.argv[1]

# base_folder = r"C:\Users\svene\OneDrive\Documents\Tufts\Research\qual"
# t0_untitled = base_folder +"\\"+sys.argv[1]                                                               # general results folder
# t0_titled = r"C:\Users\svene\OneDrive\Documents\Tufts\Research\qual\test_output"+"\\"+sys.argv[1]         # folder to save titled pngs & summary png pages
# summary_folder = r"C:\Users\svene\OneDrive\Documents\Tufts\Research\qual\test_output"+"\\"+sys.argv[1]    # folder to save scrollable pdf

widths=[]
heights=[]
folders=[]

# first, get list of folders and choose only tdc folders
all_files_folders= os.listdir(t0_untitled)

# make list of only the folders that have spectra in them
for i in all_files_folders:
    if "Time_Spectrum" in i:
        folders.append(i)

# loop through folders and perform png extraction

for j in folders:

    print("Searching through folder for "+ j)
    pngs=[]
    images =[]
    iter=0

    #construct full folder:

    full = t0_untitled+"/"+j
    #print(full)

    #get list of files
    all_files= os.listdir(full)
    
    #print(all_files)

    #make list of only correct ADC and TDC spec
    for k in all_files:
        #if "adc_time_spectrum.png" in k or "tdc_time_spectrum_raw.png" in k:
        if "adc_time_spectrum.png" in k: 
            pngs.append(k)

    print("Number of pngs of interest: "+ str(len(pngs)))

    #re-order files
    sorted_files=natsorted(pngs)

    #pull size
    for L in sorted_files:
        img=Image.open(full+"/"+L)
        images.append(img)
        w,h=img.size
        widths.append(w)
        heights.append(h)

    indiv_w=np.max(widths)
    indiv_h=np.max(heights)

    rows=3
    cols=4
    img_per_page=rows*cols

    pages=math.ceil(len(images)/(rows*cols))

    print("Concatenating spectra for "+ j)

    for m in range(1, pages+1):
        new_image=Image.new('RGB',(int(indiv_w*cols),int(indiv_h*rows)), (255,255,255))
        restart_counter=0

        for n in range(iter,iter+img_per_page):
            if n<=len(images)-1:

                #find row to populate
                new_row=math.floor(restart_counter/cols)

                #find col to populate
                new_col=math.ceil(restart_counter % cols)

                new_image.paste(images[n], ((new_col*indiv_w), (new_row*indiv_h)))
                restart_counter+=1
            else:
                pass
        new_image.save(t0_titled+"/"+j+"_summary"+str(m)+".png")
        print("page", m, "completed")
        iter+=img_per_page

print("Summary spectra saved!")
print("Generating .pdf file...")

#1 img per page

img_to_cat=[]

imgs= os.listdir(t0_titled)

for i in imgs:
    if "Time_Spectrum_summary" in i:
        img_to_cat.append(i)
img_to_cat=natsorted(img_to_cat)

images = [
    Image.open(t0_titled+"/" + f)
    for f in img_to_cat
]

pdf_path = t0_titled+"/"+ "adc_spectra_raw.pdf"

images[0].save(
    pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
)

print("PDF saved!")
print("done!")
