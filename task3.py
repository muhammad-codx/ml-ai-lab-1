from dataset import TRAINING_DATA, FEATURES
from task1 import get_target_labels, split_dataset
from task2 import select_best_feature


def majority_class(dataset):
    counts = {}

    for row in dataset:
        target = row["Target"]
        counts[target] = counts.get(target, 0) + 1

    majority = None
    highest_count = -1

    for target, count in counts.items():
        if count > highest_count:
            highest_count = count
            majority = target

    return majority


def build_tree(dataset, features):
    labels = get_target_labels(dataset)


    if len(set(labels)) == 1:
        return {
            "type": "leaf",
            "class": labels[0]
        }


    if len(features) == 0:
        return {
            "type": "leaf",
            "class": majority_class(dataset)
        }

    best_feature, best_gain = select_best_feature(
        dataset,
        features
    )

    tree = {
        "type": "node",
        "feature": best_feature,
        "majority": majority_class(dataset),
        "branches": {}
    }

    subsets = split_dataset(
        dataset,
        best_feature
    )

    remaining_features = []

    for feature in features:
        if feature != best_feature:
            remaining_features.append(feature)

    for value, subset in subsets.items():
        tree["branches"][value] = build_tree(
            subset,
            remaining_features
        )

    return tree


def print_tree(tree, indent=""):
    if tree["type"] == "leaf":
        print(indent + "-> " + tree["class"])
        return

    feature = tree["feature"]

    print(indent + feature)

    for value, child in tree["branches"].items():
        print(indent + "  [" + value + "]")

        print_tree(
            child,
            indent + "      "
        )


if __name__ == "__main__":
    tree = build_tree(
        TRAINING_DATA,
        FEATURES
    )

    print("ID3 Decision Tree")
    print("-----------------")

    print_tree(tree)