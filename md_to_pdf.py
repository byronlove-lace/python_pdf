import pdfkit
import markdown
import subprocess
from pathlib import Path

'''
This project aims to use the markdown and pdfkit libraries to allow the user to create md files and quickly convert them 
into simple pdfs
it's designed to be run entirely from the command line
'''

'''
subprocess.run('touch pdf_blueprint.md', shell=True)
subprocess.run("pdf_blueprint.md < 'Enter text:'", shell=True)
subprocess.run('nvim +3 pdf_blueprint.md', shell=True)
'''
css_file = Path('pdf_formatting.css')

css_file.exists()
css_file.is_dir()
# with css_file.open('rb') as f:
#     css = f.read()

markdown.markdownFromFile(input='pdf_blueprint.md', output='pdf_blueprint.html')
pdfkit.from_file(input='pdf_blueprint.html', output_path='output.pdf')
