
import base64
import requests
import os
import json
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename

url = "http://127.0.0.1:5000/infer"

if __name__ == "__main__":
    st = time.time()
    Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
    # show an "Open" dialog box and return the path to the selected file
    filename = askopenfilename()
    
    file = open("static/urlimage.txt", "w") # mở file để ghi với chế độ write ("w")
    file.write(os.path.basename(filename)) # ghi nội dung vào file
    file.close() # đóng file sau khi hoàn thành công việc
    # save image to static/images folder
    with open(filename, "rb") as image_file:
         with open('static/images/' + os.path.basename(filename), 'wb') as f:
                f.write(image_file.read())
    with open(filename, "rb") as image_file:
        # save image to static/images folder
        encoded_string = base64.b64encode(image_file.read())


    data = {}
    data['image_name'] = os.path.basename(filename)
    data['image'] = encoded_string

    response = requests.post(url, data=data)
    print("response")
    response_dict = json.loads(response.text)
    # for i in response_dict:
    #     print("key: ", i, "val: ", response_dict[i])
    #viet ket qua vao file json
    with open('static/results.json', 'w', encoding='utf-8-sig') as f:
        for i in response_dict:

            if i == 'image_name':
                continue
            #ensure_ascii=False giu nguyen font tieng viet
            json_str = json.dumps(
                response_dict[i], indent=4, ensure_ascii=False)

            f.write("\n" + json_str + "\n")

    print(time.time() - st)
