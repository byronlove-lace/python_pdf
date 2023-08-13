
# Watermarker

## Aim
This project aims to allow the user to create a simple watermark pdf
It will create the watermark using pandoc and css
Then apply that watermark to a pdf of the user's choice using 
pypdf

## Current Goals
- [ ] Refactor subprocess calls into a bash script
- [ ] Create css file that will center, resize, angle input
- [ ] Use pandoc to create pdf with css
- [ ] Create py script that uses said pdf as a watermark for a target pdf
- [ ] Integrate into a bash script 

## Further Expansions
Find a way to modify the Tf, Tm and Cm values of a pdf\
and use it to allow the user to change the size, font, and angle of the watermark

## Limitations


## Notes
pdfkit is just a wrapper for wkhtmltopdf 
can apply css to md and convert directly to pdf with pandoc <3
with wkhtmltopdf as the engine 

