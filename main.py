from dataset import TRAINING_DATA, TEST_DATA, FEATURES, CLASSES

from task1 import (
    get_target_labels,
    entropy,
    information_gain
)

from task2 import select_best_feature

from task3 import (
    build_tree,
    print_tree
)

from task4 import classify_test_data

from task5 import (
    build_confusion_matrix,
    calculate_accuracy,
    most_confused_class,
    print_confusion_matrix
)


def main():


    print("========== TASK 1 ==========")

    root_entropy = entropy(
        get_target_labels(TRAINING_DATA)
    )

    weather_gain = information_gain(
        TRAINING_DATA,
        "Weather"
    )

    print("Root Entropy:", root_entropy)
    print("Weather Information Gain:", weather_gain)



    print("\n========== TASK 2 ==========")

    for feature in FEATURES:
        gain = information_gain(
            TRAINING_DATA,
            feature
        )

        print(
            f"{feature:<15} {gain:.6f}"
        )

    best_feature, best_gain = select_best_feature(
        TRAINING_DATA,
        FEATURES
    )

    print()
    print("Selected Root Feature:", best_feature)
    print("Information Gain:", round(best_gain, 6))



    print("\n========== TASK 3 ==========")

    tree = build_tree(
        TRAINING_DATA,
        FEATURES
    )

    print_tree(tree)



    print("\n========== TASK 4 ==========")

    results = classify_test_data(
        tree,
        TEST_DATA
    )

    for result in results:
        print()
        print("Parcel:", result["Parcel"])
        print("Prediction:", result["Prediction"])
        print(
            "Path:",
            " -> ".join(result["Path"])
        )


    print("\n========== TASK 5 ==========")

    matrix = build_confusion_matrix(
        results,
        CLASSES
    )

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
        "Misclassifications:",
        confused_count
    )


if __name__ == "__main__":
    main()