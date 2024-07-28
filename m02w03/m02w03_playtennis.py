import numpy as np
import pandas as pd

if __name__ == "__main__":
    play_tennis = pd.read_csv("./data/play_tennis.csv")
    print(play_tennis)

    # Cho sự kiện thử nghiệm:
    # X = (Outlook=Sunny, Temperature=Cool, Humidity=High, Wind=Strong)

    print('Câu hỏi 1: Xác suất xảy ra sự kiện "Play Tennis"="Yes" và sự kiện "Play Tennis"="No" lần lượt là: A')
    play_tennis_yes = play_tennis[play_tennis["PlayTennis"] == "Yes"]
    play_tennis_no = play_tennis[play_tennis["PlayTennis"] == "No"]
    print(
        f'P("PlayTennis"=="Yes") = {len(play_tennis_yes)}/{len(play_tennis)}, P("PlayTennis"=="No") = {len(play_tennis_no)}/{len(play_tennis)}')
    p_play_tennis_yes = len(play_tennis_yes) / len(play_tennis)
    p_play_tennis_no = len(play_tennis_no) / len(play_tennis)

    play_tennis_yes_sunny = play_tennis_yes[play_tennis_yes["Outlook"] == "Sunny"]
    play_tennis_yes_cool = play_tennis_yes[play_tennis_yes["Temperature"] == "Cool"]
    play_tennis_yes_high = play_tennis_yes[play_tennis_yes["Humidity"] == "High"]
    play_tennis_yes_strong = play_tennis_yes[play_tennis_yes["Wind"] == "Strong"]
    print("play tennis = yes & Sunny: ", len(play_tennis_yes_sunny))
    print("play tennis = yes & Cool: ", len(play_tennis_yes_cool))
    print("play tennis = yes & High: ", len(play_tennis_yes_high))
    print("play tennis = yes & Strong: ", len(play_tennis_yes_strong))

    p_play_tennis_yes_sunny = len(play_tennis_yes_sunny) / len(play_tennis_yes)
    p_play_tennis_yes_cool = len(play_tennis_yes_cool) / len(play_tennis_yes)
    p_play_tennis_yes_high = len(play_tennis_yes_high) / len(play_tennis_yes)
    p_play_tennis_yes_strong = len(
        play_tennis_yes_strong) / len(play_tennis_yes)

    p_play_tennis_X_yes = p_play_tennis_yes_sunny * p_play_tennis_yes_cool * \
        p_play_tennis_yes_high * p_play_tennis_yes_strong * p_play_tennis_yes

    play_tennis_no_sunny = play_tennis_no[play_tennis_no["Outlook"] == "Sunny"]
    play_tennis_no_cool = play_tennis_no[play_tennis_no["Temperature"] == "Cool"]
    play_tennis_no_high = play_tennis_no[play_tennis_no["Humidity"] == "High"]
    play_tennis_no_strong = play_tennis_no[play_tennis_no["Wind"] == "Strong"]
    print("play tennis = no & Sunny: ", len(play_tennis_no_sunny))
    print("play tennis = no & Cool: ", len(play_tennis_no_cool))
    print("play tennis = no & High: ", len(play_tennis_no_high))
    print("play tennis = no & Strong: ", len(play_tennis_no_strong))

    p_play_tennis_no_sunny = len(play_tennis_no_sunny) / len(play_tennis_no)
    p_play_tennis_no_cool = len(play_tennis_no_cool) / len(play_tennis_no)
    p_play_tennis_no_high = len(play_tennis_no_high) / len(play_tennis_no)
    p_play_tennis_no_strong = len(play_tennis_no_strong) / len(play_tennis_no)

    p_play_tennis_X_no = p_play_tennis_no_sunny * p_play_tennis_no_cool * \
        p_play_tennis_no_high * p_play_tennis_no_strong * p_play_tennis_no

    p_X = p_play_tennis_X_yes + p_play_tennis_X_no

    print('Câu hỏi 2: Xác suất xảy ra sự kiện "Play Tennis"="Yes" khi sự kiện X xảy ra là: B')
    print("P(Play Tennis = Yes|X) =", p_play_tennis_X_yes)

    print('Câu hỏi 3: Xác suất xảy ra sự kiện "Play Tennis"="No" khi sự kiện X xảy ra là: C')
    print("P(Play Tennis = No|X) =", p_play_tennis_X_no)

    print('Câu hỏi 4: Khi xảy ra sự kiện X, nhãn của "Play Tennis" sẽ là: B')
    answer = "Yes"
    if p_play_tennis_X_yes < p_play_tennis_X_no:
        answer = "No"
    print("Khi xảy ra sự kiện X, nhãn của 'Play Tennis' sẽ là:", answer)
