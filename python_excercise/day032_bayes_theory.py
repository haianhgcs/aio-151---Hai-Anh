print("Bài Tập Toán về Naive Bayes")
total_product = 100
count_product_a = 60
count_product_b = 40
count_product_a_red_small = 20
count_product_a_red_big = 10
count_product_a_green_small = 15
count_product_a_green_big = 15
count_product_b_red_small = 10
count_product_b_red_big = 5
count_product_b_green_small = 10
count_product_b_green_big = 15

print("1. Tính xác suất tiên nghiệm của mỗi lớp")
p_prior_a = count_product_a / total_product
p_prior_b = count_product_b / total_product
print(f"P(A)={p_prior_a}, P(B)={p_prior_b}")

print("2. Tính xác suất điều kiện của màu sắc và kích thước trong mỗi lớp.")
print("Cho lớp A:")
p_red_small_when_a = count_product_a_red_small / count_product_a
p_red_big_when_a = count_product_a_red_big / count_product_a
p_green_small_when_a = count_product_a_green_small / count_product_a
p_green_big_when_a = count_product_a_green_big / count_product_a
print(f"P(Đỏ và Nhỏ|A) = {p_red_small_when_a}")
print(f"P(Đỏ và Lớn|A) = {p_red_big_when_a}")
print(f"P(Xanh và Nhỏ|A) = {p_green_small_when_a}")
print(f"P(Xanh và Lớn|A) = {p_green_big_when_a}")

print("Cho lớp B:")
p_red_small_when_b = count_product_b_red_small / count_product_b
p_red_big_when_b = count_product_b_red_big / count_product_b
p_green_small_when_b = count_product_b_green_small / count_product_b
p_green_big_when_b = count_product_b_green_big / count_product_b
print(f"P(Đỏ và Nhỏ|B) = {p_red_small_when_b}")
print(f"P(Đỏ và Lớn|B) = {p_red_big_when_b}")
print(f"P(Xanh và Nhỏ|B) = {p_green_small_when_b}")
print(f"P(Xanh và Lớn|B) = {p_green_big_when_b}")

p_a_when_red_small = p_prior_a * p_red_small_when_a  # / \
# (p_prior_a * p_red_small_when_a + p_prior_b * p_red_small_when_b)
p_b_when_red_small = p_prior_b * p_red_small_when_b  # / \
# (p_prior_a * p_red_small_when_a + p_prior_b * p_red_small_when_b)
print(f"P(A|Đỏ và Nhỏ) = {p_a_when_red_small}")
print(f"P(B|Đỏ và Nhỏ) = {p_b_when_red_small}")
if p_a_when_red_small >= p_b_when_red_small:
    print("Với xác suất cao hơn, sản phẩm mới có khả năng thuộc lớp A")
else:
    print("Với xác suất cao hơn, sản phẩm mới có khả năng thuộc lớp B")
