import logging
from AppKit import NSWorkspace
from Quartz import CGWindowListCopyWindowInfo, kCGWindowListOptionOnScreenOnly, kCGNullWindowID

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    level=logging.DEBUG)


window_name = "RuneLite - PureBerr"
def get_active_window_info(window_name):

    # Get information about all windows
    windows = CGWindowListCopyWindowInfo(kCGWindowListOptionOnScreenOnly, kCGNullWindowID)

    window_names = []
    for window in windows:
        window_n = window.get("kCGWindowName", "")
        owner_name = window.get("kCGWindowOwnerName", '')

        if window_n:
            window_names.append(window_n)
    print(window_names)


    # Find the  window
    for window in windows:
        if window['kCGWindowName'] == window_name:
            # Get window dimensions
            bounds = window['kCGWindowBounds']
            width = bounds['Width']
            height = bounds['Height']

            return {
                'name': window_name,
                'width': width,
                'height': height
            }

    # If no matching window found
    else:
        return ("Window not found")


# Get and print the active window information
window_info = get_active_window_info(window_name)
print(f"Window: {window_info['name']}")
print(f"Window dimensions: {window_info['width']} x {window_info['height']}")