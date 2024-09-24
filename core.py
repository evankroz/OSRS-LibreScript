import logging
from AppKit import NSWorkspace
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG)


class WinInfo():
    def __init__(self):
        self.username = "RuneLite - PureBerr"


def get_win_info(username):

    # Get information about all windows
    windows = CGWindowListCopyWindowInfo(kCGWindowListOptionOnScreenOnly, kCGNullWindowID)

    window_names = []
    for window in windows:
        window_n = window.get("kCGWindowName", "")
        owner_name = window.get("kCGWindowOwnerName", '')

        if window_n:
            window_names.append(window_n)
    #print(window_names)


    # Find the  window
    for window in windows:
        if window['kCGWindowName'] == f"RuneLite - {username}":
            # Get window dimensions
            bounds = window['kCGWindowBounds']
            width = bounds['Width']
            height = bounds['Height']

            return width, height

    # If no matching window found
    else:
        print("Window not found, exiting code")
        quit()


#username = "PureBerr"
# Get and print the active window information
#window_info = get_win_info(username)
#print(f"Window dimensions: {window_info[0], window_info[1]}")