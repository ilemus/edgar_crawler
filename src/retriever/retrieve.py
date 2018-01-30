import requests
import os
from tqdm import tqdm
from src.utils import Utils
from bs4 import BeautifulSoup as bs


# bs4
# tqdm==4.19.5
def download_file(index, info):
    url = "https://www.sec.gov/Archives/edgar/data/1122304/000112230417000014/form10-k.htm"
    req = requests.get(url)# , stream=True)
    # c_size = int(req.headers['content-length'])
    print('Downloading ' + 'AET' + '...')
    # p_bar = tqdm(total=c_size)

    # with open("data.dat", 'wb') as f:
    #     for chunk in req.iter_content(chunk_size=1024):
    #         if chunk:
    #             f.write(chunk)
    #             p_bar.update(1024)

    # p_bar.close()
    return req.content


def read_data(path):
    data = []
    whole = ''
    p_bar = tqdm(total=os.path.getsize(path))
    with open(path, 'rb') as f:
        # Tables are not next to each other
        part = f.read(1024)
        p_bar.update(1024)
        while part:
            # Keep adding to temp until table found, then delete from memory
            whole += str(part)

            # For each table
            got_table = Utils.get_table(whole)

            # Extract row data
            if len(got_table) > 0:
                del whole
                whole = ''
                rows = Utils.get_row(got_table[0])

                for row in rows:
                    # accumulate all the data in a row
                    row_data = []

                    # Get individual cells
                    cells = Utils.get_cell(row)
                    for cell in cells:
                        div = Utils.get_div(cell)
                        if len(div) > 0:
                            font = Utils.get_font(div[0])
                            if len(font) > 0:
                                dat = Utils.get_contents(font[0])
                                if len(dat) > 0 and dat != "&#160;":
                                    if dat == "&#8212;":
                                        dat = '-'
                                    row_data.append(dat)
                    # end for cell in cells:
                    if len(row_data) > 0:
                        data.append(row_data)
                # end for row in rows:
            # end if len(got_table) > 0:
            if len(got_table) > 1:
                for i in range(1, len(got_table)):
                    whole += got_table[i]
            part = f.read(1024)
            p_bar.update(1024)
        # end while part:

    for row in data:
        print(row)


def parse_html_data(data):
    ret_data = []
    soup = bs(data, "html.parser")
    # Get all tables
    tables = soup.findAll("table")
    for table in tables:
        rows = table.findAll("tr")
        for row in rows:
            row_data = []
            cells = row.findAll("td")
            for cell in cells:
                div = cell.find("div")
                if div is not None:
                    font = div.find("font")
                    if font is not None:
                        dat = font.string
                        if dat is not None and len(dat) > 0 and dat != '\xa0' and dat != '\xa0%':
                            if dat == "&#8212;":
                                dat = '-'
                            row_data.append(dat)
            # end for cell in cells:
            if len(row_data) > 0:
                ret_data.append(row_data)
        # end for row in rows:

    for row in ret_data:
        print(row)


# download_file(1, 2)
# read_data("data.dat")
parse_html_data(download_file(1, 2))