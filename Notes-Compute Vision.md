# Brief Introduction
**Computer Vision** là một lĩnh vực khoa học máy tính tập trung vào việc tạo 
ra các hệ thống máy tính có thể hiểu và phân tích hình ảnh và video. Nó có nhiều ứng
dụng trong các lĩnh vực như: Nhận diện đối tượng, xử lý ảnh Y Khoa, Robotic, v.v...


Có rất nhiều thư viện trong Python để chúng ta xử lý dữ liệu ảnh, trong đó OpenCV
là một trong những thư viện điển hình.

# Chuyển đổi không gian màu
OpenCV cung cấp nhiều hàm để chuyển đổi giữa các không gian màu khác nhau.
|  Hàm | Chuyển đổi  | Mô tả  |
|---|---|---|
|  cv2.COLOR_BGR2GRAY | BGR sang ảnh xám  | Chuyển đổi ảnh từ BGR sang ảnh xám.  |
|  cv2.COLOR_BGR2HSV |  BGR sang HSV | Chuyển đổi ảnh từ BGR sang không gian màu HSV (Hue, Saturation, Value).  |
|  cv2.COLOR_BGR2RGB |  BGR sang RGB | Chuyển đổi ảnh từ BGR sang không gian màu RGB (R - Red, G - Green, B - Blue).  |

# Bộ lọc Gauss (Gausian Blur)
* **Bộ lọc Gauss (Gaussian Blur)** là một kỹ thuật xử lý ảnh phổ biến được sử
dụng để làm mịn ảnh và loại bỏ nhiễu. Nó hoạt động bằng cách áp dụng một ma
trận Gauss (Gaussian kernel) lên từng pixel của ảnh.
* **Hàm Gauss** là một hàm phân phối xác suất có dạng hình chuông. Giá trị của
hàm Gauss tại mỗi pixel được xác định bởi độ lệch chuẩn (sigma) của hàm. Sigma
càng lớn, mức độ làm mịn càng cao.Công thức tổng quát của Gaussian Filter như
sau:

$G(x,y) = \displaystyle \frac{1}{2 \pi \delta ^2}\cdot exp\left ( -\frac{x^2 + y^2}{2\delta ^2} \right )$
