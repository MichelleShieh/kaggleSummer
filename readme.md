1.feature engineering
brianstorming features => create features => check features with algorithm model => improve features if needed(avoid over-fitting)
异常值处理（eg.outlier），数据分布倾斜（log，正负样本重新抽样），特征交叉组合（X1X2)，ratio（e.g.增长率），特征之间的相关系数？，特征onehotencoding？，

2.models (one per person per two weeks)
	logitstic regression：对feature要求高
	random decision forest：跑的快还有feature selection功能
	factorization matchines
	Boosted Decision Tree：
		extreme gradient boosting (xgboost): python上有实现的包  http://cos.name/2015/03/xgboost/
		gradient boost decision tree(gbdt)
	Deep neural network：能为最后的model ensemble提供一个供选择的模型， 由于training的时间跟neuralnetwork的大小， 还有数据量的大小都有关， 如果没有GPU支持的话， 很多都需要training很久的时间

3.cross validation test (2份training，1份test)

4.ensemble learning (e.g.random forest + gbdt)
https://en.wikipedia.org/wiki/Ensemble_learning

