from data.dataset import generate_realistic_dataset
from features.feature_engineering import create_features
from models.train_model import train
from evaluation.eva import evaluate

def main():
    df = generate_realistic_dataset()

    X, y = create_features(df)

    model, scaler, X_test, y_test = train(X, y)

    evaluate(model, X_test, y_test)

if __name__ == "__main__":
    main()