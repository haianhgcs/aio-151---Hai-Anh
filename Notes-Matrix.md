# Giới Thiệu
Ma trận là một công cụ toán học quan trọng trong trí tuệ nhân tạo (AI). Chúng được sử
dụng để biểu diễn và thao tác dữ liệu, cũng như trong các phép tính tuyến tính cần thiết
cho việc học máy (machine learning) và học sâu (deep learning).

# Định Nghĩa Ma Trận
Một ma trận là một mảng chữ nhật của các số, sắp xếp theo hàng và cột. Ma trận A với m
hàng và n cột được ký hiệu là:

$A = \begin{bmatrix}
a_{11} & a_{12} & \cdots  & a_{1n}\\ 
a_{21} & a_{22} & \cdots & a_{2n}\\ 
\vdots & \vdots & \ddots & \vdots \\ 
a_{m1} & a_{m1} & \cdots & a_{mn}
\end{bmatrix}$

# Các Phép Toán Ma Trận Cơ Bản
## Phép Cộng Ma Trận
Hai ma trận A và B có cùng kích thước có thể được cộng lại với nhau bằng cách cộng từng
phần tử tương ứng:

$C = A + B$ với $c_{ij} = a_{ij} + b_{ij}$

## Phép Nhân Ma Trận
Phép nhân hai ma trận A và B chỉ có thể thực hiện được khi số cột của A bằng số hàng của
B. Phần tử cij của ma trận tích C = AB được tính như sau:

$c_{ij} = \displaystyle \sum_{k=1}^{n}a_{ik}b_{kj}$


## Ma Trận Chuyển Vị
Ma trận chuyển vị của ma trận A, ký hiệu là AT, là ma trận được tạo ra bằng cách hoán
đổi hàng và cột của A:

$(A^T)_{ij} = A_{ji}$

## Ma Trận Nghịch Đảo
Ma trận nghịch đảo của ma trận vuông A, ký hiệu là A−1, là ma trận sao cho:

$AA^{-1} = A^{-1}A = I$

với $I$ là ma trận đơn vị. Không phải mọi ma trận vuông đều có ma trận nghịch đảo.

## Định Thức
Định thức là một giá trị vô hướng có thể tính toán từ một ma trận vuông và cung cấp thông
tin quan trọng về ma trận đó. Định thức của ma trận A được ký hiệu là det(A) hoặc |A|.

# Ứng Dụng của Ma Trận trong AI
Ma trận được sử dụng rộng rãi trong AI, đặc biệt là trong các lĩnh vực sau:
## Biểu Diễn Dữ Liệu
Dữ liệu trong AI thường được biểu diễn dưới dạng ma trận. Ví dụ, một hình ảnh có thể
được biểu diễn như một ma trận của các giá trị pixel.
## Mạng Nơ-ron Nhân Tạo
Ma trận được sử dụng để biểu diễn các trọng số và tính toán trong các lớp của mạng nơ-ron
nhân tạo.
## Phân Tích Dữ Liệu
Các phép toán ma trận được sử dụng trong nhiều thuật toán học máy để phân tích và biến
đổi dữ liệu, như PCA (Phân tích thành phần chính).

