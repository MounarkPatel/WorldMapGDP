# WorldMapGDP
Two-part project that uses the same GDP data found in GDP_XY_plots to create plots on the world map. This project investigates two ways to clean and unify multiple sets of data. The first way is done with filtering data through country names (WorldPlot1.py) and the second way through country codes (WorldPlot2.py). Doing the scripting with country codes improves the quality of the wolrd map becuase it creates better mapping from pygal country codes to World Bank country names. This comes at the price of having less efficent code and code that is harder to follow. 
# Installing Python 3
Install python 3. 
Preffered Method: 
python3 with anaconda(https://www.anaconda.com/download/#macos)
#
OS X: 
http://docs.python-guide.org/en/latest/starting/install3/osx/
#
Windows: 
http://docs.python-guide.org/en/latest/starting/install3/win/
#
Linux: 
http://docs.python-guide.org/en/latest/starting/install3/linux/
# Installing pygal
*Pip is sometimes included automatically when Python is installed to your system, and sometimes you have to install it yourself. 
If you do not have pip*

OS X: 
1. open terminal
2. sudo easy_install pip
#
Windows: 
1. To install pip, go to https://bootstrap.pypa.io/get-pip.py. Save the file if you’re prompted to do so; if the code for get-pip.py appears in your browser, copy and paste the entire program into your text editor and save the file as get-pip.py.
2. Open command prompt and navigate to the folder containing get-pip.py 
3. python get-pip.py
#
Linux: 
1. To install pip, go to https://bootstrap.pypa.io/get-pip.py. Save the file if you’re prompted to do so; if the code for get-pip.py appears in your browser, copy and paste the entire program into your text editor and save the file as get-pip.py.
2. Open a terminal and navigate to the folder containing get-pip.py
3. sudo python get-pip.py
#
Type "pip install pygal". For more information about pygal, http://pygal.org/en/stable/installing.html.
# Running Code 
NOTE: There are two files to run example will be given with WorldPlot1.py
Preffered Method: open Spyder from anaconda. Spyder is open source IDE that automatically comes with several scripting libraries.
#
OS X: 
1. Create a folder to run code in this repo. Download the code and csv file and move it to this folder.
2. Open Terminal.
3. cd to the folder
4. Type "python ./WorldPlot1.py" to run this program. 
NOTE: If you have python 2 and python 3 installed run "python3 GDP.py"
#
Windows:
1. Create a folder to run code in this repo. Download the code and csv file and move it to this folder.
2. Open Command Prompt.
3. cd \ to the folder
4. Type "WorldPlot1.py" to run this program. 
NOTE: If it didn't work, make sure your PATH contains the python directory.
#
Linux: 
1. Create a folder to run code in this repo. Download the code and csv file and move it to this folder.
2. Open up the terminal program. In KDE, open the main menu and select "Run Command..." to open Konsole. In GNOME, open the main menu, open the Applications folder, open the Accessories folder, and select Terminal.
3. cd ~/ to the folder
4. Type "chmod a+x WorldPlot1.py" to tell Linux that it is an executable program.
5. Type "./WorldPlot1.py" to run this program. 
# Dictionary for WorldPlot1.py
As the format of the CSV file that stores the GDP data could change (or you could acquire data from somewhere else), the functions that operate directly on the data will all take a "gdpinfo" dictionary that provides information about the file.  

gdpinfo = 
{

        "gdpfile": "isp_gdp.csv",        # Name of the GDP CSV file
        
        "separator": ",",                # Separator character in CSV file
        
        "quote": '"',                    # Quote character in CSV file
        
        "min_year": 1960,                # Oldest year of GDP data in CSV file
        
        "max_year": 2015,                # Latest year of GDP data in CSV file
        
        "country_name": "Country Name",  # Country name field name
        
        "country_code": "Country Code"   # Country code field name
        
}
# Additional dictionary for WorldPlot2.py
Since WorldPlot2.py uses country codes instead of country names another dictionary is needed. As the format of the CSV file that stores the country codes could change (or you could acquire data from somewhere else), the functions that operate directly on the country code data will all take a "codeinfo" dictionary that provides information about the file. 

codeinfo = 
{

        "codefile": "isp_country_codes.csv", # Name of the country code CSV file
        
        "separator": ",",                    # Separator character in CSV file
        
        "quote": '"',                        # Quote character in CSV file
        
        "plot_codes": "ISO3166-1-Alpha-2",   # Plot code field name
        
        "data_codes": "ISO3166-1-Alpha-3"    # GDP data code field name
}
