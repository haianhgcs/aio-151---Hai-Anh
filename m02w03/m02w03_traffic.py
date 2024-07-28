import numpy as np
import pandas as pd
import sys
import os
sys.path.append("..")

if __name__ == "__main__":
    traffic = pd.read_csv("./data/traffic.csv")
    print(traffic)

    # Cho sự kiện thử nghiệm:
    # X = (Day=Weekday, Season=Winter, Fog=High, Rain=Heavy)

    print('Câu hỏi 5: Xác suất xảy ra sự kiện "Class"="On Time", sự kiện "Class"="Late", sự kiện "Class"=" Very Late" và sự kiện "Class"="Cancelled" lần lượt là:')
    traffic_ontime = traffic[traffic["Class"] == "On Time"]
    traffic_late = traffic[traffic["Class"] == "Late"]
    traffic_verylate = traffic[traffic["Class"] == "Very Late"]
    traffic_cancelled = traffic[traffic["Class"] == "Cancelled"]
    print(f'P("Class"=="On Time") = {len(traffic_ontime)}/{len(traffic)}, \
            P("Class"=="Late") = {len(traffic_late)}/{len(traffic)}, \
            P("Class"=="Very Late") = {len(traffic_verylate)}/{len(traffic)}, \
            P("Class" == "Cancelled")={len(traffic_cancelled)}/{len(traffic)}')
    p_traffic_ontime = len(traffic_ontime) / len(traffic)
    p_traffic_late = len(traffic_late) / len(traffic)
    p_traffic_verylate = len(traffic_verylate) / len(traffic)
    p_traffic_cancelled = len(traffic_cancelled) / len(traffic)

    # On Time
    traffic_ontime_weekday = traffic_ontime[traffic_ontime["Day"] == "Weekday"]
    traffic_ontime_winter = traffic_ontime[traffic_ontime["Season"] == "Winter"]
    traffic_ontime_high = traffic_ontime[traffic_ontime["Fog"] == "High"]
    traffic_ontime_heavy = traffic_ontime[traffic_ontime["Rain"] == "Heavy"]
    print("Class = 'On Time' & Weekday: ", len(traffic_ontime_weekday))
    print("Class = 'On Time' & Winter: ", len(traffic_ontime_winter))
    print("Class = 'On Time' & High: ", len(traffic_ontime_high))
    print("Class = 'On Time' & Heavy: ", len(traffic_ontime_heavy))

    p_traffic_ontime_weekday = len(
        traffic_ontime_weekday) / len(traffic_ontime)
    p_traffic_ontime_winter = len(
        traffic_ontime_winter) / len(traffic_ontime)
    p_traffic_ontime_high = len(traffic_ontime_high) / len(traffic_ontime)
    p_traffic_ontime_heavy = len(
        traffic_ontime_heavy) / len(traffic_ontime)

    p_traffic_X_ontime = p_traffic_ontime_weekday * p_traffic_ontime_winter * \
        p_traffic_ontime_high * p_traffic_ontime_heavy * p_traffic_ontime

    # Late
    traffic_late_weekday = traffic_late[traffic_late["Day"] == "Weekday"]
    traffic_late_winter = traffic_late[traffic_late["Season"] == "Winter"]
    traffic_late_high = traffic_late[traffic_late["Fog"] == "High"]
    traffic_late_heavy = traffic_late[traffic_late["Rain"] == "Heavy"]
    print("Class = 'Late' & Weekday: ", len(traffic_late_weekday))
    print("Class = 'Late' & Winter: ", len(traffic_late_winter))
    print("Class = 'Late' & High: ", len(traffic_late_high))
    print("Class = 'Late' & Heavy: ", len(traffic_late_heavy))

    p_traffic_late_weekday = len(
        traffic_late_weekday) / len(traffic_late)
    p_traffic_late_winter = len(
        traffic_late_winter) / len(traffic_late)
    p_traffic_late_high = len(traffic_late_high) / len(traffic_late)
    p_traffic_late_heavy = len(
        traffic_late_heavy) / len(traffic_late)

    p_traffic_X_late = p_traffic_late_weekday * p_traffic_late_winter * \
        p_traffic_late_high * p_traffic_late_heavy * p_traffic_late

    # Very Late
    traffic_verylate_weekday = traffic_verylate[traffic_verylate["Day"] == "Weekday"]
    traffic_verylate_winter = traffic_verylate[traffic_verylate["Season"] == "Winter"]
    traffic_verylate_high = traffic_verylate[traffic_verylate["Fog"] == "High"]
    traffic_verylate_heavy = traffic_verylate[traffic_verylate["Rain"] == "Heavy"]
    print("Class = 'Very Late' & Weekday: ", len(traffic_verylate_weekday))
    print("Class = 'Very Late' & Winter: ", len(traffic_verylate_winter))
    print("Class = 'Very Late' & High: ", len(traffic_verylate_high))
    print("Class = 'Very Late' & Heavy: ", len(traffic_verylate_heavy))

    p_traffic_verylate_weekday = len(
        traffic_verylate_weekday) / len(traffic_verylate)
    p_traffic_verylate_winter = len(
        traffic_verylate_winter) / len(traffic_verylate)
    p_traffic_verylate_high = len(
        traffic_verylate_high) / len(traffic_verylate)
    p_traffic_verylate_heavy = len(
        traffic_verylate_heavy) / len(traffic_verylate)

    p_traffic_X_verylate = p_traffic_verylate_weekday * p_traffic_verylate_winter * \
        p_traffic_verylate_high * p_traffic_verylate_heavy * p_traffic_verylate

    # Cancelled
    traffic_cancelled_weekday = traffic_cancelled[traffic_cancelled["Day"] == "Weekday"]
    traffic_cancelled_winter = traffic_cancelled[traffic_cancelled["Season"] == "Winter"]
    traffic_cancelled_high = traffic_cancelled[traffic_cancelled["Fog"] == "High"]
    traffic_cancelled_heavy = traffic_cancelled[traffic_cancelled["Rain"] == "Heavy"]
    print("Class = 'Cancelled' & Weekday: ", len(traffic_cancelled_weekday))
    print("Class = 'Cancelled' & Winter: ", len(traffic_cancelled_winter))
    print("Class = 'Cancelled' & High: ", len(traffic_cancelled_high))
    print("Class = 'Cancelled' & Heavy: ", len(traffic_cancelled_heavy))

    p_traffic_cancelled_weekday = len(
        traffic_cancelled_weekday) / len(traffic_cancelled)
    p_traffic_cancelled_winter = len(
        traffic_cancelled_winter) / len(traffic_cancelled)
    p_traffic_cancelled_high = len(
        traffic_cancelled_high) / len(traffic_cancelled)
    p_traffic_cancelled_heavy = len(
        traffic_cancelled_heavy) / len(traffic_cancelled)

    p_traffic_X_cancelled = p_traffic_cancelled_weekday * p_traffic_cancelled_winter * \
        p_traffic_cancelled_high * p_traffic_cancelled_heavy * p_traffic_cancelled

    p_X = p_traffic_X_ontime + p_traffic_X_late + \
        p_traffic_X_verylate + p_traffic_X_cancelled

    print("Câu hỏi 6: Xác suất xảy ra sự kiện 'Class'='On Time' khi sự kiện X xảy ra là:",
          p_traffic_X_ontime)
    print("Câu hỏi 7: Xác suất xảy ra sự kiện 'Class'='Late' khi sự kiện X xảy ra là:",
          p_traffic_X_late)
    print("Câu hỏi 8: Xác suất xảy ra sự kiện 'Class'='Very Late' khi sự kiện X xảy ra là:",
          p_traffic_X_verylate)
    print("Câu hỏi 9: Xác suất xảy ra sự kiện 'Class'='Cancelled' khi sự kiện X xảy ra là:",
          p_traffic_X_cancelled)

    # Câu hỏi 4: Khi xảy ra sự kiện X, nhãn của "Play Tennis" sẽ là:
    answer = ""
    max_possibility = max([p_traffic_X_ontime, p_traffic_X_late,
                          p_traffic_X_verylate, p_traffic_X_cancelled])
    if p_traffic_X_ontime == max_possibility:
        answer = "On Time"
    elif p_traffic_X_late == max_possibility:
        answer = "Late"
    elif p_traffic_X_verylate == max_possibility:
        answer = "Very Late"
    elif p_traffic_X_cancelled == max_possibility:
        answer = "Cancelled"
    print("Câu hỏi 10: Dự đoán 'Class' của sự kiện X là:", answer)
