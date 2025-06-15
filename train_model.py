import joblib
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression

def train_and_save_model():
    data = load_diabetes()
    x,y = data.data, data.target 
    
    model = LinearRegression()
    model.fit(x,y)
    
    joblib.dump(model, "model.joblib")
    
    
if __name__ == "__main__":
    train_and_save_model()
    