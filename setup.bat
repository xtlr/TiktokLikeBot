@echo off
REM Check for Python installation using py
py --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is not installed or not accessible via 'py'. Please install Python and ensure it's added to your PATH.
    exit /b 1
)

REM Upgrade pip to ensure latest version
py -m pip install --upgrade pip

REM Install required packages
py -m pip install pandas numpy bcrypt openpyxl requests beautifulsoup4 matplotlib seaborn cryptography sqlalchemy

REM Check if the packages were installed successfully
if %ERRORLEVEL% NEQ 0 (
    echo Some packages failed to install. Please check the errors above.
    exit /b 1
)

echo All packages installed successfully!
pause
