import os, os.path

for filename in os.listdir('.'):
    name, ext = os.path.splitext(filename)

    if ext == '.svg':
        print name
        os.system('/Applications/Inkscape.app/Contents/Resources/bin/inkscape -f %s.svg -E %s.eps --export-text-to-path --export-bbox-page' % ((name,)*2) )
        #os.system('pdf2ps %s.pdf %s.ps' % ((name,)*2) )

