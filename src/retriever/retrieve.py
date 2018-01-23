import requests
from tqdm import tqdm


# tqdm==4.19.5
def download_file(index, info):
    url = "https://www.sec.gov/Archives/edgar/data/1122304/000112230417000014/0001122304-17-000014.txt"
    req = requests.get(url, stream=True)
    c_size = int(req.headers['content-length'])
    print('Downloading ' + 'AET' + '...')
    p_bar = tqdm(total=c_size)

    with open("data.dat", 'wb') as f:
        for chunk in req.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                p_bar.update(1024)

    p_bar.close()


download_file(1, 2)
