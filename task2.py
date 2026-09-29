from dataset import TRAINING_DATA, FEATURES
from task1 import information_gain


def select_best_feature(dataset, features):
    best_feature = features[0]
    best_gain = information_gain(dataset, best_feature)

    for feature in features[1:]:
        gain = information_gain(dataset, feature)

        if gain > best_gain:
            best_gain = gain
            best_feature = feature

    return best_feature, best_gain


if __name__ == "__main__":
    print("Feature Information Gain")
    print("------------------------")

    for feature in FEATURES:
        gain = information_gain(
            TRAINING_DATA,
            feature
        )

        print(f"{feature:<15} {gain:.6f}")

    best_feature, best_gain = select_best_feature(
        TRAINING_DATA,
        FEATURES
    )

    print()
    print("Selected Root Feature:", best_feature)
    print("Information Gain:", round(best_gain, 6))