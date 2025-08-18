#import required packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import seaborn as sns
from PIL import Image
import sys

#user inputs
#run_folder=r"/net/ustc_01/users/lich/muon/results"
run_folder=r"/home/svenetia/sMDTcertification/online" # Use when generating txt file (makeDB.py) in personal folder
run_file=sys.argv[1]+".txt"
output_folder=r"/home/svenetia/sMDTcertification/output/indiv_chambers"+"/"+sys.argv[1]

def summary_hist(input_folder, input_file, save_folder):
    df = pd.read_csv(input_folder+"/"+input_file, delimiter=",")
    df=df.loc[(df['Resolution[um]']>0) & (df['Efficiency']>0)]
    df.hist(column=['T0[ns]', 'TMax[ns]',
        'ADC_peak[ns]', 'ADC_width[ns]', 'Resolution[um]', 'Efficiency'], bins=30, layout =(2,3), figsize= (15,5), color='skyblue', edgecolor='black', grid=False)
    title, throwaway=input_file.split(".txt")
    plt.suptitle(title)
    plt.savefig(save_folder+"/"+"hist.png", bbox_inches="tight")
    plt.close()

def heatmaps(input_folder, input_file, save_path):
    
    heatmap_files=[]
    df = pd.read_csv(input_folder+"/"+input_file, delimiter=",")
    df=df.loc[(df['Resolution[um]']>0) & (df['Efficiency']>0)]
    df_rename=df.rename(columns={"Column": "Tube Number"}, inplace=False)
    for col in ['T0[ns]', 'TMax[ns]',
        'ADC_peak[ns]', 'ADC_width[ns]', 'Resolution[um]', 'Efficiency']:

        #Create heatmap
        heatmap_data=df_rename.pivot_table(index=df_rename["Layer"], columns=df_rename["Tube Number"], values=col)
        dcol=5
        min=0
        max=df_rename["Tube Number"].max()
        nsteps=int(max/dcol)+1
        arr=np.linspace(min,max,nsteps, dtype=int)
        heatmap_sorted=heatmap_data.sort_values(by='Layer', ascending=False)
        plt.figure(figsize=(5,3))
        ax=plt.axes()
        plotting=sns.heatmap(heatmap_sorted, annot=False, cmap='viridis', ax=ax, )
        plotting.set_xticks(arr)
        plotting.set_xticklabels(list(map(str,arr)))
        title, throwaway=input_file.split(".txt")
        plotting.set_title(col + " " + title)
        plt.savefig(save_path+"/"+col+".png", bbox_inches="tight")
        plt.close()

        heatmap_files.append(col+".png")
    
    return heatmap_files

def concat_imgs(list_of_files, output_folder, columns, new_file_name):
    widths=[]
    heights=[]
    images=[]
    for i in list_of_files:
        img=Image.open(output_folder+"/"+i)
        images.append(img)
        w,h=img.size
        widths.append(w)
        heights.append(h)
    #print(widths)
    indiv_w=np.max(widths)
    indiv_h=np.max(heights)

    rows=rows=math.ceil(len(list_of_files)/columns)
    
    new_image=Image.new('RGB',(int(indiv_w*columns),int(indiv_h*rows)), (255,255,255))
    
    # put plots on new image
    for i in range(0,len(images)):
        #find row to populate
        new_row=math.floor(i/columns)

        #find col to populate
        new_col=math.ceil(i % columns)

        new_image.paste(images[i], ((new_col*indiv_w), (new_row*indiv_h)))

    # save
    new_image.save(output_folder+"/"+new_file_name+".png")

summary_hist(run_folder, run_file,output_folder)
file_list=heatmaps(run_folder, run_file, output_folder)
concat_imgs(file_list,output_folder,3,"heatmaps")
