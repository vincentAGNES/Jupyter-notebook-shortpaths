from IPython.core.display import HTML
from urllib.request import urlopen

# Styling the notebook.
cssfile = urlopen('https://raw.githubusercontent.com/vincentAGNES/CSS_Jupyter/master/jupyter_css.css')
csscontent = cssfile.read().decode('utf-8')
cssfile.close()
css_code = '<style>'+'\n'+'{}</style>'.format(csscontent)

# Remove everything but the last line.
# You might need to run this last line in another cell.
HTML(css_code) # Styling the notebook