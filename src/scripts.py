import subprocess


def server():
    cmd = ["python3", "src/manage.py", "runserver"]
    subprocess.run(cmd)


def tests():
    cmd = ["pytest", "-p", "no:warnings", "-v"]
    subprocess.run(cmd)
