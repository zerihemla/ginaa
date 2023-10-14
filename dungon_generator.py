import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px


# A = np.random.randint(2, size = (5,5))
# print(A)
# plt.figure(1)
# plt.imshow(A, origin='upper')
# # plt.grid(True, which='both')
#
#
# plt.show()


# import plotly.express as px
# import numpy as np
# img = np.arange(15**2).reshape((15, 15))
# A = np.random.randint(2, size = (15,15))
# fig = px.imshow(A, binary_string=True)
# # grid =
# fig.show()

def plotly_plot(image):
    fig = px.imshow(image)
    fig.show()

def numpy_plot(image):
    plt.figure(1)
    plt.imshow(A, origin='upper')
    # plt.grid(True, which='both')
    plt.show()

def generate_dungon(x_size, y_size):
    A = np.zeros((y_size, x_size))

    for i in range(x_size):
        A[i,i] = 4

    return A


if __name__ =="__main__":
    x_size = int(input("Enter X Size: "))
    y_size = int(input("Enter Y Size: "))


    A = generate_dungon(x_size, y_size)

    # plotly_plot(A)
    numpy_plot(A)