import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET

PROJECT = './project_images/boxes/'

def xml_to_csv(path):
	xml_list = []
	for xml_file in glob.glob(path + '/*.xml'):
		tree = ET.parse(xml_file)
		root = tree.getroot()
		for member in root.findall('object'):
			value = (root.find('filename').text,
				     int(root.find('size').find('width').text),
				     int(root.find('size').find('height').text),
				     member.find('name').text,
				     int(member.find('bndbox').find('xmin').text),
				     int(member.find('bndbox').find('ymin').text),
				     int(member.find('bndbox').find('xmax').text),
				     int(member.find('bndbox').find('ymax').text))
			xml_list.append(value)
	column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
	xml_df = pd.DataFrame(xml_list, columns=column_name)
	return xml_df

def main():
	for folder in ['train', 'test']:
		image_path = os.path.join(os.getcwd(), (PROJECT + folder))
		xml_df = xml_to_csv(image_path)

		csv_path = PROJECT + folder + '_labels.csv'
		if not os.path.isfile(csv_path):
			fp = open(csv_path, 'w')
			fp.close()
		xml_df.to_csv(csv_path, index=None)
		print('Successfully converted xml to csv.')

main()