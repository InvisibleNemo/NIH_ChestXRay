# NIH_ChestXRay
This repo contains codes to convert NIHChestXRay png images to numpy for easier computation

## Acknowledgements 

<i><b>(From Kaggle)</b> This work was supported by the Intramural Research Program of the NClinical Center (clinicalcenter.nih.gov) and National Library of Medicine (www.nlm.nih.gov).</i>

The datasets which are provided here are not owned by me. They are released under <a href=https://creativecommons.org/publicdomain/zero/1.0/>CC0: Public Domain License.</a>

The links to the converted datasets will be provided and will follow the same license guidelines. Any material published here is not endorsed by NIH. Please feel free to use this as you feel right.

## Motivation

This repo was created as I did not find any resources where I could download the said image dataset in a format which can be operated on with ease. The programs contained here are very simple conversion programs, feel free to use, modify, copy them as you deem fit.
The fully converted dataset will be published soon.

## Dataset Details
The following datasets are used in the programs which converted them into NumPy matrices for ease of use. The original datasets may be found in the following links:

### Original Data
1. Full Data:   https://www.kaggle.com/nih-chest-xrays/data                     ~42 GB
2. Sample Data: https://www.kaggle.com/nih-chest-xrays/sample                   ~ 2 GB
3. NIH Box:     https://nihcc.app.box.com/v/ChestXray-NIHCC/folder/36938765345

### Converted Data
1.  Sample Data (NumPy Format): <a href="https://buffalo.app.box.com/s/5qdzwn881ew5bj21kudaw05f6lgibkvn">Box</a>   ~5.5 GB
    <br>The above dataset is stored in tar split tar archives and should be combined to get the <b>npy</b> file. 
    To combine all the parts, download the 113 parts and run the following command:
    
    Combine all parts together
    ``` bash
    $cat nih_chest_xray_sample.tar.gz* > nih_chest_xray_sample.tar.gz
    ```
    Extract the <b>npy</b> file
    ``` bash
    $tar -xvf nih_chest_xray_sample.tar.gz
    ```

### Converted Labels
The chest X-ray images portray a probabilistic set of labels for the images. So there is no single label associated with each X-ray image. To circumvent this training issue in algorithms one hot encoding is used. The <a href="https://github.com/InvisibleNemo/NIH_ChestXRay/tree/master/files/sample_labels.csv">labels</a> file is converted using the <a href="https://github.com/InvisibleNemo/NIH_ChestXRay/tree/master/codes/one_hot_labels.py">one_hot_labels.py</a> code.
