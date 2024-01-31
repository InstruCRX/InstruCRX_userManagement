@echo off
setlocal enabledelayedexpansion

for %%x in (%*) do (
   start http:\\%%~x:9090\pull_backend
)
