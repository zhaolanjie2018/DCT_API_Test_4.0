import requests,json
import pytest
def setup_module():
    print('\n *** 初始化-模块 ***')
def teardown_module():
    print('\n ***   清除-模块 ***')
@pytest.mark.parametrize('load_param',['{"id": 96,"update_cname": ".com","update_service_provider": "国际"}'])
def test_1_rules_cdn(load_param):
    print('测试输入参数：', load_param)
    payload = json.loads(load_param)
    headers ={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362",
        "accept":"application/json",
        "content-type": "application/json",
    }
    response = requests.put("http://127.0.0.1:8009/apis/rules/cdn",
                             headers=headers,
                             data=json.dumps(payload),)
    print(response.status_code)
    print(response.text)
    data1 = json.loads(response.text)
    data2= data1.keys()
    assert('data' in data2 or 'error'in data2)
    print('--------测试结束-----------')