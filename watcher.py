import subprocess
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import os


class ReloadHandler(FileSystemEventHandler):
    def __init__(self, script_path):
        self.script_path = script_path
        self.script_path = script_path
        self.process = None
        self.restart_script()

    def restart_script(self):
        if self.process:
            self.process.terminate()
            print(f"Ejecuting script: {self.script_path}")
            self.process.wait()
        self.process = subprocess.Popen([sys.executable, self.script_path])

    def on_modified(self, event):  
        if event.src_path.endswith(".py"):
            print(f"Cambios Detectados en: {self.script_path}. Recargando script...")
            self.restart_script()

if __name__ == "__main__":
    script_to_watch = "bluetooth-ui.py"
    path = os.path.dirname(os.path.abspath(script_to_watch))

    event_handler = ReloadHandler(script_to_watch)
    observer = Observer()   
    observer.schedule(event_handler, path=path, recursive=False)
    observer.start()
    print(f"Observando cambios en: {script_to_watch}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop() 

    observer.join()
    