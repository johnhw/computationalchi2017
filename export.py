### Run this cell to export your work as a zip file you can keep on
### your local machine
import ipywidgets as widgets
import IPython
import os
from IPython.display import HTML
button = widgets.Button(description='Export as ZIP')

def download(x):
    IPython.display.clear_output()
    IPython.display.display(HTML('Creating ZIP file...'))    
    os.system("rm -f export_chi17.zip")
    os.system("zip -r export_chi17.zip *")
    IPython.display.clear_output()
    IPython.display.display(HTML('<a href="export_chi17.zip" target="_blank">Download ZIP</a>'))    


button.on_click(download)
def show_button():
    
    IPython.display.display(button)