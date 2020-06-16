import zipfile
import xml.etree.ElementTree as ET
import os


def read_brml(path, as_text=False):
    """ Function that reads Brucker .brml files and returns 2theta angles
    and intensity in a as lists
    """
    with zipfile.ZipFile(path) as brml:
        with brml.open('Experiment0/RawData0.xml', 'r') as xml_file:
            xml_content = xml_file.readlines()
    xml_tree = ET.fromstringlist(xml_content)
    data = xml_tree.find('DataRoutes').find('DataRoute').findall('Datum')
    data_list = (datum.text.split(',') for datum in data)
    dat_data = [[two_theta, I] for _, _, two_theta, _, I in data_list]
    if as_text:
        return dat_data
    else:
        return [[float(two_theta), float(I)] for two_theta, I in dat_data]


def write_dat(dat_filename, dat_data, sep=' '):
    """ Write a .dat file from array like objects
    """
    with open(dat_filename, 'w') as dat_file:
        for dat_datum in dat_data:
            two_theta, intensity = dat_datum
            row = '{}{}{}\n'.format(two_theta, sep, intensity)
            dat_file.write(row)


def convert_all_brml_in_folder(path=os.getcwd()):
    items = os.listdir(path)
    for item in items:
        print(item[-5:])
        if item[-5:] == '.brml':
            dat_data = read_brml('{}\\{}'.format(path, item))
            print(dat_data)
            dat_path = '{}\\{}.dat'.format(path, item[:-5])
            write_dat(dat_path, dat_data)
