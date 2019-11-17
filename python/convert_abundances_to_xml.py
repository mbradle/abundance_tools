import argparse
import numpy as np
import wnutils.base as wub
from lxml import etree

wb = wub.Base()

parser = argparse.ArgumentParser(description='Convert abundance text to xml')

parser.add_argument('text_file', metavar='text_file', type=str,
                    help='the input text file')

parser.add_argument('xml_file', metavar='xml_file', type=str,
                    help='the output xml file')

args = parser.parse_args()

f = np.genfromtxt(args.text_file, dtype = str)

z = f[:,0].astype(int)
a = f[:,1].astype(int)
y = f[:,2].astype(float)

x = a * y
x /= np.sum(x)

zone_data = etree.Element("zone_data")
zone = etree.SubElement(zone_data, "zone")

for i in range(len(z)):
    nuclide = etree.SubElement(zone, "nuclide")
    attributes = nuclide.attrib
    attributes["name"] = wb.create_nuclide_name(z[i], a[i], '')
    ze = etree.SubElement(nuclide, "z")
    ze.text = str(z[i])
    ae = etree.SubElement(nuclide, "a")
    ae.text = str(a[i])
    xe = etree.SubElement(nuclide, "x")
    xe.text = str(x[i])
    
et = etree.ElementTree(zone_data)
et.write(args.xml_file, pretty_print=True)
