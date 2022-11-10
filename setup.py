from cx_Freeze import setup, Executable

# Files to include
includefiles = [
    "nvdaControllerClient.dll"
]

# Executables
CORE = Executable("main.py", target_name="nvdatalker", base="Win32GUI")

# Installation
setup(
    name = "nvdatalker",
    version = "1.0",
    description = "NVDA Talker",
    executables = [CORE],
    options = {'build_exe': {
            "include_files": includefiles,
            "excludes": ["_gtkagg", "_tkagg", "bsddb", "distutils", "curses",
                    "pywin.debugger", "pywin.debugger.dbgcon",
                    "pywin.dialogs", "tcl", "Tkconstants", "Tkinter"],
            "packages": ["colander", "pathlib", "queue"],
    }},
)
