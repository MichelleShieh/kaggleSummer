import csv
import numpy as np
from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sets import Set
from sklearn.datasets import load_iris
import pdb


def readRawData(filename):
	'''
	get string format data
	'''
	with open(filename, 'rb') as csvfile:
		data = csv.reader(csvfile)
		RawData = [row for row in data]
	return RawData

def featureExtraction(RawData, abandon):
	'''
	transfer data from string format to numerical format, but still are categorical data
	'''
	categories = {}
	for i in range(len(RawData[0])):
		categories[RawData[0][i]] = list(Set([row[i] for row in RawData[1:]]))

	#print RawData[0], len(RawData[0])
	#print categories['action_type']
	#print categories['combined_shot_type']
	#print categories['shot_zone_range']
	#print categories['shot_zone_area']
	#print categories['shot_zone_basic']
	#print sorted([int(dist) for dist in categories['shot_distance']])
	#print sorted([int(dist) for dist in categories['seconds_remaining']])
	#print sorted([int(dist) for dist in categories['minutes_remaining']])
	
	FeatureM_test = []
	FeatureM_train = []
	Labels_train = []
	for shot in RawData[1: ]:
		temp = []
		train = True
		for num_key in range(len(categories.keys())):
			if categories.keys()[num_key] == 'shot_made_flag':
				if shot[RawData[0].index(categories.keys()[num_key])] == '-1':
					train = False
				continue
			elif categories.keys()[num_key] in abandon:
				continue
			temp.append(categories[categories.keys()[num_key]].index(shot[RawData[0].index(categories.keys()[num_key])]))
		if train:
			FeatureM_train.append(temp)
			Labels_train.append(int(shot[RawData[0].index('shot_made_flag')]))
		else:
			FeatureM_test.append(temp)

	print 'features are:'
	print list(Set(categories.keys()) - Set(abandon))
	return np.array(FeatureM_train), np.array(Labels_train), np.array(FeatureM_test)

def main():
	RawData = readRawData('data.csv')
	abandon = ['matchup', 'team_name', 'team_id', 'lon', 'lat', 'loc_x', 'loc_y', 'game_id', 'shot_id', 'seconds_remaining', 'game_event_id']
	FeatureM_train, Labels_train, FeatureM_test = featureExtraction(RawData, abandon)
	print FeatureM_train.shape, FeatureM_test.shape, Labels_train.shape
	
	print 'try out random forest'
	clf = RandomForestClassifier(n_estimators = 201)
	scores = cross_val_score(clf, FeatureM_train, Labels_train, cv = 5)
	clf.fit(FeatureM_train, Labels_train)
	Labels_test = clf.predict(FeatureM_test)
	print 'average score: ', scores.mean()

	print 'do predction'
	index1 = RawData[0].index('shot_made_flag')
	index2 = RawData[0].index('shot_id')
	predction = []
	position = 0
	for shot in RawData:
		if shot[index1] == '-1':
			predction.append(shot[index2] + ',' + str(Labels_test[position]))
			position += 1
	print 'should be 5000', position
	f = open('predction.csv', 'w')
	f.write('shot_id,shot_made_flag\n')
	for predict in predction:
		f.write(predict + '\n')







if __name__ == '__main__':
	main()
