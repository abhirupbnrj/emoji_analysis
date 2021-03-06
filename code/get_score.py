# mail function to run
# takes the screenshot as input and outputs the sentiment score

import os
import sys
import pandas as pd
from tqdm import tqdm
from core.name_to_score import name_2_score
from utils.ss_to_image import final_crop


if __name__ == '__main__':

	name = sys.argv[1] + '.jpeg'
	file_path = '../resource/screenshots/' + sys.argv[1] + '.jpeg'
	
	if name in os.listdir('../resource/screenshots/'):

		cropped_image = final_crop(file_path)
		l = name_2_score(cropped_image)
		print('')
		print(' Negative : ',l[0].round(3))
		print(' Neutral  : ',l[1].round(3))
		print(' Positive : ',l[2].round(3))
		print('')
	
	else:
		file_name = '../resource/screenshots/' + str(sys.argv[1])

		l_neg = []
		l_net = []
		l_pos = []

		for i in tqdm(os.listdir(file_name), bar_format='{l_bar}{bar:20}{r_bar}{bar:-20b}'):
			
		    file_path = os.path.join(file_name, i)

		    cropped_image = final_crop(file_path)
		    l_neg.append(name_2_score(cropped_image)[0].round(3))
		    l_net.append(name_2_score(cropped_image)[1].round(3))
		    l_pos.append(name_2_score(cropped_image)[2].round(3))

		df = pd.DataFrame({'negative' : l_neg,
				   'neutral'  :	l_net,
				   'positive' : l_pos})		
		print(df)



