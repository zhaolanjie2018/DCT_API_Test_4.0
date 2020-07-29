#------verification_code的测试用例--------
import requests,json
import pytest
#pytest框架初始化
def setup_module():
    print('\n *** 初始化-模块 ***')
def teardown_module():
    print('\n ***   清除-模块 ***')

print("这是verification_code的test")
@pytest.mark.parametrize('url',['http://www.damatu1.com'])
def test_verification_code_post(url):
        print(url)
    # count = 0
    # f = open("Output_results.txt", "w")
    # f2 = open("Output_judge_value.txt", "w")
    # for line in open("language_test.txt"):
    #     # sum_t = 0.0
    #     # time_start = time.time()
    #     count+=1
    #     print('开始执行第:', count, line)
        payload = {
            "url": url,
        }
        headers ={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
            "accept":"application/json",
            "content-type": "application/json",
        }
        response = requests.post("http://127.0.0.1:8009/apis/verification_code",
                                 headers=headers,
                                 data=json.dumps(payload))
        print(response.status_code)
        print(response.text)
        data1 = json.loads(response.text)
        response_id=data1.get('id')
        #return response_id
        headers_2 ={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
            "accept":"application/json",
            "content-type": "application/json",
        }
        while True:
            response_2 = requests.get("http://127.0.0.1:8009/apis/detection/task/result/" + response_id,
                                   headers=headers_2,)
            data2 = json.loads(response_2.text)
            if data2.get('operate_status')=="STARTED":
                continue
            elif data2.get('operate_status') =="SUCCESS":
                print(response_2.text)
                #print("{}".format(response_2.text.replace('\n','')), file=f)
                result_output = json.loads(response_2.text)
                result_key = result_output.get('data')
                result_dict = json.loads(result_key)
                judge_value=result_dict.get("judge")
                assert(judge_value=='False'or judge_value=='True')
                #print("{}{}".format("judge:",judge_value), file=f2)
                break
            elif data2.get('operate_status') == "failed":
                print(response_2.status_code)
                print(response_2.text)
                #print(response_2.text)
                #print("{}".format(response_2.text.replace('\n', '')), file=f)
                result_output = json.loads(response_2.text)
                result_key = result_output.get('operate_status')
                assert(result_key=='failed')
                #print("{}{}".format("operate_status:", result_key), file=f2)
                break
            elif data2.get('operate_status') == "PENDING":
                continue
                # print(response_2.status_code)
                # print(response_2.text)
                # # print(response_2.text)
                # # print("{}".format(response_2.text.replace('\n', '')), file=f)
                # result_output = json.loads(response_2.text)
                # result_key = result_output.get('operate_status')
                # assert (result_key == 'PENDING')
                # # print("{}{}".format("operate_status:", result_key), file=f2)
                # break
            else:
                print(response_2.status_code)
                print(response_2.text)
                assert (1 == 2)
                break
            # time_end = time.time()
            # sum_t = (time_end - time_start) + sum_t  # 运行所花时间
            #print('时间花费:', sum_t, 's')
        print('------------结束执行---------------')

        # f.close()
        # f2.close()
#test_verification_code_post()
