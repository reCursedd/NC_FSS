from util import O
from pprint import pprint
DATA1 ="""
outlook,$temp,?humidity,windy,play
sunny,85,85,FALSE,no
sunny,80,90,TRUE,no
overcast,83,86,FALSE,yes
rainy,70,96,FALSE,yes
rainy,68,80,FALSE,yes
rainy,65,70,TRUE,no
overcast,64,65,TRUE,yes
sunny,72,95,FALSE,no
sunny,69,70,FALSE,yes
rainy,75,80,FALSE,yes
sunny,75,70,TRUE,yes
overcast,100,25,90,TRUE,yes
overcast,81,75,FALSE,yes
rainy,71,91,TRUE,no"""

DATA2 ="""
    outlook,   # weather forecast.
    $temp,     # degrees farenheit
    ?humidity, # relative humidity
    windy,     # wind is high
    play       # yes,no
    sunny,85,85,FALSE,no
    sunny,80,90,TRUE,no
    overcast,83,86,FALSE,yes

    rainy,70,96,FALSE,yes
    rainy,68,80,FALSE,yes
    rainy,65,70,TRUE,no
    overcast,64,

                  65,TRUE,yes
    sunny,72,95,FALSE,no
    sunny,69,70,FALSE,yes
    rainy,75,80,FALSE,yes
          sunny,
                75,70,TRUE,yes
    overcast,100,25,90,TRUE,yes
    overcast,81,75,FALSE,yes # unique day
    rainy,71,91,TRUE,no"""

def lines(str):
    "Return contents, one line at a time."
    # print ("inside lines")
    line_list = []
    for i in str.split("\n"):
        if "#" in i:
            i = i.split("#")[0]
        #print (i)
        i = i.strip(' ')
        line_list.append(i)
        # how to replace this with yeild
    return(line_list)


def rows(lines):
    """Kill bad characters. If line ends in ','
     then join to next. Skip blank lines."""
    # print ("----INSIDE ROW----")
    buffer_line = ""
    rows = []
    for i in lines:
        if  (i.endswith(',')):
            buffer_line = buffer_line+i
            continue
        if i is "":
            continue
        else:
            rows.append(buffer_line+i)
            buffer_line = ""
    return rows

    # pprint (rows)


def cols(rows):
    """ If a column name on ro w1 contains '?',
  then skip over that column."""
    # print ("Inside col")
    new_rows = []
    waste_cols = []
    for index, key in enumerate(rows[0].split(",")):
            if "?" in key:
                waste_cols.append(index)

    for row in (rows):
        row = row.split(",")
        for index, key in enumerate(row):
            if index in waste_cols:
                del row[index]
        new_rows.append(row)
    return (new_rows)

def prep(nice_rows):
    """ If a column name on row1 contains '$',
  coerce strings in that column to a float."""
    # print("Inside prep")
    new_rows = []
    conv_cols = []
    for index, key in enumerate(nice_rows[0]):
      if "$" in key:
          conv_cols.append(index)

    # nice_rows = [x if (condition) else None for x in ls]

    for i,row in enumerate(nice_rows):
        for index, key in enumerate(row):
          if index in conv_cols and i != 0:
              del row[index]
              row.insert(index, float(key))
        new_rows.append(row)
    # print (new_rows)
    return (new_rows)



def ok0(s):
    # prep(cols(rows(lines(s))))
    for row in prep(cols(rows(lines(s)))):
        print(row)
        return row

# @O.k
# def ok1(): ok0(DATA1)

# @O.k
# def ok2(): ok0(DATA2)

# @O.k
# def ok3():
#     assert ok0(DATA1) == ok0(DATA2)