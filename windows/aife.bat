@echo off

REM Check if the keyword "activate" is provided
rem runs python script
python "c:\Users\Victor\Desktop\AI-Terminal-Tool\main.py" "%1"

REM Check if there is at least one command after the keyword
if "%1" equ "" (
  
    echo Error: No command provided after the keyword.
    echo Input aife -h to see the possible commands aife offers.
    exit /b
)

REM Run the intended command
echo Activating command: %2
%2
