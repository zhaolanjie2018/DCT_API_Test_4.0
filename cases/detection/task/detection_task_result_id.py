import requests,json
id = '25863b4b-1934-4efb-b267-34a7904ac3fb'

headers ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
    "accept":"application/json",
    "content-type": "application/json",
}

proxies = {
    "http": "http://127.0.0.1:8888",
    "https": "http://127.0.0.1:8888",
}


response = requests.get("http://222.186.150.231:5000/apis/detection/task/result/"+id,
                         headers=headers,
                         proxies=proxies,

                                                  )
print(response.text)