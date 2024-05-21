import requests
from datetime import datetime

def download_file(url, local_filename):
    # Send a GET request to the URL
    start = datetime.now()
    with requests.get(url, stream=True) as r:
        # Raise an exception if the request failed
        r.raise_for_status()
        # Open the local file for writing in binary mode
        with open(local_filename, 'wb') as f:
            # Stream the content of the response to the file
            for chunk in r.iter_content(chunk_size=8192): 
                f.write(chunk)
    print(f"Success fully downloaded in {datetime.now()-start}")
    return local_filename

#download_file("http://192.168.1.44:5000/matches/avl.v.liv.1.epl.13.05.2024/2",'match2.mp4')
