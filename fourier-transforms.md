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

# Fourier transforms

Like Fourier series, the *Fourier transform* of a function $f$ is a
way to decompose $f$ into complex exponentials.  This is a very useful
tool in quantum mechanics and signal processing, for example.

The difference between [](fourier-series) and Fourier transforms is
that while Fourier series are defined for functions on a bounded
interval (or equivalently for *periodic* functions), the Fourier
transform can be applied to functions on the whole real line.  As a
consequence, all complex exponentials

$$
e_t(x)=\exp(itx)
$$

for arbitrary real numbers $t$ are needed to decompose arbitrary
functions $f$ as above.

Click on the green button to navigate

## Definition and basic properties

:::{prf:definition} Fourier transform
:label: def-ft

Let $f$ be a (real or complex) function on the real line $\mathbb{R}$.
The *Fourier transform* of $f$ is the function

$$
\hat f(y) = \int_{-\infty}^\infty f(x)\exp(-2\pi i x y)dx.
$$ (fourier-transform)
:::

:::{warning}
Various other conventions exist for the definition of the Fourier
transform, so be careful when combining different sources.
:::

The most important property is that using the Fourier transform $\hat
f$, we can express the original function $f$ using a very similar
formula.

:::{prf:theorem} Fourier inversion formula
Let $f$ be a (real or complex) function on the real line $\mathbb{R}$.
Then we can recover $f$ from its Fourier transform $\hat f$ via the
formula

$$
f(x) = \int_{-\infty}^\infty \hat f(y)\exp(2\pi i x y)dy.
$$
:::

This means that $\hat f$ describes the ‘coefficients’ that occur when
expressing $f$ as a ‘linear combination’ of exponential functions,
except the expression involves an integral rather than a sum.

:::{prf:property} Properties of the Fourier transform
:label: ft-properties

Here are several other properties of the Fourier transform, for a
given function $f$ with Fourier transform $\hat f$:

1. For any real number $a$, the Fourier transform of $f(x-a)$ equals
   $\exp(-2\pi i ay)\hat f(y)$.

2. For any real number $a\ne0$, the Fourier transform of $f(ax)$
   equals $|a|^{-1}\hat f(y/a)$.

3. The Fourier transform of $\frac{df}{dx}$ is $2\pi iy\hat f(y)$.

4. The Fourier transform of $xf(x)$ is $\frac{1}{2\pi i y}$ times the
   Fourier transform of $\frac{df}{dx}$.

5. (Plancherel's theorem) We have

   $$
   \int_{-\infty}^\infty|f(x)|^2 dx=
   \int_{-\infty}^\infty|\hat f(y)|^2 dy.
   $$
:::

The first four of these properties are fairly direct consequences of
the definition of the Fourier transform.  The last property is more
difficult to show; see {ref}`ex-fourier-inversion`.

## Examples

### The Fourier transform of a rectangular function

Consider the rectangular (or “square pulse”) function

$$
f(x) = \begin{cases}
1& \text{if }-1/2\le x\le 1/2,\\
0& \text{otherwise}
\end{cases}
$$(eq-rectangular)

(see {numref}`rectangular` below).  We compute

$$
\begin{aligned}
\hat f(y) &= \int_{-1}^1 \exp(-2\pi i x y)dx\\
&= \left[-\frac{1}{2\pi i y}\exp(-2\pi i x y)\right]_{x=-1/2}^{1/2}\\
&= -\frac{1}{2\pi i y}(\exp(-\pi i y)-\exp(\pi i y)).
\end{aligned}
$$

Using the formula

$$
\sin t = \frac{e^{it}-e^{-it}}{2i}
$$

we obtain

$$
\hat f(y) = \sinc y,
$$

where the $\sinc$ function is defined by

$$
\sinc(t) = \frac{\sin(\pi t)}{\pi t}.
$$

```{code-cell} ipython3
:tags: [hide-input, remove-output]

from matplotlib import pyplot as plot
from myst_nb import glue
import numpy as np

fig, ax = plot.subplots(2, 1, figsize=(8,8))

ax[0].plot((-1, -.5, -.5, .5, .5, 1), (0, 0, 1, 1, 0, 0), color='red')
ax[0].set_xlabel('$x$')
ax[0].set_ylabel('$f(x)$')

y = np.linspace(-4, 4, 101)
fhat = np.sinc(y)
ax[1].plot(y, fhat, color='blue')
ax[1].set_xlabel('$y$')
ax[1].set_ylabel('$\\hat f(y)$')

glue("rectangular", fig)
```

(rectangular)=
```{glue:figure} rectangular
A rectangular function and its Fourier transform
```

### The Fourier transform of a Gaussian function

For a fixed $a>0$, consider the function

$$
f(x) = \exp(-\pi ax^2)
$$

(see {numref}`gaussian-ft` below).  We compute

$$
\begin{aligned}
\hat f(y) &= \int_{-\infty}^\infty \exp(-\pi a x^2-2\pi i x y)dx\\
&= \int_{-\infty}^\infty \exp(-\pi a(x+iy/a)^2 - \pi y^2/a)dx\\
&= \int_{-\infty}^\infty \exp(-\pi a(x+iy/a)^2)dx\cdot \exp(- \pi y^2/a).
\end{aligned}
$$

To finish the computation, we need the *contour integration* technique
from complex analysis.  The integral in the above expression can be
interpreted as the integral of the function $\exp(-\pi z^2)$ over the
line $\Im z=y/a$.  Shifting the line of integration to $\Im z=0$ (the
real axis), we get

$$
\hat f(y) = \int_{-\infty}^\infty \exp(-\pi ax^2)dx\cdot \exp(- \pi y^2/a).
$$

Finally, we make use of the *Gaussian integral*

$$
\int_{-\infty}^\infty \exp(-\pi ax^2)dx = a^{-1/2}
$$ (gaussian-integral)

(if you don't know this, look it up in your favourite reference for
integrals) to conclude

$$
\hat f(y) = a^{-1/2} \exp(-\pi y^2/a).
$$

```{code-cell} ipython3
:tags: [hide-input]
from myst_nb import glue
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from _modules.wave_utils import compute_gaussian, compute_fourier_transform, create_slider_steps

# Initial parameter
a_init = 0.5

x, f = compute_gaussian(a_init)
y, fhat = compute_fourier_transform(None, a=a_init)

# Set up plot with subplots
fig = make_subplots(
    rows=2, cols=1,
    subplot_titles=[
        f'Gaussian function with a = {a_init:.2f}',
        f'Fourier transform with a = {a_init:.2f}'
    ]
)

# Add initial Gaussian and Fourier transform traces
fig.add_trace(go.Scatter(x=x, y=f, mode='lines', line=dict(color='red'), name='Gaussian'), row=1, col=1)
fig.add_trace(go.Scatter(x=y, y=fhat, mode='lines', line=dict(color='blue'), name='Fourier transform'), row=2, col=1)

# Update axes labels
fig.update_xaxes(title_text="x", row=1, col=1)
fig.update_yaxes(title_text="f(x)", row=1, col=1)
fig.update_xaxes(title_text="y", row=2, col=1)
fig.update_yaxes(title_text='f(y)', row=2, col=1)

# Generate data for slider steps
a_values = np.arange(0.1, 4.1, 0.1)
gaussians = [compute_gaussian(a) for a in a_values]
fourier_transforms = [compute_fourier_transform(None, a=a) for a in a_values]

slider_steps = create_slider_steps(a_values, gaussians, fourier_transforms, "Gaussian function", "Fourier transform")

# Add slider to the layout
sliders = [dict(active=4, currentvalue={"prefix": "a: "}, pad={"t": 50}, steps=slider_steps)]
fig.update_layout(sliders=sliders, height=600, width=800, showlegend=False)

glue("gaussian", fig)
```

(gaussian-ft)=
```{glue:figure} gaussian
The Gaussian function $f_{1/2}(x)$ and its Fourier transform
$\widehat{f_{1/2}}(y)=\sqrt{2}f_2(y)$
```

<!-- TODO: replace by an example involving Fourier transforms on the real line
```{code-cell} ipython3
:tags: [remove-input]
from myst_nb import glue
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from _modules.wave_utils import compute_fourier_transform, generate_waveforms

t = np.linspace(-1, 1, 1000, endpoint=False)

# Generate waveforms and their Fourier transforms
waveforms = generate_waveforms(t)
fourier_transforms = {name: compute_fourier_transform(wave, t=t) for name, wave in waveforms.items()}

fig = make_subplots(
    rows=1, cols=2,
    subplot_titles=("Waveform", "Fourier transform"),
    column_widths=[0.5, 0.5]
)

def add_traces(fig, waveforms, fourier_transforms, t):
    """Adds waveform and Fourier transform traces to the figure."""
    for i, (name, wave) in enumerate(waveforms.items()):
        freqs, fft_mag = fourier_transforms[name]
        
        # Add waveform and FFT traces
        fig.add_trace(
            go.Scatter(x=t, y=wave, mode="lines", name=f"{name} Wave",
                       visible=(i == 0)), row=1, col=1)
        fig.add_trace(
            go.Scatter(x=freqs, y=fft_mag, mode="lines", name=f"{name} FFT",
                       visible=(i == 0)), row=1, col=2)

add_traces(fig, waveforms, fourier_transforms, t)

def create_dropdown(waveforms):
    """Creates dropdown menu buttons for toggling waveforms."""
    num_traces = 2 * len(waveforms)  # Each waveform has 2 traces (wave + FFT)
    return [
        {
            "buttons": [
                {
                    "label": name,
                    "method": "update",
                    "args": [
                        {"visible": [True if j == i * 2 or j == i * 2 + 1 else False for j in range(num_traces)]},
                        {"title": f"{name} wave and its Fourier transform"}
                    ],
                }
                for i, name in enumerate(waveforms.keys())
            ],
            "direction": "down",
            "showactive": True,
            "x": 0.5,
            "y": 1.2,
            "xanchor": "center",
            "yanchor": "top",
        }
    ]

# Add dropdown menu to the layout
fig.update_layout(updatemenus=create_dropdown(waveforms))

fig.update_layout(
    title="Waveforms and Fourier transforms",
    xaxis_title="Time (s)",
    yaxis_title="Amplitude",
    xaxis2_title="Frequency (Hz)",
    yaxis2_title="Magnitude",
    showlegend=False,
    template="plotly"
)

glue("waveforms", fig)
```

```{glue:figure} waveforms
Various waveforms and their Fourier transforms
```
-->

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz
display_quiz("_static/quizzes/fourier_transf.json")
```

## Fourier transforms and convolutions

The *convolution* of two functions is an operation that has
applications in many areas, such as physics, engineering and
probability.  We briefly introduce it here because of an interesting
and useful relation between convolutions and the Fourier transform:
the Fourier transform converts convolution into (pointwise)
multiplication.  This is made precise by {prf:ref}`thm-ft-conv` below.

:::{prf:definition} Convolution
Let $f$ and $g$ be (real or complex) functions on the real line
$\mathbb{R}$.  The *convolution* of $f$ and $g$ is the function
$f * g$ defined by

$$
(f * g)(y) = \int_{-\infty}^\infty f(x)g(y - x)dx.
$$(convolution)
:::

:::{prf:theorem} Fourier transform and convolution
:label: thm-ft-conv

Let $f$ and $g$ be (real or complex) functions on the real line
$\mathbb{R}$.  Then the Fourier transform of the convolution of $f$
and $g$ equals the (pointwise) product of the Fourier transforms:

$$
\widehat{f * g}(z) = \hat f(z) \hat g(z).
$$
:::

:::{prf:proof}

We compute the Fourier transform of $f * g$ by interchanging the order
of integration and using part 1 of {prf:ref}`ft-properties` for the
function $g(y-x)$:

$$
\begin{aligned}
\widehat{f * g}(z) &= \int_{-\infty}^\infty
\int_{-\infty}^\infty f(x)g(y - x)dx\,
\exp(-2\pi i yz)dy\\
&= \int_{-\infty}^\infty f(x)
\left(\int_{-\infty}^\infty g(y - x)\exp(-2\pi i yz)dy\right)dx\\
&= \int_{-\infty}^\infty f(x)\left(\exp(-2\pi i xz)\hat g(z)\right)dx\\
&= \hat f(z)\hat g(z).
\end{aligned}
$$
:::

Symmetrically, the Fourier transform converts a pointwise product into
a convolution; see {ref}`ex-ft-conv`.

***

## Exercises

:::{exercise}
For a fixed $a>0$, compute the Fourier transform of the function

$$
f(x) = \exp(-a|x|).
$$
:::

:::{exercise}
:label: ex-fourier-inversion

Do Problem 2.20 in {cite:t}`griffiths`, which gives a step-by-step
derivation of the Fourier inversion formula (called Plancherel's
theorem in {cite}`griffiths`).
:::

:::{exercise}
Consider the rectangular function $f$ defined by {eq}`eq-rectangular`.
Show that the convolution of $f$ with itself equals the ‘triangular’
function $\Lambda$ (sketch the graph!) given by

$$
\Lambda(x) = \begin{cases}
1+x& \text{if }-1\le x\le 0\\
1-x& \text{if }0\le x\le 1\\
0& \text{if }|x|\ge 1.
\end{cases}
$$(eq-triangular)
:::

:::{exercise}
Use the previous exercise and {prf:ref}`thm-ft-conv` to compute the
Fourier transform of the triangular function $\Lambda$ defined by
{eq}`eq-triangular`.
:::

:::{exercise}
:label: ex-ft-conv

Show that if $f$ and $g$ are two functions on the real line, then the
following analogue of {prf:ref}`thm-ft-conv` holds:

$$
(\hat f * \hat g)(z) = \widehat{fg}(z).
$$

*Hint:* use the Fourier inversion formula.
:::
