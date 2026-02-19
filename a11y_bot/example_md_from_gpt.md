---
title: "Lesson 3 — Introduction to Linear Regression"
course: "Data Science 101"
author: "Prof. A. Example"
---

# Lesson 3 — Linear Regression (Quick Intro)

Welcome! In this lesson we will learn what linear regression is and how to interpret a fitted line. Please read carefully and then complete the exercises at the end.

## Learning Objectives
- Understand the idea of fitting a line to data
- Interpret slope and intercept
- Recognize common pitfalls (outliers, correlation vs causation)

### Before you start
If anything is unclear, click here: [click here](https://example.com/help).

---

# 1. Why Linear Regression?

Linear regression helps us approximate the relationship between an input variable (e.g., study hours) and an output variable (e.g., exam score). In practice, we assume a simple relationship:

![](images/equation.png)

The equation above is the most important thing in this lesson.

Now consider the following explanation. Linear regression is used widely across fields such as economics, biology, engineering, and social sciences. It provides a simple baseline model and is often a first step in modeling. However, it makes assumptions about linearity and errors, and it can be sensitive to outliers. Additionally, when interpreting coefficients, you must consider the scale of the variables and the context in which the data was collected, because correlation does not imply causation, and a regression line does not automatically mean one variable causes another. This is a subtle point that students often misunderstand, so please read this paragraph twice and make sure you fully understand it before proceeding to the next section of the lesson where we will start using data and computing a fit. 

---

## 2. Example Dataset

We collected the following dataset about study hours and exam scores.

| hours | score |
|------:|------:|
| 1     | 52    |
| 2     | 55    |
| 3     | 60    |
| 4     | 62    |
| 5     | 63    |

We will fit a line and then interpret it.

### 2.1 Visualization

Below is a scatter plot and a fitted line:

![Graph](images/study_hours_vs_score.png)

**Important:** The red line is the regression line and the green dots are the points. You can clearly see the trend because the red line goes up.

---

## 3. Interpreting the Model

The slope means: if study hours increases by 1, score increases by *about* the slope amount (on average).

See the official documentation: [this page](https://example.com/docs).

### 3.1 A diagram of slope and intercept

![image](images/slope_intercept_diagram.png)

---

## 4. Quick Exercise

Answer the following:

1) What does the intercept represent?
2) What does the slope represent?

If you need a hint, look at the figure above and read the paragraph again.

### 4.1 Optional coding exercise

Copy the code below and run it:

```python
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1],[2],[3],[4],[5]])
y = np.array([52,55,60,62,63])

model = LinearRegression().fit(X, y)
print("slope:", model.coef_[0])
print("intercept:", model.intercept_)
```

---

## 5. Extra Notes (Accessibility)

- Students should focus on the red line (good) and green points (bad).
- The “good” results are highlighted in green in the figure.

Also, the professor says: **“As you can see above, it’s obvious.”**

---

## 6. Summary

That’s it. For more, go here: [here](https://example.com/more).

Good luck!

