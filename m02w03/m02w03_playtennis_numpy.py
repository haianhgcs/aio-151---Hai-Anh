import numpy as np
import pandas as pd


def create_train_data(data):
    return np.array(data)


def compute_prior_probability(train_data):
    unique, counts = np.unique(train_data, return_counts=True)
    total_count = len(train_data)
    prior_prob = counts / total_count

    return dict(zip(unique, prior_prob))


def compute_conditional_probability(train_data):
    y_unique = ['No', 'Yes']
    conditional_probability = []
    list_x_name = []

    for i in range(0, train_data.shape[1]-1):
        x_unique = np.unique(train_data[:, i])
        list_x_name.append(x_unique)
        x_conditional_probability = np.zeros((len(y_unique), len(x_unique)))
        for j in range(len(y_unique)):
            for k in range(len(x_unique)):
                df_y_condition = np.nonzero(
                    train_data[:, -1] == y_unique[j])[0]
                df_x = np.nonzero(
                    (train_data[:, i] == x_unique[k]) & (train_data[:, -1] == y_unique[j]))[0]
                x_conditional_probability[j, k] = len(
                    df_x) / len(df_y_condition)
        conditional_probability.append(x_conditional_probability)
    return conditional_probability, list_x_name


def get_index_from_value(feature_name, list_features):
    # This function is used to return the index of the feature name
    return np.nonzero(list_features == feature_name)[0][0]


def train_naive_bayes(train_data):
    prior_probability = compute_prior_probability(train_data)
    conditional_probability, list_x_name = compute_conditional_probability(
        train_data)

    return prior_probability, conditional_probability, list_x_name


def prediction_play_tennis(x, list_x_name, prior_probability, conditional_probability):
    x1 = get_index_from_value(x[0], list_x_name[0])
    x2 = get_index_from_value(x[1], list_x_name[1])
    x3 = get_index_from_value(x[2], list_x_name[2])
    x4 = get_index_from_value(x[3], list_x_name[3])

    p0 = prior_probability["No"] \
        * conditional_probability[0][0, x1] \
        * conditional_probability[1][0, x2] \
        * conditional_probability[2][0, x3] \
        * conditional_probability[3][0, x4]

    p1 = prior_probability["Yes"] \
        * conditional_probability[0][1, x1] \
        * conditional_probability[1][1, x2] \
        * conditional_probability[2][1, x3] \
        * conditional_probability[3][1, x4]

    if p0 > p1:
        y_pred = "No"
    else:
        y_pred = "Yes"
    return y_pred


if __name__ == "__main__":
    play_tennis = pd.read_csv("./data/play_tennis.csv")
    print(play_tennis)

    train_data = create_train_data(
        play_tennis[["Outlook", "Temperature", "Humidity", "Wind", "PlayTennis"]])
    print(train_data)
    prior_probability = compute_prior_probability(train_data[:, 4])

    # Câu hỏi 14: Kết quả nào sau đây là output từ chương trình trên:
    print("P(play tennis = No)", prior_probability["No"])
    print("P(play tennis = Yes)", prior_probability["Yes"])

    conditional_probability, list_x_name = compute_conditional_probability(
        train_data)
    print('Câu hỏi 15: Hãy cho biết kết quả của đoạn chương trình sau đây:')
    print("x1 = ", list_x_name[0])
    print("x2 = ", list_x_name[1])
    print("x3 = ", list_x_name[2])
    print("x4 = ", list_x_name[3])

    print('Câu hỏi 16: Hãy cho biết kết quả của đoạn chương trình sau đây:')
    outlook = list_x_name[0]
    i1 = get_index_from_value("Overcast", outlook)
    i2 = get_index_from_value("Rain", outlook)
    i3 = get_index_from_value("Sunny", outlook)
    print(i1, i2, i3)

    print('Câu hỏi 17: Hãy cho biết kết quả của đoạn chương trình sau đây:')
    x1 = get_index_from_value("Sunny", list_x_name[0])
    print("P('Outlook'='Sunny'| Play Tennis = 'Yes') = ",
          np.round(conditional_probability[0][1, x1], 2))  # np.round(conditional_probability[0]["Yes"]["Sunny"], 2)

    print('Câu hỏi 18: Hãy cho biết kết quả của đoạn chương trình sau đây:')
    print("P('Outlook'='Sunny'| Play Tennis= 'No') = ",
          np.round(conditional_probability[0][0, x1], 2))

    print('Câu hỏi 19: Hãy cho biết kết quả của đoạn chương trình sau đây:')
    X = ['Sunny', 'Cool', 'High', 'Strong']
    prior_probability, conditional_probability, list_x_name = train_naive_bayes(
        train_data)
    pred = prediction_play_tennis(
        X, list_x_name, prior_probability, conditional_probability)

    if (pred):
        print("Ad should go!")
    else:
        print("Ad should not go!")
