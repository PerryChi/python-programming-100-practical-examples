# 请求网页HTML内容 示例
import requests

# 主函数main
if __name__ == '__main__':
    # vprotocol = 'https'
    # url = vprotocol + '//***.***.***/s'
    url = 'https://www.mca.gov.cn/mzsj/xzqh/2022/202201xzqh.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36'
    }

    queryword = input('请录入查询内容')
    parm = { 'q': queryword }
    res = requests.get(url, params=parm, headers=headers)
    txt = res.text
    with open('./administrative-division.html', 'w', encoding='utf-8') as fs:
        fs.write(txt)
    print('程序运行完成')
