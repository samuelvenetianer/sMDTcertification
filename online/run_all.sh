#!/bin/bash

#testing again

if [ -d "/home/svenetia/sMDTcertification/output/indiv_chambers/$1" ]; then
    read -p "$1 does exist. Do you want to re-analyze the results? (y/n) " response
    if [ "$response" = "y" ]; then
        python pdf_maker.py $1
        echo "pdf_maker.py complete!"
        python pdf_maker_raw.py $1
        echo "pdf_maker_raw.py complete!"
        # python plots.py $1
        # echo "plots.py complete!"
        # python stats.py $1
        # echo "stats.py complete!"

        cd /home/svenetia/sMDTcertification/output/indiv_chambers/$1
        mod=$1
        zip_ext=".zip"
        txt_ext=".txt"
        results_path="/net/ustc_01/users/lich/muon/results/"
        txt_path="${results_path}${mod}${txt_ext}"
        # echo $txt_path

        txt_name="${mod}${txt_ext}"

        echo "copying text file!"
        cp $txt_path .

        echo "zipping files!"
        zip "${mod}${zip_ext}" all_spectra.pdf adc_spectra_raw.pdf heatmaps.png hist.png stats.txt $txt_name
    elif [ "$response" = "n" ]; then
        echo "OK, exiting now."
    else
        echo "That is not an option. Exiting now."
    fi
else
    mkdir /home/svenetia/sMDTcertification/output/indiv_chambers/$1
    echo "new directory created!"

    python pdf_maker.py $1
    echo "pdf_maker.py complete!"
    python pdf_maker_raw.py $1
    echo "pdf_maker_raw.py complete!"
    # python plots.py $1
    # echo "plots.py complete!"
    # python stats.py $1
    # echo "stats.py complete!"

    cd /home/svenetia/sMDTcertification/output/indiv_chambers/$1
    mod=$1
    zip_ext=".zip"
    txt_ext=".txt"
    results_path="/net/ustc_01/users/lich/muon/results/"
    txt_path="${results_path}${mod}${txt_ext}"

    txt_name="${mod}${txt_ext}"

    # echo "copying text file!"
    # cp $txt_path .

    echo "zipping files!"
    zip "${mod}${zip_ext}" all_spectra.pdf adc_spectra_raw.pdf heatmaps.png hist.png stats.txt $txt_name
fi
