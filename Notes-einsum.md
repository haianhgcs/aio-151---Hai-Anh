# Khái niệm `einsum` trong Python
`einsum` là một hàm trong thư viện NumPy của Python, viết tắt của "Einstein summation",
giúp chúng ta thực hiện các phép tính trên ma trận một cách ngắn gọn và hiệu quả. `einsum`
cho phép bạn chỉ định các phép toán trên các mảng đa chiều bằng cách sử dụng ký hiệu
Einstein. Ký hiệu này cho phép bạn mô tả các phép tính như tổng, nhân chéo, và nhiều phép
toán phức tạp khác một cách trực quan và ngắn gọn. Cú pháp của `einsum` là:

```python
numpy.einsum(subscripts, *operands, out=None)
```

Trong đó: 
- `subscripts` là một chuỗi mô tả các phép toán. 
- `operands` là các mảng đầu vào mà bạn muốn thực hiện phép tính.

## Subscripts
There are two parts, the left-hand side and the right-hand side separated by an arrow-> :

<left-hand side> -> <right-hand side>

The left-hand side describes the dimensions of the tensors involved. Each letter represents one dimension, and each tensor is separated by a comma. All dimensions have to be written down. If a letter is repeated the dimensions that letter represents will be multiplied over (therefore they have to be the same size if the same letter is used). Thus, a left-hand side expression such as ij,jk implies one tensor with dimensions ij and another with dimensions jk . Since j is repeated, a multiplication over the second axis of the first tensor with the first axis of the second tensor will be performed (i.e. rows of the first matrix with columns of the second matrix):

```python
a = np.random.uniform(size=(50, 20))
b = np.random.uniform(size=(20, 40))

c = np.zeros((a.shape[0], a.shape[1], b.shape[1]))
for i in range(a.shape[0]):
    for k in range(b.shape[1]):
        for j in range(a.shape[1]):
            c[i, j, k] = a[i, j] * b[j, k]

assert np.allclose(c, np.einsum("ij,jk->ijk", a, b))
```

Next, on the right-hand side, the resulting expression is formulated. Here omitted dimensions/letters will be summed over and each letter can only appear at most once. In the example above the largest possible tensor is kept, but by removing indices we can reduce the dimension by summing over it:

```python
# matrix multiplication
assert np.allclose(a @ b, np.einsum("ij,jk->ik", a, b))
# matrix multiplication then summing over first dimension
assert np.allclose((a @ b).sum(axis=0), np.einsum("ij,jk->k", a, b))
# matrix multiplication then summing over entire matrix
assert np.allclose((a @ b).sum(), np.einsum("ij,jk->", a,b))
```