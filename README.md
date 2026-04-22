#  ML-Based Loop Unrolling Factor Predictor

##  Overview

This project builds a **Machine Learning model** to predict the optimal **loop unrolling factor (1, 2, 4, 8)** using compiler-style loop features.

Loop unrolling is a key **compiler optimization technique** used to improve performance by reducing loop overhead and increasing instruction-level parallelism.

Instead of relying on static heuristics, this project uses **ML models** to make smarter decisions based on loop characteristics.

---

##  Objectives

* Simulate compiler-level loop features
* Perform feature engineering
* Train ML models to predict optimal unroll factor
* Compare ML model performance with traditional heuristic
* Demonstrate improvement over rule-based approaches

---

##  Features Used

The model uses the following loop features:

* `trip_count` → Number of loop iterations
* `body_instr_count` → Instructions inside loop
* `memory_accesses` → Load/store operations
* `has_branch` → Branch inside loop
* `loop_depth` → Nesting level
* `vectorizable` → Whether loop can be vectorized
* `live_vars` → Register pressure indicator
* `cache_line_hits` → Memory locality

###  Engineered Features

* `body_per_trip`
* `memory_density`
* `register_pressure`
* `unroll_friendly`

---

##  Project Structure

```
loop-unroll-predictor/
│
├── data/                  # Dataset generation
├── features/              # Feature engineering
├── models/                # Model training
├── evaluation/            # Model evaluation
├── utils/                 # Heuristic baseline
├── inference/             # Prediction logic
│
├── main.py                # Entry point
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation & Setup

###  Clone the repository

```bash
git clone https://github.com/jyotipatthak/loop-unroll-predictor.git
cd loop-unroll-predictor
```

###  Create virtual environment (recommended)

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

###  Install dependencies

```bash
pip install -r requirements.txt
```

---

##  How to Run the Project

Run the main script:

```bash
python main.py
```

---

##  Output Explanation

When you run the project, you will see:

###  Model Training Results

The model compares:

* Random Forest
* Gradient Boosting

It selects the **best-performing model**

---

###  Classification Report

Example:


              precision    recall  f1-score   support

factor=1       0.90       0.92       0.91
factor=2       0.85       0.83       0.84
factor=4       0.88       0.87       0.87
factor=8       0.91       0.89       0.90

accuracy                           0.88
```

 Meaning:

* Model predicts loop unrolling factor with ~88% accuracy
* Shows precision, recall, F1-score for each class

---

### 3 Baseline vs ML Comparison

```
Baseline Heuristic Accuracy : 0.73
ML Model Accuracy           : 0.88
Improvement                 : +15%
```

 Meaning:

* Traditional compiler heuristic is less accurate
* ML model significantly improves performance

---

###  Confusion Matrix & Feature Importance

A plot file will be generated:

```
loop_unroll_results.png
```

This includes:

* Feature importance (which features matter most)
* Confusion matrix (prediction vs actual)

---

### 5️ Inference Example

Example output:

```
Loop features: trip=64, body=6 instrs, vectorizable=True
Predicted unroll factor: 8x
Confidence: {1: '2%', 2: '5%', 4: '10%', 8: '83%'}
```

 Meaning:

* Model predicts best unroll factor = **8**
* Shows confidence distribution

---

##  Key Results

* ✅ Accuracy: ~88%
* ✅ Outperforms heuristic by ~15%
* ✅ Handles complex loop patterns better than static rules

---

##  Tech Stack

* Python
* NumPy, Pandas
* Scikit-learn
* Matplotlib, Seaborn

---

##  Future Improvements

* Integrate real LLVM IR data instead of synthetic dataset
* Deploy as REST API (Flask / FastAPI)
* Build frontend visualization dashboard (React)
* Add deep learning models

---



##  Conclusion

This project demonstrates how **Machine Learning can enhance compiler optimizations**, making decisions more adaptive and data-driven compared to static heuristics.

---
