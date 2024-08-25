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

`<left-hand side> -> <right-hand side>`

The left-hand side describes the dimensions of the tensors involved. Each letter represents one dimension, and each tensor is separated by a comma. 

In *implicit* mode, the chosen subscripts are important since the axes of the output are reordered alphabetically. This means that `np.einsum('ij', a)` doesn’t affect a 2D array, while `np.einsum('ji', a)` takes its transpose. Additionally, `np.einsum('ij,jk', a, b)` returns a matrix multiplication, while, `np.einsum('ij,jh', a, b)` returns the transpose of the multiplication since subscript ‘h’ precedes subscript ‘i’.

In *explicit* mode the output can be directly controlled by specifying output subscript labels. This requires the identifier ‘->’ as well as the list of output subscript labels. This feature increases the flexibility of the function since summing can be disabled or forced when required. The call `np.einsum('i->', a)` is like `np.sum(a)` if a is a 1-D array, and `np.einsum('ii->i', a)` is like `np.diag(a)` if a is a square 2-D array. The difference is that einsum does not allow broadcasting by default. Additionally `np.einsum('ij,jh->ih', a, b)` directly specifies the order of the output subscript labels and therefore returns matrix multiplication, unlike the example above in implicit mode.

All dimensions have to be written down. If a letter is repeated the dimensions that letter represents will be multiplied over (therefore they have to be the same size if the same letter is used). Thus, a left-hand side expression such as `ij,jk` implies one tensor with dimensions `ij` and another with dimensions `jk` . Since `j` is repeated, a multiplication over the second axis of the first tensor with the first axis of the second tensor will be performed (i.e. rows of the first matrix with columns of the second matrix):

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

The special case is if you have a tensor with dimensions of the same size and specify the same letter multiple times for that tensor on the left-hand side. Then you get the diagonal of the right-hand side by specifying one letter or the sum of the diagonal (trace) if left empty:

```python
a = np.random.uniform(size=(10, 10))

# return the matrix
assert np.allclose(np.einsum("ij->ij", a), a)
# sum over one axis or both
assert np.allclose(np.einsum("ij->i", a), a.sum(axis=1))
assert np.allclose(np.einsum("ij->j", a), a.sum(axis=0))
assert np.allclose(np.einsum("ij->", a), a.sum())

# specify that it is a square matrix
# np.einsum("ii->ii", a) will lead to error because of repeated subscripts
# diagonal
assert np.allclose(np.einsum("ii->i", a), np.diagonal(a))
# trace
assert np.allclose(np.einsum("ii->", a), np.trace(a))

a = np.random.uniform(size=(10, 10))
b = np.random.uniform(size=(10, 10))
# ii,ii is diagonal * diagonal (element wise multiplication)
assert np.allclose(np.einsum("ii,ii->i", a, b), np.diagonal(a) * np.diagonal(b))
assert np.allclose(np.einsum("ii,ii->", a, b), (np.diagonal(a) * np.diagonal(b)).sum())
```

You can also control the final order of the dimensions:
```python
a = np.random.uniform(size=(10, 10))
b = np.random.uniform(size=(10, 20))

# tranpose
assert np.allclose(b.T, np.einsum("ab->ba", b))
# matrix multiplication then tranpose
assert np.allclose((a @ b).T, np.einsum("ij,jk->ki", a, b))
# swapping around the dimensions
a = np.random.uniform(size=(5, 10, 7, 8, 9))
assert np.allclose(np.transpose(a, (2, 1, 3, 0, 4)), np.einsum("abcde->cbdae", a))
```

