import pytest
# TODO: add necessary import
from ml.model import compute_model_metrics, inference, train_model, load_model
from sklearn.metrics import fbeta_score, precision_score, recall_score
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# TODO: implement the first test. Change the function name and input as needed
def test_compute_model_metrics():
    """
 # This tests the functionality of the compute_model_metrics function in the
 # model.py file
    """
    # Your code here
    cmm_list_1 = np.array([0, 1, 0, 0, 1]) # Calling array of binary values as an array per compute_model_metrics function
    cmm_list_2 = np.array([1, 0, 1, 1, 0]) # Calling array of binary values as an array per compute_model_metrics function
    a, b, c = compute_model_metrics(cmm_list_1, cmm_list_2) # Calling the compute_model_metrics function for both arrays
    assert 0 <= a <= 1 # Asserting that Precision is between 0 and 1
    assert 0 <= b <= 1 # Asserting that Recall is between 0 and 1
    assert 0 <= c <= 1 # Asserting that F-beta (f-score) is between 0 and 1

# TODO: implement the second test. Change the function name and input as needed
def test_inference():
    """
# This tests the functionality of the inference function in the
# model.py file
    """
    # Your code here
    inf_model = RandomForestClassifier() # Calling the model RandomForestClassifier
    ti_x_data = np.array([0, 0, 1, 1, 1]) # Calling array of binary values as an array per inference function
    ti_y_data = np.array([1, 1, 0, 0, 0]) # Calling array of binary values as an array per inference function
    inf_model.fit(ti_x_data, ti_y_data) # Fits the np.arrays to the model
    predict = inference(inf_model, ti_x_data) # Stores the inference function's predictions
    result = inf_model.predict(ti_x_data) # Stores the model's predictions
    assert np.array_equal(predict, result) # Ensuring the two predictions are equal

# TODO: implement the third test. Change the function name and input as needed
def test_train_model():
    """
# This tests the functionality of the train_model function in the
# model.py file
    """
    # Your code here
    tm_x_vals = np.array([0, 0, 1, 0, 1]) # Calling array of binary values as an array per train_model function
    tm_y_vals = np.array([1, 1, 0, 1, 0]) # Calling array of binary values as an array per train_model function
    tm_model = train_model(tm_x_vals, tm_y_vals) # Calling the train_model function for both arrays
    assert isinstance(tm_model, RandomForestClassifier) # Ensuring if there is a RandomForestClassifier instance
    assert tm_model.n_estimators > 0 # Ensuring model is fitted properly

# if __name__ == "__main__":
    # pytest.main(['-v', 'test_ml.py'])

