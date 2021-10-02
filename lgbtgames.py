import pandas
import requests
from bs4 import BeautifulSoup
import matplotlib

url = "https://representme.charity/projects/queer\
/database/spreadsheet?columns%5B%5D=title&columns\
%5B%5D=year&columns%5B%5D=developer&columns%5B%5D\
=publisher&columns%5B%5D=genre&columns%5B%5D=plat\
form&columns%5B%5D=aaa&columns%5B%5D=protagonist&\
columns%5B%5D=npcs&columns%5B%5D=references&column\
s%5B%5D=implied"
page = requests.get(url)

def implied_per_year(table):
    """plot year vs the number of games with only implied representation,
    wanted to see if there was a trend,
    set too small for any meaningful conclusions to be drawn"""
    impliedYearTable = table
    impliedYearTable["Year"] = impliedYearTable["Year"].str[0:5]
    impliedYearTable["Year"] = pandas.to_numeric(impliedYearTable["Year"],errors="coerce")
    impliedYearTable.dropna(subset=["Year"],inplace=True)
    impliedYearTable["Year"] = impliedYearTable["Year"].astype(int)
    impliedYearTable = impliedYearTable.groupby(["Year", "Implied?"])["Title"].count().reset_index(name="count")
    impliedYearTable = impliedYearTable[impliedYearTable["Implied?"]=="Yes"].reset_index(drop=True)
    return impliedYearTable

#find the table and convert it to a dataframe
htmlText = BeautifulSoup(page.text, 'html.parser')
htmlTable = htmlText.find('table',{'class':"spreadsheet"})
table = pandas.read_html(str(htmlTable))
table = pandas.DataFrame(table[0])

impliedYearTable = implied_per_year(table)

#AAA games with implied vs non-implied rep.
aaaImpliedTable = table.copy()
aaaImpliedTable = aaaImpliedTable[aaaImpliedTable["AAA?"] == "Yes"]
aaaImpliedTable = aaaImpliedTable.groupby(["Implied?"]).count()
aaaImpliedTable = aaaImpliedTable[["Protagonist rep.", "NPC/s rep.", "Other rep."]]
aaaImpliedTable.plot.bar(rot=0)

#remove games with only implied LGBT+ characters
table = table.loc[table["Implied?"] == "No"]

protagTable = table.copy()
protagTable.dropna(subset=["Protagonist rep."],inplace=True)



#impliedYearTable.plot(x = "Year", y = "count", xlabel = "Year", ylabel = "Implied Count")
matplotlib.pyplot.show()
