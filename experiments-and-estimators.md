---
jupytext:
    formats: md:myst
    text_representation:
        extension: .md
        format_name: myst
kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Experiments and estimators

Recommended reference: {cite:t}`wasserman`, Sections 6.1 and 7.2 (in
particular Examples 7.10 and 7.11).

In this section we give a very brief introduction to the concept of
*statistical inference*, in which we try to infer properties of an
unknown distribution from samples of the distribution.

The setting that we are thinking of is that of an experiment that
gives us a collection of data points, or a process that we observe
during a certain amount of time.  We view our observations as random
variables $X_1,\ldots,X_n$.  We want to make a “best guess” for the
value of some unknown quantity behind our experiment.  For example,
suppose we have an object radiating heat and we take a picture with an
infrared camera.  Then we can try to estimate the temperature of the
object from the values of the pixels in the image.

The concept of an *estimator* formalises how we estimate an unknown
quantity $\theta$ from the observed values of $X_1,\ldots,X_n$.  An
estimator for $\theta$, denoted by $\hat\theta$, is just a function of
the observations $X_1,\ldots,X_n$.  Of course, we are interested in
estimators that tell us as much about the value of $\theta$ as
possible.

Suppose $X_1,\ldots,X_n$ are independent samples from an unknown
distribution.  We already defined the *sample mean* in
{prf:ref}`def-sample-mean`, but we will denote it in this context by
$\hat\mu$.  Thus

$$
\hat\mu = \frac{1}{n}\sum_{i=1}^n X_i.
$$ (eq-muhat)

:::{prf:definition} Sample variance
The *sample variance* of $X_1,\ldots,X_n$ is

$$
\hat\sigma^2 = \frac{1}{n-1}\sum_{i=1}^n(X_i-\hat\mu)^2,
$$

with $\hat\mu$ as in {eq}`eq-muhat`.
:::

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz
display_quiz("_static/quizzes/estimators.json")
```

:::{note}
The sample variance can also be defined with a factor $\frac{1}{n}$
instead of $\frac{1}{n-1}$.  The reason for the factor $\frac{1}{n-1}$
is that we have already used the same data to estimate $\mu$.  If we
knew the exact value $\mu$ beforehand and used it instead of $\hat\mu$
to define the sample variance, the factor $\frac{1}{n}$ would be the
correct one.
:::

***

## Exercises

:::{exercise}
Suppose $X_1, X_2, \ldots, X_6$ are independent samples from a Poisson
distribution with unknown parameter $\lambda$.  Suppose we measure
these and obtain the values 0, 1, 4, 3, 0, 3.  Compute the sample mean
$\hat\mu$ and the sample variance $\hat\sigma^2$ of the distribution.
Can you guess the value of $\lambda$?
:::
