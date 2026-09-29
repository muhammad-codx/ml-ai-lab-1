from dataset import TRAINING_DATA, TEST_DATA, FEATURES
from task3 import build_tree


def predict(tree, sample):
    path = []

    current = tree

    while current["type"] != "leaf":
        feature = current["feature"]

        value = sample[feature]

        path.append(
            feature + "=" + value
        )

        if value not in current["branches"]:
            prediction = current["majority"]

            path.append(prediction)

            return prediction, path

        current = current["branches"][value]

    prediction = current["class"]

    path.append(prediction)

    return prediction, path


def classify_test_data(tree, test_data):
    results = []

    for sample in test_data:
        prediction, path = predict(
            tree,
            sample
        )

        results.append({
            "Parcel": sample["Parcel"],
            "Prediction": prediction,
            "Actual": sample["Actual"],
            "Path": path
        })

    return results


if __name__ == "__main__":
    tree = build_tree(
        TRAINING_DATA,
        FEATURES
    )

    results = classify_test_data(
        tree,
        TEST_DATA
    )

    for result in results:
        print(result["Parcel"])
        print("Prediction:", result["Prediction"])
        print(
            "Path:",
            " -> ".join(result["Path"])
        )
        print()