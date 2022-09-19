import numpy as num
import matplotlib.pyplot as plt

N = int(input('Введите чётное N (размерность матрицы), большее 3: '))
A = num.eye(N)

K = int(input('Введите K: '))

if N < 4 or (N % 2 != 0):
    raise ValueError('N должна быть больше 3 и кратной двум!')
    exit()

A = num.random.randint(-10, 10, (N, N))

print(f'A = \n{A}\n')

B = A[:int(N/2), :int(N/2)]
print(f'B = \n{B}\n')
C = A[:int(N/2), int(N/2):]
print(f'C = \n{C}\n')
D = A[int(N/2):, :int(N/2)]
print(f'D = \n{D}\n')
E = A[int(N/2):, int(N/2):]
print(f'E = \n{E}\n')

F = A.copy()

counter = num.sum(C[:, ::2] > K)
production = 1

for i in C[::2, :]:
    for j in i:
        production *= j

print(f'Количество элементов, больших К, в нечетных столбцах С: {counter}')
print(f'Произведение элементов нечетных строк матрицы С: {production}')

print(F)

if counter > production:
    print("Количество элементов, больших К, в нечетных столбцах С больше, чем "
          "произведение элементов нечетных строк матрицы С => меняем С и В симметрично")
    B1 = num.flip(B, axis=1)
    C1 = num.flip(C, axis=1)
    F = num.vstack([num.hstack([C1, B1]), num.hstack([D, E])])
    print(F)

else:
    print("Количество элементов, больших К, в нечетных столбцах С меньше, чем\n"
          "произведение элементов нечетных строк матрицы С=> меняем С и Е несимметрично")
    F = num.hstack([num.vstack([B, D]), num.vstack([E, C])])
    print(F)

detA = num.linalg.det(A)
print(f'Определитель матрицы А: {detA}')
diagonalsF = sum(num.diagonal(F)) + sum(num.diagonal(num.flip(F, axis=1)))
print(f'Сумма диагоналей матрицы F: {diagonalsF}')

expression = []
if detA > diagonalsF:
    print("Определитель А больше суммы диагоналей F:")
    expression = A * num.transpose(A) - K * num.linalg.inv(F)
else:
    print("\nОпределитель А меньше суммы диагоналей F:")
    G = num.tril(A)
    expression = (num.linalg.inv(A) + G - num.transpose(F)) * K

print("\nРезультат выражения:")
print(expression)

plt.subplot(2, 2, 1)
plt.imshow(F[:int(N/2), :int(N/2)], cmap='rainbow', interpolation='bilinear')
plt.subplot(2, 2, 2)
plt.imshow(F[:int(N/2), int(N/2):], cmap='rainbow', interpolation='bilinear')
plt.subplot(2, 2, 3)
plt.imshow(F[int(N/2):, :int(N/2)], cmap='rainbow', interpolation='bilinear')
plt.subplot(2, 2, 4)
plt.imshow(F[int(N/2):, int(N/2):], cmap='rainbow', interpolation='bilinear')
plt.show()

plt.subplot(2, 2, 1)
plt.plot(F[:int(N/2), :int(N/2)])
plt.subplot(2, 2, 2)
plt.plot(F[:int(N/2), int(N/2):])
plt.subplot(2, 2, 3)
plt.plot(F[int(N/2):, :int(N/2)])
plt.subplot(2, 2, 4)
plt.plot(F[int(N/2):, int(N/2):])
plt.show()