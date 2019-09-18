The repository includes data cleaning scripts for the EAR annotation project.

In order to run the code:
- Download EAR folder from http://toos.usc.edu:5000/ using your account.
- From the downloaded EAR folder, move Data and Raw-Data folders to this EAR repository.

The raw data includes 4 datasets:
1- EAR1: CALM
2- EAR2: Breast_cancer
3- EAR3: DSE
4- EAR4: Aging

There are two scripts for extracting text data and generating json files. In order to generate the json files first extract the data from the raw text files using:

`python3 generate_datasets.py --sample <DATASET>`

Replace `<DATASET>` with the name of a corpus. There are four corpora in the raw dataset, and your options are CALM, Breast_Cancer, DSE and Aging 
The script extracts the text documents from the raw data file and generates a .csv file. The .csv file is stored in the corresponding folder under Data folder and has three columns: 
- user: the user id that appears in the original raw data.
- line: the raw data line that includes this document
- text: the short text document which is to be annotated

Afterwards, you can use the following command to generate the .json file in a format that is compatible with CSSL's annotation tool:

`python3 generate_json.py --sample <DATASET>`

Here again the `<DATASET>` is the name of a corpus. The script first removed the empyt lines from the .csv file and then generates the .json file.
The timestamp is set to a fixed time since this information is not provided in the dataset.

In order to upload the .json file to the annotation tool, compress the file and upload it to the annotation tool using "hate" parsing format.
