@REM @Author: CPS
@REM @email: 373704015@qq.com
@REM @Date: 2026-01-19 09:42:39.021476
@REM Last Modified by: CPS
@REM Last Modified time: 2026-01-19 09:42:39.021476
@REM Modified time: 2026-01-19 09:42:39.021476
@REM @file_path "W:\CPS\MyProject\projsect_persional\cps-cli\cps-cli-template\template-fastapi"
@REM @Filename "SingelExe.build.bat"
@REM @descriton 使用nuitka来进行单文件打包

@echo off && setlocal enabledelayedexpansion
@chcp 65001

REM 基础参数
set "BASE_ARGS=--onefile --jobs=7 --standalone --show-memory --show-progress --follow-imports --output-dir=build src/main.py"

REM 支持 poetry、pdm、uv
if exist "pdm.lock" (
    pdm run python -m nuitka %BASE_ARGS%
) else if exist "poetry.lock" (
    poetry run python -m nuitka %BASE_ARGS%
) else if exist "uv.lock" (
    uv run python -m nuitka %BASE_ARGS%
) else (
    python -m nuitka %BASE_ARGS%
)
pause
