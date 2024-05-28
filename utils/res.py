#统一返回
from enum import Enum, auto

class Res():
    ok = "操作成功"
    error = "操作失败"
    

def ok():
    return Res.ok

def error():
    return Res.error
    
 
