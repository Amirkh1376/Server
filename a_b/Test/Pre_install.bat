@echo off

    :: Check if Python interpreter is available
    python --version > nul 2>&1
    if %errorlevel% NEQ 0 (
        echo Python interpreter not found in the system's environment.
        echo Please install Python and ensure it is added to the system's PATH.
        pause
        exit /b 1
    )

    :: Install libraries using the default Python interpreter and pip
    python -m pip install numpy requests

    :: Pause to keep the command prompt window open for viewing output (optional)
    pause