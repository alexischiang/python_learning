def user_agent(browser):
    if browser == 'chrome':
        dict = {
            'User-Agent' :'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        }
        return dict
    elif browser == 'firefox':
        dict = {
            'User-Agent' :'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        }
        return dict


