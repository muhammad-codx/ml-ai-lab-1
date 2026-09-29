import math

from dataset import TRAINING_DATA


def get_target_labels(dataset):
    labels = []

    for row in dataset:
        labels.append(row["Target"])

    return labels


def entropy(labels):
    counts = {}


    for label in labels:
        if label not in counts:
            counts[label] = 0

        counts[label] += 1

    total = len(labels)
    result = 0.0

    for count in counts.values():
        probability = count / total

        result -= probability * math.log2(probability)

    return result


def split_dataset(dataset, feature):
    subsets = {}

    for row in dataset:
        value = row[feature]

        if value not in subsets:
            subsets[value] = []

        subsets[value].append(row)

    return subsets


def weighted_entropy(dataset, feature):
    subsets = split_dataset(dataset, feature)

    total_samples = len(dataset)
    result = 0.0

    for subset in subsets.values():
        subset_labels = get_target_labels(subset)

        subset_entropy = entropy(subset_labels)

        weight = len(subset) / total_samples

        result += weight * subset_entropy

    return result


def information_gain(dataset, feature):
    parent_labels = get_target_labels(dataset)

    parent_entropy = entropy(parent_labels)

    child_weighted_entropy = weighted_entropy(
        dataset,
        feature
    )

    gain = parent_entropy - child_weighted_entropy

    return gain


if __name__ == "__main__":

    labels = get_target_labels(TRAINING_DATA)

    root_entropy = entropy(labels)

    print("Root Entropy:")
    print(root_entropy)

    print()

    weather_subsets = split_dataset(
        TRAINING_DATA,
        "Weather"
    )

    print("Weather subsets:")

    for weather, subset in weather_subsets.items():

        subset_labels = get_target_labels(subset)

        print(
            weather,
            "samples:",
            len(subset),
            "entropy:",
            entropy(subset_labels)
        )

    print()

    weather_weighted_entropy = weighted_entropy(
        TRAINING_DATA,
        "Weather"
    )

    weather_gain = information_gain(
        TRAINING_DATA,
        "Weather"
    )

    print("Weighted Entropy for Weather:")
    print(weather_weighted_entropy)

    print()

    print("Information Gain for Weather:")
    print(weather_gain)