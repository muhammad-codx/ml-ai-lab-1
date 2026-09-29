from dataset import (
    TRAINING_DATA,
    TEST_DATA,
    FEATURES,
    CLASSES
)

from task3 import build_tree
from task4 import classify_test_data


def build_confusion_matrix(results, classes):
    matrix = {}

    for actual in classes:
        matrix[actual] = {}

        for predicted in classes:
            matrix[actual][predicted] = 0

    for result in results:
        actual = result["Actual"]
        predicted = result["Prediction"]

        matrix[actual][predicted] += 1

    return matrix


def calculate_accuracy(matrix, classes):
    correct = 0
    total = 0

    for actual in classes:
        for predicted in classes:
            value = matrix[actual][predicted]

            total += value

            if actual == predicted:
                correct += value

    return correct / total


def most_confused_class(matrix, classes):
    result_class = classes[0]
    highest_confusion = -1

    for actual in classes:
        confused = 0

        for predicted in classes:
            if actual != predicted:
                confused += matrix[actual][predicted]

        if confused > highest_confusion:
            highest_confusion = confused
            result_class = actual

    return result_class, highest_confusion


def print_confusion_matrix(matrix, classes):
    print(
        f"{'Actual / Predicted':<20}",
        end=""
    )

    for predicted in classes:
        print(
            f"{predicted:<15}",
            end=""
        )

    print()

    for actual in classes:
        print(
            f"{actual:<20}",
            end=""
        )

        for predicted in classes:
            print(
                f"{matrix[actual][predicted]:<15}",
                end=""
            )

        print()


if __name__ == "__main__":
    tree = build_tree(
        TRAINING_DATA,
        FEATURES
    )

    results = classify_test_data(
        tree,
        TEST_DATA
    )

    matrix = build_confusion_matrix(
        results,
        CLASSES
    )

    print("Confusion Matrix")
    print("----------------")

    print_confusion_matrix(
        matrix,
        CLASSES
    )

    accuracy = calculate_accuracy(
        matrix,
        CLASSES
    )

    confused_class, confused_count = most_confused_class(
        matrix,
        CLASSES
    )

    print()
    print(
        "Accuracy:",
        f"{accuracy * 100:.2f}%"
    )

    print(
        "Most confused class:",
        confused_class
    )

    print(
        "Number of misclassifications:",
        confused_count
    )