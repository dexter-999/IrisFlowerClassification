import matplotlib.pyplot as plt
import time

x = [10, 20, 30, 40, 50]
y = [25, 45, 65, 70, 95]
a = 0
b = 0
alpha = 0.0005
N = len(y)

losses = []
plt.ion()
fig, ax = plt.subplots()

for i in range(10000):
    y_hat = [a * i + b for i in x]
    # Mean squared error loss
    loss_func = sum((y[j] - y_hat[j]) ** 2 for j in range(N)) / N

    losses.append(loss_func)

    # Gradients
    derivative_a = (-2 / N) * sum(x[j] * (y[j] - y_hat[j]) for j in range(N))
    derivative_b = (-2 / N) * sum((y[j] - y_hat[j]) for j in range(N))

    # Update parameters
    a -= alpha * derivative_a
    b -= alpha * derivative_b
















    # Visualization every 1000 iterations
    if i % 1000 == 0:
        time.sleep(3)
        ax.clear()
        ax.scatter(x, y, color='blue', label='Data')
        y_pred_line = [a * x_i + b for x_i in x]
        ax.plot(x, y_pred_line, color='red', label=f'Iteration {i}')
        ax.set_title(f'Iteration {i}\nLoss: {loss_func:.2f}')
        ax.legend()
        plt.pause(0.1)

plt.ioff()
plt.show()

# Plot loss curve
plt.figure()
plt.plot(losses)
plt.xlabel('Iteration')
plt.ylabel('Loss')
plt.title('Loss Curve')
plt.show()