#import required packages
import pandas as pd
import sys

#user inputs
#run_folder=r"/net/ustc_01/users/lich/muon/results"
run_folder=r"/home/svenetia/sMDTcertification/online" # Use when generating txt file (makeDB.py) in personal folder
run_file=sys.argv[1]+".txt"
output_folder=r"/home/svenetia/sMDTcertification/output/indiv_chambers"+"/"+sys.argv[1]

#Choose run of interest
def calc_stats_txt(input_txt_folder,input_txt_file, output_txt_folder):

    # import txt file as df
    df = pd.read_csv(input_txt_folder+"/"+input_txt_file, delimiter=",") #import txt file

    # check for dead tubes
    with open(output_txt_folder+"/"+"stats.txt", "w") as file:
        file.write("Stats for: "+ input_txt_file+'\n')
        file.write("\n") 
        if len(df.loc[(df['Resolution[um]']==0) & (df['Efficiency']==0)]) > 0:
            number=len(df.loc[(df['Resolution[um]']==0) & (df['Efficiency']==0)])
            file.write(str(number) + " dead tubes are suppressed.\n")
            file.write("\n")
            file.write("Dead Tubes:\n")
            #display(df.loc[(df['Resolution[um]']==0) & (df['Efficiency']==0)])
            df_dead=df.loc[(df['Resolution[um]']==0) & (df['Efficiency']==0)]
            df_string = df_dead.to_string(header=True, index=False)
            file.write(df_string + '\n')
            file.write("\n")
        else:
            file.write("There are no dead tubes.\n")
            file.write("\n")

    # find stats for only alive tubes
    df=df.loc[(df['Resolution[um]']>0) & (df['Efficiency']>0)] #select alive tubes
    mins=df.min().to_frame()
    mins.columns=["Min"]
    maxes=df.max().to_frame()
    maxes.columns=["Max"]
    means=df.mean().to_frame()
    means.columns=["Mean"]
    summary=pd.concat([mins,maxes,means],axis=1)
    summary=summary.drop(labels=["Column", "Layer", "TDC_id", "TDC_Ch_id"], axis=0, inplace=False)
    
    with open(output_txt_folder+"/"+"stats.txt", 'a') as f:
        f.write("Statistics (excluding dead tubes):\n")
        df_string = summary.to_string(header=True, index=True)
        f.write(df_string + '\n')

    #summary.to_csv('output.txt', sep='\t', index=True)

    return

avgs=calc_stats_txt(run_folder, run_file, output_folder)
