import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import Binarizer

class EarthquakeDataPreprocessor:

  """
  A class for preprocessing earthquake prediction data.

  Args:
    data: The input data.
    remove_nan: Whether to remove NaN values.
    remove_duplicates: Whether to remove duplicate rows.
    binarize_magnitude: Whether to binarize the magnitude column.
    threshold: The threshold for binarization.
    test_size: The size of the test set.
    validation_size: The size of the validation set.
    n: The number of rows to remove between the training and testing/validation sets.
    normalize_data: Whether to normalize the data.
  """

  def __init__(self, data, remove_nan=False, remove_duplicates=False, binarize_magnitude=True, threshold=5, test_size=0.3, validation_size=0.3, n=50, normalize_data=False):
    self.data = data
    self.remove_nan = remove_nan
    self.remove_duplicates = remove_duplicates
    self.binarize_magnitude = binarize_magnitude
    self.threshold = threshold
    self.test_size = test_size
    self.validation_size = validation_size
    self.n = n
    self.normalize_data = normalize_data

  def _remove_nan(self):
    """
    Remove NaN values from the data.
    """

    if self.remove_nan:
      self.data.dropna(axis=0, inplace=True)

  def _remove_duplicates(self):
    """
    Remove duplicate rows from the data.
    """

    if self.remove_duplicates:
      self.data.drop_duplicates(inplace=True)

  def _binarize_magnitude(self):
    """
    Binarize the magnitude column.
    """

    if self.binarize_magnitude:
      self.data.iloc[:, -1] = self.data.iloc[:, -1] >= self.threshold

  def _split_train_test(self):
    """
    Split the data into training and testing sets.
    """

    train_data, test_data = train_test_split(self.data, test_size=self.test_size, shuffle=False)
    return train_data[:-self.n], test_data

  def _split_train_validation(self, train_data):
    """
    Split the training data into training and validation sets.
    """

    train_data, validation_data = train_test_split(train_data, test_size=self.validation_size,shuffle=False)
    return train_data[:-self.n], validation_data

  def _normalize_data(self, train_data):
    """
    Normalize the data.
    """

    if self.normalize_data:
      mean = train_data.mean()
      std = train_data.std()
      self.data = (self.data - mean) / std

  def get_datasets(self):
    """
    Get the training, validation, and testing sets.

    Returns:
      The training, validation, and testing sets.
    """

    # Remove NaN values
    self._remove_nan()

    # Remove duplicate rows
    self._remove_duplicates()

    # Binarize the magnitude column
    self._binarize_magnitude()

    # Split the data into training and testing sets
    train_data, test_data = self._split_train_test()
    # Normalize the data
    self._normalize_data(train_data)
    # Split the data into training and testing sets again
    train_data, test_data = self._split_train_test()
    # Split the training data into training and validation sets
    train_data, validation_data = self._split_train_validation(train_data)


    return train_data, validation_data, test_data
