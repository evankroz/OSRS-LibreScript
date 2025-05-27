import logging
from AppKit import NSWorkspace
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                   level=logging.DEBUG)
class WinInfo():
    def __init__(self, username):
        self.username = f"RuneLite - {username}"


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
            #print(window)
            # Get window dimensions
            bounds = window['kCGWindowBounds']
            x = int(bounds["X"])
            y = int(bounds["Y"])
            width = int(bounds['Width'])
            height = int(bounds['Height'])

            return (x, y, width, height)

    # If no matching window found
    else:
        print("Window not found, exiting code")
        quit()


username = "PureBerr"
# Get and print the active window information
window_info = get_win_info(username)
print(f"Window dimensions: {window_info[0], window_info[1], window_info[2], window_info[3]}")