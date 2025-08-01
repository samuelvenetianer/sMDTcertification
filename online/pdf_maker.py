from PIL import Image
import os
import numpy as np
import math
import matplotlib.pyplot as plt
from natsort import natsorted
import sys

#Specify paths

t0_untitled = r"/net/ustc_01/users/lich/muon/results"+"/"+sys.argv[1]+"/"+"T0Fits" #folder with Chihao's T0 fits
t0_titled = r"/home/svenetia/sMDTcertification/output/indiv_chambers"+"/"+sys.argv[1] #folder to save titled pngs & summary png pages
summary_folder = r"/home/svenetia/sMDTcertification/output/indiv_chambers"+"/"+sys.argv[1] #folder to save scrollable pdf

widths=[]
heights=[]
pngs=[]
images=[]
iter=0

#get list of files
all_files= os.listdir(t0_untitled)

#make list of only pngs
for i in all_files:
    if "TestData" in i:
        pngs.append(i)

print("Adding titles to spectra...this might take a while...")

#turn all pngs into images
for i in pngs:
    img=Image.open(t0_untitled+"/"+i)

    #add title
    fig,ax=plt.subplots()
    ax.imshow(img)
    ax.set_axis_off()

    #construct new title
    throwaway, keep=i.split("TestData_")
    keep, throwaway=keep.split("_time_spectrum")
    ax.set_title(keep)
    full_path=t0_titled+"/"+keep+".png"
    plt.savefig(full_path, bbox_inches="tight", dpi=300)
    plt.close()

titled=[]

print("Sorting files...")
#get list of titled files and sort them by name
titled_files= os.listdir(t0_titled)

#make list of only pngs
for i in titled_files:
    if "tdc" in i:
        titled.append(i)

#re-order files
sorted_files=natsorted(titled)
#print(sorted_files)

for i in sorted_files:
    img=Image.open(t0_titled+"/"+i)
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

print("New spectra saved!")
print("Concatenating spectra...")

for i in range(1, pages+1):
    new_image=Image.new('RGB',(int(indiv_w*cols),int(indiv_h*rows)), (255,255,255))
    restart_counter=0

    for j in range(iter,iter+img_per_page):
        if j<=len(images)-1:

            #find row to populate
            new_row=math.floor(restart_counter/cols)

            #find col to populate
            new_col=math.ceil(restart_counter % cols)

            new_image.paste(images[j], ((new_col*indiv_w), (new_row*indiv_h)))
            restart_counter+=1
        else:
            pass
    new_image.save(t0_titled+"/"+"fitsummary"+str(i)+".png")
    print("page", i, "completed")
    iter+=img_per_page

print("Summary spectra saved!")
print("Generating .pdf file...")
#1 img per page

img_to_cat=[]

imgs= os.listdir(t0_titled)

for i in imgs:
    if "fitsummary" in i:
        img_to_cat.append(i)
img_to_cat=natsorted(img_to_cat)

images = [
    Image.open(t0_titled+"/" + f)
    for f in img_to_cat
]

pdf_path = t0_titled+"/"+ "all_spectra.pdf"
    
images[0].save(
    pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
)

print("PDF saved!")
print("done!")
