import os
from train_model import train_and_save_model


def test_train_and_save_model():
    train_and_save_model()
    assert os.path.exists("model.joblib")
