import torch
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ai_anomaly_detection import model

def test_prediction():
    sample = torch.tensor([[60000, 6]], dtype=torch.float)

    output = model(sample)

    #model should produce a tensor output
    assert output.shape == (1,1)
