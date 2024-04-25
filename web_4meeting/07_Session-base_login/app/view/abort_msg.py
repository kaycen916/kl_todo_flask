import sys
import traceback

def abort_msg(e):
    error_class = e.__class__.__name__
    detail = e.args[0]
    # 得到錯誤的完整資訊
    cl, exc, tb = sys.exc_info()
    # 取得最後一行的錯誤訊息
    lastCallStack = traceback.extract_tb(tb)[-1]
    # 錯誤的檔案位置名稱
    fileName = lastCallStack[0]
    # 錯誤的行數
    lineNum = lastCallStack[1]
    # 錯誤的 function 名稱
    funcName = lastCallStack[2]

    errMsg = {error_class: [detail]}
    return errMsg