import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'psutil'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'zmq'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'websockets'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'python-banyan'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'pyserial'])

subprocess.check_call([sys.executable, '-m', 'pip', 'install',
'PyQt5'])

# process output with an API in the subprocess module:
reqs = subprocess.check_output([sys.executable, '-m', 'pip',
'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]

print(installed_packages)