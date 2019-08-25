@echo off
ECHO Installing Python
"%CD%\python-3.7.3.exe" /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
ECHO Done
ECHO Now launch "2.bat"
PAUSE
