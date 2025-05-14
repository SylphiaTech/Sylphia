from backend.model import SomeModel

def test_model_prediction():
    model = SomeModel()
    result = model.predict([1, 2, 3])
    assert isinstance(result, float)