import argparse
from lxml import etree

def get_mass_fractions(xml_file, nuc_xpath):
    data = {}
    root = etree.parse(xml_file).getroot()
    
    nuclides = root.xpath('//nuclide' + nuc_xpath)

    for nuc in nuclides:
        name = nuc.attrib['name']
        x = float(nuc.xpath('x')[0].text)
        data[name] = x

    return data
      
parser = argparse.ArgumentParser(description='Print mass fractions from xml')

parser.add_argument('xml_file', metavar='xml_file', type=str,
                    help='the input xml file')

parser.add_argument('--nuc_xpath', metavar='nuc_xpath', type=str,
                    default = '',
                    help='the nuclear xpath to select nuclides')

args = parser.parse_args()

data = get_mass_fractions(args.xml_file, args.nuc_xpath)

for d in data:
    print(d, data[d])


