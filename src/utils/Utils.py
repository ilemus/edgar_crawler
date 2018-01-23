import re


def get_table(data):
    ret_val = []
    data_arr = data.split("<table")

    if len(data_arr) > 1:
        for row in data_arr:
            temp_arr = row.split("</table>")
            # There is no table inside of table in EDGAR data
            if len(temp_arr) > 1:
                ret_val.append("<table" + temp_arr[0] + "</table>")

    return ret_val


def get_row(data):
    ret_val = []
    data_arr = data.split("<tr")

    if len(data_arr) > 1:
        for row in data_arr:
            temp_arr = row.split("</tr>")
            # There is no row inside of row in EDGAR data
            if len(temp_arr) > 1:
                ret_val.append("<tr" + temp_arr[0] + "</tr>")

    return ret_val


def get_cell(data):
    ret_val = []
    data_arr = data.split("<td")

    if len(data_arr) > 1:
        for row in data_arr:
            temp_arr = row.split("</td>")
            # There is no cell inside of cell in EDGAR data
            if len(temp_arr) > 1:
                ret_val.append("<td" + temp_arr[0] + "</td>")

    return ret_val


def get_div(data):
    ret_val = []
    data_arr = data.split("<div")

    if len(data_arr) > 1:
        for row in data_arr:
            temp_arr = row.split("</div>")
            # There is no div inside of div in EDGAR data
            if len(temp_arr) > 1:
                ret_val.append("<div" + temp_arr[0] + "</div>")

    return ret_val


def get_font(data):
    ret_val = []
    data_arr = data.split("<font")

    if len(data_arr) > 1:
        for row in data_arr:
            temp_arr = row.split("</font>")
            # There is no font inside of font in EDGAR data
            if len(temp_arr) > 1:
                ret_val.append("<font" + temp_arr[0] + "</font>")

    return ret_val

# Removes tags and leaves data inside
def get_contents(data):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', data)
    return cleantext


dat = get_contents("<font wut is this>this is some data </font>")
print(dat)
