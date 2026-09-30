import matplotlib.pyplot as plt

approaches = ["Centralized", "Distributed"]

scores = [7,9]

plt.title("Decision-Making Approach Comparison")
plt.bar(approaches, scores, color=["orange", "green"], width=0.3)
plt.xlabel("Decision-Making Method")
plt.ylabel("Evaluation Score")

for i, value in enumerate(scores):
    plt.text(i, value + 0.1, str(value), ha="center")

plt.show()