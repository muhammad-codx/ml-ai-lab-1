# ID3 Decision Tree from Scratch

This project implements the **ID3 Decision Tree algorithm from scratch using Core Python only**.

The goal is to predict parcel delivery status using categorical features such as traffic, weather, courier load, and distance.

The model predicts one of three classes:

- `ON_TIME`
- `DELAYED`
- `SEVERE_DELAY`

No machine learning libraries such as `scikit-learn` are used.

## Student Information

**Name:** Akbarshoh Boymirzayev  
**Student ID:** SE16017

## Project Structure

```text
assignment/
├── dataset.py
├── task1.py
├── task2.py
├── task3.py
├── task4.py
├── task5.py
├── main.py
└── README.md
```

## Files

### `dataset.py`

Contains:

- Training dataset
- Test dataset
- Feature list
- Target class list

### `task1.py`

Implements:

- Entropy calculation
- Dataset splitting
- Weighted entropy
- Information Gain calculation

It also calculates the Information Gain for the `Weather` feature.

### `task2.py`

Calculates the Information Gain for all available features:

- Traffic
- Weather
- Courier Load
- Distance

The feature with the highest Information Gain is selected as the root node.

A deterministic feature order is used when two features have equal Information Gain.

### `task3.py`

Builds the complete ID3 Decision Tree recursively.

The recursion stops when:

- All samples belong to the same class
- No unused features remain

If no features remain, the majority class is used as the leaf prediction.

### `task4.py`

Uses the trained decision tree to classify the test parcels.

For every parcel, the program prints:

- Parcel ID
- Predicted class
- Root-to-leaf decision path

Example:

```text
Parcel: T6
Prediction: SEVERE_DELAY
Path: Traffic=High -> Weather=Rain -> SEVERE_DELAY
```

### `task5.py`

Evaluates the model using:

- 3×3 Confusion Matrix
- Accuracy
- Most frequently confused class

Rows represent actual classes and columns represent predicted classes.

### `main.py`

Runs all five tasks in sequence.

This is the main entry point of the project.

## How to Run

Make sure Python 3 is installed.

Run the complete project with:

```bash
python main.py
```

Individual tasks can also be executed separately:

```bash
python task1.py
python task2.py
python task3.py
python task4.py
python task5.py
```

## ID3 Algorithm

At every node, ID3 selects the feature with the highest Information Gain.

Entropy is calculated as:

```text
H(D) = -Σ p(k) log2(p(k))
```

Weighted entropy after splitting by feature `A`:

```text
H(D | A) = Σ (|Dv| / |D|) × H(Dv)
```

Information Gain:

```text
IG(D, A) = H(D) - H(D | A)
```

The feature with the largest Information Gain is selected for the next decision node.

## Root Feature

For the provided training dataset, the Information Gain values are approximately:

```text
Traffic         0.493994
Weather         0.191856
Courier Load    0.432499
Distance        0.083007
```

Therefore, the selected root feature is:

```text
Traffic
```

## Requirements

- Python 3
- No external libraries required

Only standard Python functionality is used, including:

- Lists
- Dictionaries
- Loops
- Functions
- Recursion
- `math.log2()`

## Author

**Akbarshoh Boymirzayev**  
**Student ID: SE16017**
