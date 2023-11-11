@echo off
setlocal

REM 设置 Python 脚本路径和参数
set python_script=app.py
set script_args=QUESTION_LANG=cn QUESTION_LLM='baidu' QUESTION_LLM_KEY='xxx'

REM 使用 python 命令调用脚本并传递参数
python %python_script% %script_args%
pause
