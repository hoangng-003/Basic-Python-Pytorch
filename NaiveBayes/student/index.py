
# Naive Bayes Classification Model

import csv
import random

# Prepare Data


def load_data(file):
    csv_reader = csv.reader(file, delimiter=",")
    csv_list = list(csv_reader)
    dataset = [[]]
    schoolsup_index = csv_list[0].index("schoolsup")
    activities_index = csv_list[0].index("activities")
    internet_index = csv_list[0].index("internet")
    romantic_index = csv_list[0].index("romantic")

    for i in range(len(csv_list)):
        dataset[i].append(csv_list[i][schoolsup_index])
        dataset[i].append(csv_list[i][activities_index])
        dataset[i].append(csv_list[i][internet_index])
        dataset[i].append(csv_list[i][romantic_index])
        # print(dataset[i][0] + "-" + dataset[i][1] +
        #       "-" + dataset[i][2] + "-" + dataset[i][3])
        dataset.append([])
    return dataset


def split_data(dataset, trainAmount):
    trainSet = []
    testSet = dataset
    while len(trainSet) < trainAmount:
        index = random.randrange(len(testSet))
        trainSet.append(testSet.pop(index))

    return [trainSet, testSet]

# Train Model


def prop_absolute_j_and_result(j, target_j, result, dataset):
    count_absolute_j_and_result = 0
    for i in range(len(dataset)-1):
        if dataset[i][j] == target_j and dataset[i][3] == result:
            count_absolute_j_and_result += 1
    return count_absolute_j_and_result / len(dataset)


def prop_result(result, dataset):
    count = 0
    for i in range(len(dataset)-1):
        if dataset[i][3] == result:
            count += 1
    return count / len(dataset)


def prop_absolute_j_know_result(j, target_j, result, dataset):
    return prop_absolute_j_and_result(j, target_j, result, dataset) / prop_result(result, dataset)


def solutions(prop_x_know_result, result, dataset):
    return prop_x_know_result*prop_result(result, dataset)


with open('NaiveBayes/student/data/student-mat.csv') as csv_file:
    dataset = load_data(csv_file)
    print(prop_result("yes", dataset))
    # x = {no, no, yes}

    yes = [0, 1, 2]
    yes[0] = prop_absolute_j_know_result(0, 'no', 'yes', dataset)
    yes[1] = prop_absolute_j_know_result(1, 'no', 'yes', dataset)
    yes[2] = prop_absolute_j_know_result(2, 'yes', 'yes', dataset)

    x_yes = yes[0]*yes[1]*yes[2]

    no = [0, 1, 2]
    no[0] = prop_absolute_j_know_result(0, 'no', 'no', dataset)
    no[1] = prop_absolute_j_know_result(1, 'no', 'no', dataset)
    no[2] = prop_absolute_j_know_result(2, 'yes', 'no', dataset)

    x_no = no[0]*no[1]*no[2]

    prop_yes = solutions(x_yes, 'yes', dataset)
    prop_no = solutions(x_no, 'no', dataset)

    if prop_yes > prop_no:
        print(
            "with set of values x = { schoolsup = no , activities = no , internet = yes } , this Object is Romantic ")
    else:
        print(
            "with set of values x = { schoolsup = no , activities = no , internet = yes } , this Object is NOT Romantic ")
