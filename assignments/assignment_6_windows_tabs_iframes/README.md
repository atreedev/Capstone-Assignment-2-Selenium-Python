# Assignment 6 - Windows, Tabs & Iframes

## Objective

Demonstrate Selenium handling of:
1. An iframe.
2. A newly opened browser window/tab.

## Demonstrated

### Iframe
- `driver.switch_to.frame()`
- Interact with an element inside the iframe.
- `driver.switch_to.default_content()`

### New Window
- `driver.window_handles`
- Switch to the new window.
- Read and verify the title.
- Close the new window.
- Switch back to the original window.

## Run

```bash
pip install -r requirements.txt
python assignment6_windows_tabs_iframes.py
```

Expected output:

```text
Iframe interaction PASSED
New window title: New Window
Window switching PASSED
Assignment 6 PASSED
```
