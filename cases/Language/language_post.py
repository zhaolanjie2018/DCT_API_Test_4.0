#------language的测试用例--------
import requests,json
import time
#请求测试网址返回响应消息，获取id信息

def obtain_id(test_url):
    payload = {
        "url": test_url,
    }
    headers ={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
        "accept":"application/json",
        "content-type": "application/json",
    }
    response = requests.post("http://127.0.0.1:8009/apis/Language",
                             headers=headers,
                             data=json.dumps(payload) )

    print(response.status_code)
    print(response.text)
    data1 = json.loads(response.text)
    response_id=data1.get('id')
    return response_id


#根据id查询爬虫结果
def obatin_reponse(response_id):
    headers ={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
        "accept":"application/json",
        "content-type": "application/json",
    }
    while True:
        response = requests.get("http://127.0.0.1:8009/apis/detection/task/result/" + response_id,
                               headers=headers,)
        data2 = json.loads(response.text)
        if data2.get('operate_status')=="STARTED":
            continue
        elif data2.get('operate_status') =="SUCCESS":
            print(response.text)
            print("{}".format(response.text.replace('\n','')), file=f)
            result_output = json.loads(response.text)
            result_key = result_output.get('data')
            result_dict = json.loads(result_key)
            judge_value=result_dict.get("judge")
            print("{}{}".format("judge:",judge_value), file=f2)
            break
        elif data2.get('operate_status') == "failed":
            print(response.text)
            print("{}".format(response.text.replace('\n', '')), file=f)
            result_output = json.loads(response.text)
            result_key = result_output.get('operate_status')
            print("{}{}".format("operate_status:", result_key), file=f2)
            break
        else:
            continue

print("这是language的test")
count= 0
f= open("Output_results.txt","w")
f2=open("Output_judge_value.txt","w")
for line in open("language_test.txt"):
#    line_add_quote = '"'+line.replace('\n','')+'"'

    count+=1
    print('开始执行第:',count,line)
    a=obtain_id(line)
    #try_sleep()
    #计时器开
    sum_t = 0.0
    time_start = time.time()
    #响应函数
    obatin_reponse(a)
    #计时结束
    time_end = time.time()
    sum_t = (time_end - time_start) + sum_t  # 运行所花时间
    print('时间花费:', sum_t, 's')
    print('------------结束执行---------------')

f.close()
f2.close()



