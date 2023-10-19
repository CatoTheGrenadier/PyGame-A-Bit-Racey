import cx_Freeze

executables = [cx_Freeze.Executable("C:\\Users\\Clementine\\Desktop\\Projects\\PyGame A Bit Racey\\My first python game.py")]

cx_Freeze.setup(
    name = "A Bit Racey",
    options={"build_exe":{"packages":["pygame"],
                            "include_files":["C:\\Users\\Clementine\\Desktop\\Projects\\PyGame A Bit Racey\\racecar.png"]
                            }
            },
    executables = executables
    )
    
