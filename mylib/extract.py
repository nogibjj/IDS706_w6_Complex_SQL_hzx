"""
Extract a dataset from a URL like Kaggle or data.gov. JSON or CSV formats tend to work well

"""
import requests
import __main__

def extract(url="https://github.com/fivethirtyeight/data/blob/master/special-elections/special-elections.csv?raw=true", 
            file_path="data/Sp_elections.csv"):
    """"Extract a url to a file path"""
    with requests.get(url) as r:
        print("request status code is", r.status_code)
        with open(file_path, 'wb') as f:
            f.write(r.content)
    return file_path

if __name__ == "__main__":
    extract()


