import json


class Config:

    def __init__(self):
        self.filename = "/Users/wuxueliang/Documents/Workspace/git/Global_Config/config.json"

    def get_host(self):
        with open(self.filename, 'r') as fp:
            contents = json.load(fp)
            print(contents)
            # 为了防止敏感信息泄漏，我就将一些敏感信息放在本地，然后直接读取
            return contents['web'], contents['h5'], contents['file']


if __name__ == '__main__':
    print(Config().get_host())
