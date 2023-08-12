import pdfkit
import markdown
import subprocess
from pathlib import Path

'''
This project aims to use the markdown and pdfkit libraries to allow the user to create md files and quickly convert them 
into simple pdfs
it's designed to be run entirely from the command line
'''

subprocess.run('touch pdf_blueprint.md', shell=True)
subprocess.run("pdf_blueprint.md < 'Enter text:'", shell=True)
subprocess.run('nvim +3 pdf_blueprint.md', shell=True)


markdown.markdownFromFile(input='pdf_blueprint.md', output='pdf_blueprint.html')