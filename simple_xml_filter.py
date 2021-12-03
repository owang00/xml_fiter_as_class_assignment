import sys

def filter_xml (infile, outfile):
    import re
    out_string = ''
    with open(infile) as instream:
        instring = instream.read()
        xml_pattern = re.compile('<[^>]*>')
        out_string = xml_pattern.sub('',instring)
    with open(outfile,'w') as outstream:
        outstream.write(out_string)

def main(args):
    infile = args[1]
    split_point = infile.rindex('.')
    outfile = infile[:split_point]+'.txt'
    filter_xml(infile,outfile)

sys.exit(main(sys.argv))
