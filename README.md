python -m venv venv
venv\Scripts\activate #cmd
venv\Scripts\Activate.ps1 #pwrshl

python main.py

#For powershell issues:
Set-ExecutionPolicy Unrestricted -Scope Process

# Run designer.exe to open QtDesigner
schmelzer\squad-planner-env\Lib\site-packages\qt5_applications\Qt\bin\designer.exe