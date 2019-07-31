from aip import AipOcr

# *配置参数↓
APP_ID = '10672844'
API_KEY = 'AtZDUUsmUQbr7zC1mr5MkQef'
SECRET_KEY = '7DQxS70cTSAsPii7VKvjr8TEyYgYqsGn'

options = {}
options["detect_direction"] = "true"
options["language_type"] = "CHN_ENG"
options["probability"] = "true"


def get_text_from_image(img_path='./images/a.jpg'):
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    # *打开图片
    with open(img_path, 'rb') as fp:
        image = fp.read()

    # *带参数调用高精度文字识别, 图片参数为本地图片
    result = client.basicAccurate(image, options)
    qa = result["words_result"]
    # *qa是个list，元素为dict

    # global question, ans1, ans2, ans3
    # # *全局变量
    # question = qa[0]['words']
    # ans1 = qa[1]['words']
    # ans2 = qa[2]['words']
    # ans3 = qa[3]['words']

    # *不够优雅
    QA = []
    for x in qa:
        words = x["words"]
        QA.append(str(words))
    return QA


if __name__ == "__main__":
    print(get_text_from_image())
