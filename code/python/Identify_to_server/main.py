import requests
import hashlib
from pathlib import Path
import os


uri = "http://192.168.0.100:8000"


def main():
    certif_sum = get_certif_sum()
    cpu_info = get_cpuinfo()
    try:
        req = requests.post(f"{uri}/user/identification?id_cpu={cpu_info}&id_sum={certif_sum}", timeout=10 )
    except requests.exceptions.ConnectTimeout:
        print("Error Timeout : Retrive ")
        main()
        return
    except Exception as ex:
        print(f"Error : {type(ex).__name__}")
        return
    print(req)
    json = req.json()
    print(f"{req.status_code},  {json}")
    
def get_certif_sum():
    filepath = '/home/john/certif.key'
    filebytes = Path(filepath).read_bytes()
    id_sum = hashlib.sha512(filebytes)
    return id_sum.hexdigest()
    
def get_cpuinfo():
    cpu_info = open("/proc/cpuinfo", "r") 
    for l in cpu_info.readlines():
        if "Serial" in l:
            txt = l.split(':')
            return txt[1].strip()
    

if __name__ == '__main__':
    main()
    