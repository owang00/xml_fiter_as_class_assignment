import sys
import re

def escape_char(str):
    # xPattern = re.compile('&((amp)|(lt)|(gt)|(quot)|(apos)|(nbsp));')

    str = re.sub('&amp;', '&', str)
    str = re.sub('&lt;', '<', str)
    str = re.sub('&gt;', '>', str)
    str = re.sub('&quot;', '"', str)
    str = re.sub('&apos;', '\'', str)
    str = re.sub('&nbsp;', ' ', str)

    return str

def remove_style(str):
    # special treatment for the <style> tag
    str = re.sub('<style>[.\s\S]*</style>', '', str)

    return str

def filter_xml (infile, outfile):
    out_string = ''
    with open(infile) as instream:
        instring = instream.read()

        ## take care the style tags 1st
        out_string = remove_style(instring)

        xml_pattern = re.compile('<[^>]*>')
        out_string = xml_pattern.sub('', out_string)

        ### replace the special characters
        out_string = escape_char(out_string)

    with open(outfile,'w') as outstream:
        outstream.write(out_string)

def main(args):
    infile = args[1]
    split_point = infile.rindex('.')
    outfile = infile[:split_point]+'.txt'
    filter_xml(infile,outfile)

sys.exit(main(sys.argv))