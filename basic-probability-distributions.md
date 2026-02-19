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

# Basic probability distributions

Recommended reference: {cite:t}`wasserman`, in particular Sections 2.3
and 2.4.

In this section we cover some of the most important examples of
probability distributions.

## Discrete probability distributions

### Discrete uniform distribution

The idea of the uniform distribution is that there is a finite
collection of possible outcomes, each of which is equally likely.

The **discrete uniform distribution** on a set $S$ of size $n$ (for
example the set $\{1,2,\ldots,n\}$) assigns probability $1/n$ to each
element of $S$:

$$
P(X = x) = \frac{1}{n}\quad(x\in S).
$$

```{code-cell} ipython3
:tags: [hide-input, remove-output]

from matplotlib import pyplot
from myst_nb import glue

fig, ax = pyplot.subplots()
for x in (1, 2, 3, 4):
	ax.add_line(pyplot.Line2D((x, x), (0, 0.25), linewidth=2))
ax.set_xbound(0, 5)
ax.set_ybound(0, 0.3)
ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')

glue("discrete-uniform", fig)
```

:::{glue:figure} discrete-uniform
Probability mass function of a uniform discrete random variable with
values $1,2,3,4$.
:::

### Bernoulli distribution

The **Bernoulli distribution** models an experiment that can have two
outcomes, for example a (possibly biased) coin flip.  We will denote
the two possible outcomes by $0$ and $1$.  The distribution depends on
a parameter $p\in[0,1]$, which is by definition the probability that
the outcome equals 1.  We have

$$
P(X = 0) = 1-p\quad\text{and}\quad
P(X = 1) = p.
$$

```{code-cell} ipython3
:tags: [hide-input, remove-output]

from matplotlib import pyplot
from myst_nb import glue

fig, ax = pyplot.subplots()
for x, px in ((0, 0.3), (1, 0.7)):
	ax.add_line(pyplot.Line2D((x, x), (0, px), linewidth=2))
ax.set_xbound(-.5, 1.5)
ax.set_ybound(0, 0.8)
ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')

glue("bernoulli", fig)
```

:::{glue:figure} bernoulli
Probability mass function of a Bernoulli random variable with $p=0.7$.
:::

### Binomial distribution

The **binomial distribution** with parameters $n$ and $p$ is defined
by the probability mass function

$$
P(X = k) = \binom{n}{k} p^k(1-p)^{n-k}.
$$

Here $\binom{n}{k}=\frac{n!}{k!(n-k)!}$ is the usual binomial
coefficient.

This can be viewed as a sum of $n$ Bernoulli random variables with
parameter $p$.

```{code-cell} ipython3
:tags: [hide-input, remove-output]

from math import comb
from matplotlib import pyplot
from myst_nb import glue

fig, ax = pyplot.subplots()
n = 10
p = 0.7
for k in range(n + 1):
	pk = comb(n, k) * p**k * (1 - p)**(n - k)
	ax.add_line(pyplot.Line2D((k, k), (0, pk), linewidth=2))
ax.set_xbound(-1, n+1)
ax.set_ybound(0, 0.3)
ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')

glue("binomial", fig)
```

:::{glue:figure} binomial
Probability mass function of a binomial random variable with
parameters $n=10$ and $p=0.7$.
:::

### Poisson distribution

The **Poisson distribution** with rate $\lambda$ is defined by the
probability mass function

$$
P(X = k) = \exp(-\lambda)\frac{\lambda^k}{k!}.
$$

:::{note}
The total probability equals 1 because of the Taylor series expansion
of the exponential function, which tells us that

$$
\sum_{k=0}^\infty\frac{\lambda^k}{k!} = \exp(\lambda);
$$

see [](taylor-exponential).
:::

The Poisson distribution is used to model situations where we have a
series of independent random events that occur with some fixed rate in
a given time interval.

(See also the section on the [exponential
distribution](exponential-distribution) below.)

```{code-cell} ipython3
:tags: [hide-input, remove-output]

from math import exp, factorial
from matplotlib import pyplot
from myst_nb import glue

fig, ax = pyplot.subplots()
L = 2
for k in range(10):
	pk = exp(-L) * L**k / factorial(k)
	ax.add_line(pyplot.Line2D((k, k), (0, pk), linewidth=2))
ax.set_xbound(-1, 11)
ax.set_ybound(0, 0.3)
ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')

glue("poisson", fig)
```

:::{glue:figure} poisson
Probability mass function of a Poisson random variable with
parameter $\lambda=2$.
:::

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz
display_quiz("_static/quizzes/basic-probability-distributions.json")
```

## Continuous probability distributions

### Continuous uniform distribution

This a continuous analogue of the discrete uniform distribution
described above.  In this case, the intuition that “all outcomes are
equally likely” is strictly speaking meaningless, since every outcome
has probability 0.

The **continuous uniform distribution** on a bounded interval $[a,b]$
has constant probability density function $1/(b-a)$ on the interval:

$$
f(x) = \frac{1}{b-a}\quad(a\le x\le b).
$$

```{code-cell} ipython3
:tags: [hide-input, remove-output]

from matplotlib import pyplot
from myst_nb import glue

fig, ax = pyplot.subplots()
ax.plot((-2, -1, -1, 3, 3, 4), (0, 0, 1/4, 1/4, 0, 0))
ax.set_xbound(-2, 4)
ax.set_ybound(0, 0.3)
ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')

glue("continuous-uniform", fig)
```

(continuous-uniform)=
:::{glue:figure} continuous-uniform
Probability density function of a uniform continuous random variable.
:::

### Normal or Gaussian distribution

The **normal** or **Gaussian distribution** with mean $\mu$ and
variance $\sigma^2$ is defined by the probability density function

$$
f(x) = \frac{1}{\sigma\sqrt{2\pi}}
\exp\biggl(-\frac{(x-\mu)^2}{2\sigma^2}\biggr)\quad(x\in\RR).
$$

The normal distribution with mean $0$ and variance $1$ is also called
the **standard normal distribution**.

The normal distribution is one of the most common probability
distributions.  One of the reasons for this is the role that it plays
in the [central limit theorem](clt).

```{code-cell} ipython3
:tags: [hide-input]

import numpy as np
import plotly.graph_objects as go

def compute_gaussian(mu, sigma):
    x = np.linspace(-5, 5, 101)
    y = 1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(x - mu)**2 / (2 * sigma**2))
    return x, y

x, y = compute_gaussian(0, 1)

fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines'))

fig.update_layout(
    xaxis_title="x",
    yaxis_title="f(x)",
    sliders=[{
        'active': 5,
        'currentvalue': {"prefix": "sigma: "},
        'pad': {"t": 50},
        'steps': [
            {
                'label': f'{sigma:.1f}',
                'method': 'update',
                'args': [{'y': [compute_gaussian(0, sigma)[1]]}]
            } for sigma in np.round(np.arange(0.5, 2.1, 0.1), 1)
        ]
    }]
)

glue("gaussian", fig)
```

(gaussian)=
:::{glue:figure} gaussian
Probability density function of a normal (Gaussian) random variable
with mean $0$ and variance $\sigma^2$.
:::

You can also view an interactive graph of a [Gaussian with adjustable
mean and variance (Geogebra, by Gonçalo
Meneses)](https://www.geogebra.org/m/fmrmp3ys).

(exponential-distribution)=
### Exponential distribution

The **exponential distribution** with rate $\lambda>0$ is defined by
the probability density function

$$
f(x) = \lambda\exp(-\lambda x)\quad(x\ge0).
$$

```{code-cell} ipython3
:tags: [hide-input]

import numpy as np
import plotly.graph_objects as go

def compute_exp(lamb):
    x = np.linspace(0, 4, 101)
    y = lamb * np.exp(-lamb * x)
    return x, y

initial_lambda = 1
x, y = compute_exp(initial_lambda)

fig = go.Figure()

fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=f'lambda={initial_lambda}'))

fig.update_layout(
    xaxis_title="x",
    yaxis_title="f(x)",
    sliders=[{
        'active': 9,
        'currentvalue': {"prefix": "Lambda: "},
        'pad': {"t": 50},
        'steps': [
            {
                'label': f'{lamb:.1f}',
                'method': 'update',
                'args': [{'y': [compute_exp(lamb)[1]]}]
            } for lamb in np.round(np.arange(0.1, 5.1, 0.1), 1)
        ]
    }]
)

glue("exponential", fig)
```

(exponential)=
:::{glue:figure} exponential
Probability density function of an exponential random variable.
:::

### Cauchy or Lorentz distribution

We include this example mostly to illustrate that seemingly nice
probability distributions can display “pathological” behaviour.

:::{prf:definition} Cauchy distribution
:label: cauchy-distribution

The **Cauchy** (or **Lorentz**) **distribution** is defined by the
probability density function

$$
f(x) = \frac{1}{\pi(1+x^2)}.
$$
:::

The graph of this function (see {numref}`cauchy` below) looks a bit
like that of a normal distribution, but the ‘tails’ decrease much less
rapidly.

Let us see what happens if we try to calculate the expectation of this
distribution:

$$
\begin{aligned}
E(X) &= \int_{-\infty}^\infty xf(x)dx\\
&=\frac{1}{\pi}\int_{-\infty}^\infty \frac{x}{1+x^2}dx\\
&=\frac{1}{\pi}\cdot\biggl.\frac{1}{2}\log(x^2+1)\biggr|_{x=-\infty}^\infty\\
&=\infty-\infty
\end{aligned}
$$

This shows that the expectation is undefined.  The same holds for the
variance.

```{code-cell} ipython3
:tags: [hide-input, remove-output]

from matplotlib import pyplot
from myst_nb import glue
import numpy as np

x = np.linspace(-4, 4, 101)
fx = 1 / (np.pi * (1 + x**2))

fig, ax = pyplot.subplots()
ax.plot(x, fx)
ax.set_xbound(-4, 4)
ax.set_ybound(0, .4)
ax.set_xlabel('$x$')
ax.set_ylabel('$f(x)$')

glue("cauchy", fig)
```

(cauchy)=
:::{glue:figure} cauchy
Probability density function of a Cauchy (Lorentz) random variable.
:::

***

## Exercises

:::{exercise}
Calculate the expectation and variance of a Bernoulli distribution
with parameter $p$.
:::

:::{exercise}
Check that the total probability of a binomial distribution with
parameters $n$ and $p$ equals 1 (as it should).
:::

:::{exercise}
Calculate the expectation and variance of the continuous uniform
distribution on the interval $[-1,3]$.
:::

:::{exercise}
Check that the total probability of a normal distribution with mean
$\mu$ and variance $\sigma^2$ equals 1 (as it should).

*Hint:* use the Gaussian integral {eq}`gaussian-integral`.
:::

:::{exercise}
Compute the expectation of $X$ and of $X^2$ for a Gaussian random
variable $X$ with mean $\mu$ and variance $\sigma^2$.

*Hint:* use integration by parts.
:::

:::{exercise}
Suppose $X_1$ and $X_2$ are independent continuous random variables, where $X_1$ follows the uniform distribution on $[0,1]$ and $X_2$ follows the uniform distribution on $[0,2]$. Find the probability density function for the random variable $Z = X_1 + X_2$.
:::
