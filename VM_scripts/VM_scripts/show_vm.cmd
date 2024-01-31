@echo off
setlocal enabledelayedexpansion

for %%x in (%*) do (
   start http:\\%%~x:7080?userID=lena
)
