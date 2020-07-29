import requests,json
import pytest
def setup_module():
    print('\n *** 初始化-模块 ***')
def teardown_module():
    print('\n ***   清除-模块 ***')
@pytest.mark.parametrize('param',['cdn','vpn','download','drug','mirror'])
def test_9_rules_rest(param):
        #count = 0
    # for line in open('test_9_rules_rest.txt', encoding='UTF-8'):
    #     param= json.loads(line)
    #     param_add_quot = '"'+param+'"'
        print('测试输入参数：', param)
        payload = {
            "detail_content": param,
        }
        headers ={
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
            "accept":"application/json",
            "content-type": "application/json",
        }

        response = requests.get("http://127.0.0.1:8009/apis/rules/"+param,
                                 headers=headers,
                                 data=json.dumps(payload),)
        print(response.status_code)
        print(response.text)
        data1 = json.loads(response.text)
        data2= data1.keys()

        # if 'data' in data2:
        #     print("True")
        # elif 'error' in data2:
        #     print("False")
        # else:
        #     print('不包含data或error！')
        assert('data' in data2 or 'error'in data2)
        # assert('data' not in data2),"True"
        # assert('error' not in data2),"False"
        #count += 1
        print('--------测试结束-----------')