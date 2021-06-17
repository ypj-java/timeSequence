from django.http import HttpResponse
import json
import os
import time
import re

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def upload(request):
    res = {}
    if request.method == 'POST':
        file = request.FILES.get("file", None)
        fileName, name = saveFile(file)
        if fileName is None:
            res["code"] = 400
            res["msg"] = "上传文件出错"
            return HttpResponse(json.dumps(res))
        columns = getColumn(fileName)
        if columns is not None:
            res["code"] = 200
            res["msg"] = "success"
            res["data"] = {"columns": columns, "title": name, "fileName": fileName}
            return HttpResponse(json.dumps(res))
    else:
        res["code"] = 400
        res["msg"] = "仅支持POST方式请求"
        return HttpResponse(json.dumps(res))


def saveFile(file):
    if file:
        name = file.name[:file.name.rindex(".")]
        name = re.sub(r'[^\w]', '', name)
        tail = file.name[file.name.rindex(".") + 1:]
        fileName = name + str(int(round(time.time() * 1000))) + "." + tail
        destination = open(os.path.join('temp', fileName),
                           'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()
        return fileName, name
    else:
        return None


def getColumn(fileName):
    columns = None
    with open(os.path.join('temp', fileName), 'r') as fp:
        for line in fp:
            columns = line.split(",")[1:]
            break
    if columns is not None:
        for i in range(len(columns)):
            columns[i] = {"label": columns[i].strip(), "value": i}
    return columns


@csrf_exempt
def sequence(request):
    res = {}
    if request.method == "GET":
        fileName = request.GET["fileName"]
        title = request.GET["title"]
        column = request.GET["column"]
        fileNameHead = fileName[:fileName.rindex(".")]
        os.system(
            f"python time_sequence.py -file temp{os.sep}{fileName} -column {column} -path static{os.sep}{fileNameHead} -title {title}")
        res["code"] = 200
        res["msg"] = "success"
        res["data"] = fileNameHead + ".png"
        return HttpResponse(json.dumps(res))
    else:
        res["code"] = 400
        res["msg"] = "仅支持GET方式请求"
        return HttpResponse(json.dumps(res))
