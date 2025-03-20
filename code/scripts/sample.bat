@echo off

:: Activating Anaconda environment
call activate Gan

:: Checking if the activation is successful
if not %errorlevel% == 0 (
    echo Failed to activate the conda environment. Exiting.
    exit /b 1
)

:: Configs of different datasets
set cfg=%1

:: Model settings
set imgs_per_sent=16
set cuda=True
set gpu_id=0

:: Running the Python script
python "C:\Users\VATSAL\OneDrive\Documents\DF-GAN-master\code\src\sample.py" ^
        --cfg %cfg% ^
        --imgs_per_sent %imgs_per_sent% ^
        --cuda %cuda% ^
        --gpu_id %gpu_id%
