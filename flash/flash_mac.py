# ToDo: figure out how to have an "update" mode that doesn't remove any configuration

# Watch for either of the directories we would update to appear in /Volumes 
# if CIRCUITPY shows up:  flash with the code
# if RPI-RP2 shows up: flash with the CircuitPython image

import os
import time
import shutil
import watchdog.events 
import watchdog.observers

def empty_dir(target):
    for fname in os.listdir(target):
        path = os.path.join(target,fname)
        try:
            if os.path.isfile(path):
                os.unlink(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)
            #else:
            #    print("Can't figure out how to remove this: {}".format(path))
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (path, e))


def copy_code(src_dir, dst_dir):
    for fname in os.listdir(src_dir):
        path = os.path.join(src_dir, fname)
        try:
            if os.path.isfile(path):
                shutil.copy2(path,dst_dir)
            elif os.path.isdir(path):
                shutil.copytree(path,os.path.join(dst_dir,fname))
            else:
                print("Can't copy {}".format(path))
        except Exception as e:
            print('Failed to copy %s. Reason: %s' % (path, e))
    print("Finished copying software to badge at {}.".format(dst_dir))


def copy_data(dst_dir):
    # ToDo: Check if config has been run, if not run it
    # ToDo: Copy a variant of the config to the badge
    pass

class Handler(watchdog.events.FileSystemEventHandler):

    def __init__(self):
        watchdog.events.DirCreatedEvent.__init__(self, src_path="/Volumes")

    def on_created(self,event):
        # handle when a new directory is created in /Volunes 
        time.sleep(2)  # give the volume a chance to finish mounting

        new_vol = os.path.basename(event.src_path)
        if new_vol == "RPI_RP2":
            print("Found a bare badge, flashing with circuitpy")
        elif new_vol == "CIRCUITPY":
            print("Flashed badge inserted, time to write our softwrae.")
            empty_dir(event.src_path)
            copy_code("../software/", event.src_path)
            copy_data(os.path.join(event.src_path,"data"))
        else:
            # uncomment to check what other volumes get mounted from the badge
            # print("Not sure what I found: {}".format(new_vol))
            pass
        # ToDo: umount /Volumes/CIRCUITPY

class flash_mac:
    def __init__(self):
        self.path = "/Volumes"


    def run(self):
        print("Looping waiting for new Volumes to arrive...")
        
        event_handler = Handler()
        observer = watchdog.observers.Observer()
        observer.schedule( event_handler, path=self.path, recursive=True )
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

if __name__ == "__main__":
    flash = flash_mac()
    flash.run()
