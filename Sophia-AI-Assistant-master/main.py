import os
import eel
from engine.features import *
from engine.command import *

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
www_dir = os.path.join(script_dir, 'www')

eel.init(www_dir)

# Play start sound if available
try:
	playAssistantSound()
except Exception:
	pass

# Launch a Chrome app window for the UI (optional)
try:
	port = int(os.environ.get('EEL_PORT', '8000'))
except Exception:
	port = 8000
try:
	os.system(f'start chrome.exe --app="http://localhost:{port}/index.html"')
except Exception:
	pass

eel.start('index.html', mode=None, host='localhost', port=port, block=True)