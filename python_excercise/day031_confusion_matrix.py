print('98 ảnh mèo (trong 100 ảnh do search engine trả về) được gọi là gì? ', "TP")
print('2 ảnh không phải mèo (trong 100 ảnh do search engine trả về) được gọi là gì? ', "FP")
print('100 ảnh do search engine trả về được gọi là gì? ', "")
print('302 ảnh mèo còn lại (400 ảnh mèo – 98 ảnh mèo) được gọi là gì? ', "FN")
print('598 ảnh không phải mèo còn lại (600 ảnh không phải mèo – 2 ảnh không phải mèo) được gọi là gì? ', "TN")

tp = 98
tn = 598
fn = 302
fp = 2

precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1 = precision * recall / (precision + recall)

print("precision: ", precision)
print("recall: ", recall)
print("f1: ", f1)
