import subprocess


def server():
    cmd = ["python3", "src/manage.py", "runserver"]
    subprocess.run(cmd)
