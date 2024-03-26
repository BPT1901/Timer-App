from cx_Freeze import setup, Executable

setup(
    name='TimerApp',
    version='1.0',
    description='Timmer Application',
    executables=[Executable('main.py')]
)