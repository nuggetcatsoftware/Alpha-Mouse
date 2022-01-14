from http.server import executable
from cx_Freeze import setup, Executable
setup(name="Flyingmouse",
version="0.1",
description=" A Flying Mouse",
executables=[Executable("handmouse.py")])