headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like G'
                      'ecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.24'
}
import  requests
if __name__ == "__main__":
    post_url = 'https://fanyi.youdao.com/'
    data = {
        'kw': 'dog'
    }

    response = requests.post(url=post_url,data=data,headers=headers)
    dic_obj = response.text
    print(dic_obj)