# -*- coding:utf-8 -*-


data_directory = "screenshots"

default_answer_number = 5

### ocr config
hanwan_appcode = "2815f26d414445aea47ced67cac07668"

### baidu orc
app_id = "10683349"
app_key = "XB6xqK0EWjRl7Ithmmwu2QGg"
app_secret = "3GwEF0PE0YDMfDwUqysqwkxIRNLUbbM7"

### 如果你想要使用汉王的话，将汉王移动到前面，默认使用百度，每天封顶500次
prefer = ("baidu", "hanwang")
# prefer = ("hanwang", "baidu")

text_summary = True

### 1代表灰度处理， 2代表二值化处理，如果需要使用二值化，需要将2放到前面
image_compress_level = (1, 2)

summary_sentence_count = 5
