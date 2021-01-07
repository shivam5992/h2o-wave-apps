import driverlessai, os
import pandas as pd

class DriverlessPredict:

	def __init__(self, config):
		self.dai, self.exp = self.dai_connect(config)

	def dai_connect(self, config):
		dai = driverlessai.Client(address = config['address'], username = config['username'], 
									password = config['password'], backend_version_override='latest')
		exp = dai.experiments.get(config['experiment_key'])
		return dai, exp


	def dai_predict(self, input_path):
		dai_table = self.dai.datasets.create(input_path, force=True)
		pred_path = self.exp.predict(dai_table).download('datasets/', overwrite=True)
		os.rename(pred_path, "datasets/credit_predictions.csv")
		return pd.read_csv("datasets/credit_predictions.csv")