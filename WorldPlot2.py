#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 15:42:48 2018

@author: mounarkpatel
"""

"""
Unify data via common country codes. Use pygal to plot wold map with the GDP of each country.
"""

import csv
import math
import pygal

def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - Name of CSV file
      keyfield  - Field to use as key for rows
      separator - Character that separates fields
      quote     - Character used to optionally quote fields

    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    table = {}
    with open(filename, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
        for row in csvreader:
            rowid = row[keyfield]
            table[rowid] = row
    return table


def build_country_code_converter(codeinfo):
    """
    Inputs:
      codeinfo      - A country code information dictionary

    Output:
      A dictionary whose keys are plot country codes and values
      are world bank country codes, where the code fields in the
      code file are specified in codeinfo.
    """
    mapdict = {} #dictionary to be returned
    file = codeinfo["codefile"]
    separator = codeinfo["separator"]
    quote = codeinfo["quote"]
    #plot_codes = country codes used by the plot library 
    #data_codes = country codes used by the GDP data
    plot = codeinfo["plot_codes"] 
    data = codeinfo["data_codes"]
    pcountry = read_csv_as_nested_dict(file, plot, separator, quote)
    
    for key in pcountry:
        #dic is the dictionary with keys such as 'Country Code' and 'Country Name'
        dic = pcountry[key]
        for item in dic:
            #check to see if the key of dic is equal to the key for GDP data
            if item == data:
            #then the plot country code key is set to country code found in GDP  data
                mapdict[key] = dic[item]
    return mapdict
                
    
def build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year for which to create GDP mapping

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    gdp = {} # for the first element of tuple
    nocountry = set() #countries not found in GDP data file
    nodata = set() #counties that did not have any GDP
    filename = gdpinfo['gdpfile']
    keyfield = gdpinfo['country_code']
    separator = gdpinfo['separator']
    quote = gdpinfo['quote']
    stat = read_csv_as_nested_dict(filename, keyfield, separator, quote)
    """dic will be needed to convert from the values given in plot_countires
    to the actual keys found in stat to get actual years and the GDP values"""
    dic = build_country_code_converter(codeinfo)
    
    for code in plot_countries:
        #country name
        name = plot_countries[code]
        if name in dic:
            """the key for WB country codes are similar or exact in regards to the 
            keys found in stat, they can differ in the case of letters so checking
            has to be done for that"""
            value = dic[name] #exact WB country code
            Uvalue = value.upper() #makes all letters uppercase
            Lvalue = value.lower() #makes all letters lowercase
            Svalue = value.swapcase() #swaps the letters from uppercase to lowercase and vice versa
            #condictionals check if any resemblence is found between WB country codes and keys in stat
            if Uvalue in stat:
                #the keys of dictionary are strings such as '2005' and values such as '5'
                yrs = stat[Uvalue]
                for key in yrs:
                    #checks to go to the right year such as '2005'
                    if (key == year) and (yrs[key] != '' or yrs[key] != ""):
                        gdp[code] = math.log10(float(yrs[key]))
                    #checks to see if country is found but has no value for GDP
                    elif (key == year) and (yrs[key] == '' or yrs[key] == ""):
                        nodata.add(code)
            elif Lvalue in stat:
                yrs = stat[Lvalue]
                for key in yrs:
                    if (key == year) and (yrs[key] != '' or yrs[key] != ""):
                        gdp[code] = math.log10(float(yrs[key]))
                    elif (key == year) and (yrs[key] == '' or yrs[key] == ""):
                        nodata.add(code)
            elif value in stat:
                yrs = stat[value]
                for key in yrs:
                    if (key == year) and (yrs[key] != '' or yrs[key] != ""):
                        gdp[code] = math.log10(float(yrs[key]))
                    elif (key == year) and (yrs[key] == '' or yrs[key] == ""):
                        nodata.add(code)  
            elif Svalue in stat:
                yrs = stat[Svalue]
                for key in yrs:
                    if (key == year) and (yrs[key] != '' or yrs[key] != ""):
                        gdp[code] = math.log10(float(yrs[key]))
                    elif (key == year) and (yrs[key] == '' or yrs[key] == ""):
                        nodata.add(code)  
            #final options is that the country code was not found in stat
            else:
                nocountry.add(code)   
        #or that it was not a valid country name in dic
        else:
            nocountry.add(code)     
    return (gdp, nocountry, nodata)
        
    
def render_world_map(gdpinfo, codeinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      codeinfo       - A country code information dictionary
      plot_countries - Dictionary mapping plot library country codes to country names
      year           - String year of data
      map_file       - String that is the output map file name

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data in gdp_mapping and outputs
      it to a file named by svg_filename.
    """
    mapdata = build_map_dict_by_code(gdpinfo, codeinfo, plot_countries, year)
    gdpdict = mapdata[0] #the GDP dictionary
    notinfile = mapdata[1] #set of country codes not present in file
    nogdp = mapdata[2] #set of country's with no gdp value
    
    worldmap = pygal.maps.world.World()
    worldmap.title = "GDP by country for " + year + " (log scale), " + "unified by common country NAME"
    #shades of counties are different between all three adds or datasets
    worldmap.add("GDP for " + year, gdpdict)
    worldmap.add("Missing from World Bank Data", notinfile)
    worldmap.add("No GDP data", nogdp)
    worldmap.render_to_file(map_file)


def test_render_world_map():
    """
    Test the project code for several years
    """
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    codeinfo = {
        "codefile": "isp_country_codes.csv",
        "separator": ",",
        "quote": '"',
        "plot_codes": "ISO3166-1-Alpha-2",
        "data_codes": "ISO3166-1-Alpha-3"
    }

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES

    # 1960
    render_world_map(gdpinfo, codeinfo, pygal_countries, "1960", "isp_gdp_world_code_1960.svg")

    # 1980
    render_world_map(gdpinfo, codeinfo, pygal_countries, "1980", "isp_gdp_world_code_1980.svg")

    # 2000
    render_world_map(gdpinfo, codeinfo, pygal_countries, "2000", "isp_gdp_world_code_2000.svg")

    # 2010
    render_world_map(gdpinfo, codeinfo, pygal_countries, "2010", "isp_gdp_world_code_2010.svg")

test_render_world_map()