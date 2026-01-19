@REM @Author: CPS
@REM @email: 373704015@qq.com
@REM @Date: 2022-10-06 15:01:56.235254
@REM Last Modified by: CPS
@REM Last Modified time: 2022-10-06 15:01:56.235254
@REM Modified time: 2022-10-06 15:01:56.235254
@REM @file_path "D:\CPS\MyProject\Projects_Personal\cps-cli\template\fastapi"
@REM @Filename "run.bat"

@echo off && setlocal enabledelayedexpansion
@chcp 65001


REM 支持 poetry、pdm、uv
if exist "pdm.lock" (
    pdm run python src/main.py
) else if exist "poetry.lock" (
    poetry run python src/main.py
) else if exist "uv.lock" (
    uv run python src/main.py
) else (
    python src/main.py
)

pause
