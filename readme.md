# developed by : https://github.com/000-ghost-000
visit https://www.kaggle.com/
and signup  with your google account 
then after signup visit your profile and sellect the settings 
in the settings you will find the API option 
## create new API  key and copy the API key
https://www.kaggle.com/settings


paste/download the  API key 
### if using Mac/Linux
```bash

mkdir -p ~/.kaggle
mv ~/Downloads/kaggle.json ~/.kaggle/
chmod 600 ~/.kaggle/kaggle.json  # Set permissions to secure the file
```
### if using Windows
Move the kaggle.json file to the C:\Users\<Your Username>\.kaggle\ directory.

    Create the .kaggle folder if it doesn't exist.
    Move the kaggle.json file into the folder

##### the downloaded API should be present in ~/.config/kaggle/kaggle.json file structure if using Mac/Linux

#### install all the dependencies by  running the following command
``` python

pip install -r requirements.txt
```
#### run the script using 
``` python

python main.py
```
##### file structure
``` bash

kaggle_data_extractor/
├── data/                 # Directory for storing downloaded datasets
├── main.py               # Main script for downloading and loading the dataset
├── requirements.txt      # List of dependencies for the project
└── README.md             # Optional: Instructions for the project
```
