"""
Basic Python - If - Else

Can Chi là một hệ thống tính toán giờ, ngày, tháng, năm âm lịch của người trung quốc cổ đại. Can Chi có 10 thiên can và 12 địa chi. 
Tên gọi 10 thiên can: Canh,Tân, Nhâm, Quý, Giáp, Ất, Bính, Đinh, Mậu, Kỷ. 
Tên gọi 12 địa chi: Thân, Dậu, Tuất, Hợi, Tý, Sửu, Dần, Mão, Thìn, Tỵ, Ngọ, Mùi.

Để tính được can chi, chúng ta dựa vào quy tắc sau đây:
– Can: lấy năm sinh chia cho 10 và lấy phần dư. Nếu phần dư bằng 0 tương ứng với Canh, 1 tương ứng với Tân, tiếp tục cho tới 9 tương ứng với Kỷ
– Chi: lấy năm sinh chia cho 12 và lấy phần dư. Nếu phần dư bằng 0 tương ứng với Thân, 1 tương ứng với Dậu, tiếp tục cho tới 11 tương ứng với Mùi
"""


def calculate_can_chi_calendar(year):
    can_dic = {0: "Canh", 1: "Tân", 2: "Nhâm", 3: "Quý", 4: "Giáp",
               5: "Ất", 6: "Bính", 7: "Đinh", 8: "Mậu", 9: "Kỷ"}
    chi_dic = {0: "Thân", 1: "Dậu", 2: "Tuất", 3: "Hợi", 4: "Tý", 5: "Sửu",
               6: "Dần", 7: "Mão", 8: "Thìn", 9: "Tỵ", 10: "Ngọ", 11: "Mùi"}

    return can_dic[year % 10] + " " + chi_dic[year % 12]


print(calculate_can_chi_calendar(2024))
print(calculate_can_chi_calendar(2023))
print(calculate_can_chi_calendar(1997))
