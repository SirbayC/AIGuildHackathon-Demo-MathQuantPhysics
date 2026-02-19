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

# Hilbert spaces

Recommended reference: {cite:t}`griffiths`, in particular Section 3.1.

So far, we have been considering vectors in an $n$-dimensional real or
complex space.  In quantum mechanics, one encounters
infinite-dimensional vector spaces as well.  In particular, the state
of a quantum system is represented mathematically by a (unit) vector
in a *Hilbert space*.

## Vector spaces

As is customary in quantum physics and quantum algorithms, we use
*bra-ket notation* for vectors in Hilbert spaces.

:::{prf:definition} Vector space

A (real or complex) *vector space* consists of

- a set of vectors, denoted by symbols like $\ket\alpha$
- a distinguished vector $\mathbf{0}$ called the *zero vector*[^zero]
- a way of *adding vectors*, i.e. given two vectors $\ket\alpha$ and
  $\ket\beta$ we can obtain a third vector
  $\ket\alpha+\ket\beta$
- a way of *multiplying a vector by a scalar*: given a scalar $c$ (a
  real or complex number, depending on whether we consider a real or
  complex vector space) and a vector $\ket\alpha$ we can obtain a
  vector $c\ket\alpha$

such that a number of properties hold:

- $0\ket\alpha=\mathbf{0}$
- $1\ket\alpha=\ket\alpha$
- $\mathbf{0}+\ket\alpha=\ket\alpha$
- $\ket\alpha+\ket\beta=\ket\beta+\ket\alpha$
- $(\ket\alpha+\ket\beta)+\ket\gamma=\ket\alpha+(\ket\beta+\ket\gamma)$
- $c(\ket\alpha+\ket\beta)=c\ket\alpha+c\ket\beta$
- $(c+d)\ket\alpha = c\ket\alpha + d\ket\alpha$
- $c(d\ket\alpha)=(cd)\ket\alpha$

:::

[^zero]: We avoid denoting the zero vector by $\ket0$ because this
    symbol is often used for a distinguished unit vector, as in
    {prf:ref}`finite-dimensional`.

:::{prf:definition} Basis, dimension
A *basis* for a vector space is a collection of vectors
$(\ket{e_i})_i$ such that every vector can be written in exactly one
way as a linear combination of the $\ket{e_i}$.  The number of
vectors in a basis is called the *dimension* of the space.
:::

As in [](basis-transformations), any two bases contain the same number
of vectors, so the dimension does not depend on the choice of basis.

:::{prf:example}
:label: finite-dimensional

The simplest examples are the $n$-dimensional vector spaces $\RR^n$
and $\CC^n$ with coordinatewise addition and scalar multiplication.

An important special case is the two-dimensional space $\CC^2$.  In
bra-ket notation, various symbols are used for the standard basis
vectors $\binom{1}{0}$ and $\binom{0}{1}$ in this space, such as

- $\ket+$ and $\ket-$;
- $\ket0$ and $\ket1$ (in the context of quantum computing);
- $\ket\uparrow$ and $\ket\downarrow$ (in the context of spins).
:::

## Hermitian inner products and Hilbert spaces

:::{prf:definition} Hermitian inner product
A *Hermitian inner product* assigns to vectors $\ket\alpha$ and
$\ket\beta$ a complex number $\braket{\alpha|\beta}$ such that the
following properties hold:

- $\braket{\alpha|\beta}=\overline{\braket{\beta|\alpha}}$;
- $\braket{\alpha|\alpha}\ge0$, and $\braket{\alpha|\alpha}=0$ holds
  precisely when $\ket\alpha=\mathbf{0}$ (note that
  $\braket{\alpha|\alpha}$ is a real number because of the first
  property);
- $\bra\alpha(\ket\beta+\ket\gamma) = \braket{\alpha|\beta} +
  \braket{\alpha|\gamma}$;
- $\bra\alpha(c\ket\beta)=c(\braket{\alpha|\beta})$;
:::

:::{prf:definition} Norm of a vector
The *norm* or *length* of a vector $\ket\alpha$ in a Hilbert space
is defined as the real number

$$
\|\alpha\|=\sqrt{\braket{\alpha|\alpha}}.
$$
:::

:::{note}

The properties above imply that for any scalar $c$, the inner product
of $c\ket{\alpha}$ with $\ket\beta$ equals $\bar
c\braket{\alpha|\beta}$.  In other words, while the inner product is
(complex) linear in its second argument, it is only *conjugate linear*
in its first argument.  This is the usual convention in physics.  It
differs from the convention in mathematics, where inner products are
usually linear in the first argument and conjugate linear in the
second argument.

:::

:::{prf:definition} Hilbert space

A *Hilbert space* is a complex vector space $\HH$ equipped with a
Hermitian inner product $\braket{\enspace|\enspace}$ and satisfying a
condition called *completeness*.
:::

We will not make the notion of completeness precise in these notes.
Roughly speaking, it means that we do not have to worry too much about
convergence of sequences or series in our Hilbert space, and there is
a notion of infinite linear combinations.

:::{prf:example}
:label: inner-product-example

We take $\HH=\CC^n$ and define an inner product by

$$
\braket{\alpha|\beta} = \sum_{i=1}^n\bar\alpha_i\beta_i.
$$

Check for yourself that this satisfies all the properties of a
Hermitian inner product.
:::

:::{prf:example}

Consider the space $L^2(\RR)$ of square-integrable functions on the
real line, i.e. functions $f\colon\RR\to\CC$ such that the integral
$\int_{-\infty}^\infty|f(x)|^2 dx$ exists and is finite.  This is a
Hilbert space with inner product

$$
\braket{f|g} = \int_{-\infty}^\infty \bar f(x)g(x)dx.
$$

:::

:::{prf:example}

Consider the space $\ell^2$ of sequences $z=(z_0,z_1,\ldots)$ of
complex numbers such that

$$
\sum_{n=0}^\infty |z_n|^2<\infty.
$$

Then $\ell^2$ is a Hilbert space with inner product

$$
\braket{w|z}=\sum_{n=0}^\infty \bar w_n z_n.
$$

:::

## The dual Hilbert space

With any Hilbert space $\HH$, we can associate a *dual* Hilbert space
$\HH^*$.  In the bra-ket formalism used in quantum mechanics, for
every “ket vector” $\ket\alpha$ in $\HH$ we have a dual “bra vector”
$\bra\alpha$ in $\HH^*$.  This correspondence has the following
properties:

| vector in $\HH$         | corresponding vector in $\HH^*$ |
|-------------------------|---------------------------------|
| ket vector $\ket\alpha$ | bra vector $\bra\alpha$         |
| $\ket\alpha+\ket\beta$  | $\bra\alpha+\bra\beta$          |
| $c\ket\alpha$           | $\bar c\bra\alpha$              |

In mathematical language, $\HH^*$ is the space of continuous linear
maps $\HH\to\CC$.  The bra vector $\bra\alpha$ then represents the
linear map that sends $\ket\beta$ to $\braket{\alpha|\beta}$.

:::{prf:example} The dual of $\CC^n$

In the case $\HH=\CC^n$ we can identify $\HH^*$ with $\CC^n$ as well;
for a vector $\ket\alpha$ in $\CC^n$, the dual vector $\bra\alpha$ is
then simply the same vector.
However, it can also be convenient to distinguish $\HH$ from $\HH^*$
by denoting a ket vector $\ket\alpha$ as a column vector and the
corresponding bra vector $\bra\alpha$ by the conjugate transpose of
$\ket\alpha$, so $\bra\alpha$ is the row vector whose entries are the
complex conjugates of those of $\alpha$.  In $\CC^2$, for example, we
have

$$
\ket\alpha=\begin{pmatrix}1\\ i\end{pmatrix}\Longrightarrow
\bra\alpha=\begin{pmatrix}1& -i\end{pmatrix}.
$$

This allows us to view $\bra\alpha$ as a linear map sending
$\ket\beta$ to the scalar obtained by multiplying the row vector
$\bra\alpha$ by the column vector $\ket\beta$.

:::

:::{note}
If you know about continuous linear maps of Hilbert spaces, here is a
useful connection between the mathematical definition of $\HH^*$ and
the bra-ket formalism: the *Riesz representation theorem* states that
every continuous linear map $\HH\to\CC$ is of the form
$\braket{\alpha|\enspace}$ for some $\alpha$ in $\HH$.
:::

## Orthonormal bases

When working with vector spaces, it is frequently useful to make a
choice of basis adapted to the problem at hand.  In the context of a
Hilbert space, it turns out that a “good” basis is often one that
satisfies the following property with respect to the inner product.

:::{prf:definition} Orthonormal system
An *orthonormal system* of vectors in a Hilbert space $\HH$ is a
collection of vectors $(\ket{e_i})_{i\in I}$, where $I$ is some index
set, satisfying

$$
\braket{e_i|e_j} = \begin{cases}
1&\quad\text{if }i=j,\\
0&\quad\text{if }i\ne j.
\end{cases}
$$
:::

:::{prf:definition} Orthonormal basis
An *orthonormal basis* of a Hilbert space $\HH$ is an orthonormal
system $(\ket{e_i})_{i\in I}$ in $\HH$ that spans $\HH$, i.e. every
vector in $\HH$ can be written as a (possibly infinite) linear
combination of the $\ket{e_i}$.
:::

:::{prf:example}
In the Hilbert space $\CC^n$ with the standard inner product, the
standard basis $(e_1,\ldots,e_n)$ is an orthonormal basis.
:::

:::{prf:example}
:label: fourier-orthonormal

Consider the space $L^2([0,1])$ of square-integrable functions on the
unit interval.  An orthonormal basis for this space consists of the
functions $e_n(x)=\exp(2\pi i n x)$ for all integers $n$.  This
reflects the fact that every “nice” function on $[0,1]$ can be
expressed as a [](fourier-series).
:::

## Linear subspaces

:::{prf:definition} Linear subspace
:label: linear-subspace
A *linear subspace* of a vector space $V$ is a set of vectors $W$
contained in $V$ such that the following properties hold:

1. The zero vector of $V$ lies in $W$.

2. For all vectors $w$ and $w'$ in $W$, the sum $w+w'$ is also in $W$.

3. For every vector $w$ in $W$ and every scalar $\lambda$, the scalar
   multiple $\lambda w$ is also in $W$.
:::

In quantum physics, linear subspaces are important because they encode
quantum states that a physical state can collapse to when a
measurement is performed.  To make this more precise, we need the
notions of *orthogonal complement* of a subspace and (in the next
chapter) of *orthogonal projection* onto a subspace.

:::{prf:definition} Orthogonal complement
Consider a Hilbert space $\HH$ and a linear subspace $W$ of $\HH$.
The *orthogonal complement* of $W$ in $\HH$, denoted by $W^\perp$, is
the set of all vectors $\ket{v}$ in $\HH$ that are orthogonal to all
of $W$, i.e.

$$
W^\perp = \{\ket{v}\in\HH\mid\braket{v|w}=0\quad\text{for all }w\in W\}.
$$
:::

It is not hard to verify that the orthogonal complement of a linear
subspace of $\HH$ is again a linear subspace; see
{ref}`exercise-orthogonal`.

Within a Hilbert space $\HH$, we will only consider linear subspaces
$W$ that satisfy the completeness condition and are therefore
themselves Hilbert spaces.

## Example of a function space: spherical harmonics

In physics, Hilbert spaces often occur as spaces of functions on some
space.  We have already seen the examples of $L^2(\RR)$ and
$L^2([0,1])$, the Hilbert spaces of square-integrable functions on the
real line and the unit interval, respectively.

Another useful example is the Hilbert space of square-integrable
functions on the unit sphere

$$
S^2 = \{(x,y,z)\in\RR^3\mid x^2+y^2+z^2=1\}.
$$

It is useful to work with spherical coordinates $\theta,\phi$ with
$0\le\theta\le\pi$ and $0\le\phi\le 2\pi$ such that

$$
x=\sin\theta\cos\phi,\quad
y=\sin\theta\sin\phi,\quad
z=\cos\theta.
$$

Then the inner product of two functions $f,g:S^2\to\CC$ is defined via
the standard area form $\sin\theta\,d\theta\,d\phi$ as

$$
\langle f,g\rangle_{S^2} = \int_{\phi=0}^{2\pi} \int_{\theta=0}^\pi
\overline{f(\theta,\phi)}g(\theta,\phi)
\sin\theta\,d\theta\,d\phi.
$$

Much like the functions $\exp(2\pi i m x)$ form an orthonormal basis
for $L^2([0,1])$, one can write down a set of functions forming an
orthonormal basis for $L^2(S^2)$.  The standard functions are the
*spherical harmonics*.  These are defined by

$$
Y_\ell^m(\theta,\phi) = N_\ell^m \exp(im\phi) P_\ell^m(\cos\theta),
$$

where $\ell$ and $m$ are integers with $-\ell\le m\le \ell$.  Here
$P_\ell^m$ is an *associated Legendre polynomial* and $N_\ell^m$ is an
appropriate normalisation factor.

The [Spherical Harmonics webpage](https://www.quantum-physics.polytechnique.fr/sphericalHarmonics.php?lang=1)
by Manuel Joffre (École Polytechnique) allows you to make
3-dimensional plots of spherical harmonics.  For more background and
definitions, see also {cite:t}`griffiths` or the
[Wikipedia](https://en.wikipedia.org/wiki/Spherical_harmonics) and
[MathWorld](https://mathworld.wolfram.com/SphericalHarmonic.html)
pages on spherical harmonics.

***

## Exercises

:::{exercise}
Check that the inner product defined in
{prf:ref}`inner-product-example` is indeed a Hermitian inner product
on $\CC^n$.
:::

:::{exercise}
:label: cauchy-schwarz

The *Cauchy–Schwarz inequality* states that for vectors
$\ket\alpha,\ket\beta$ in a Hilbert space we have

$$
\bigl|\braket{\alpha|\beta}\bigr|^2\le
\braket{\alpha|\alpha}\braket{\beta|\beta}.
$$

Show this using the basic properties of the inner product.
:::

:::{exercise}

The *triangle inequality* states that for vectors
$\ket\alpha,\ket\beta$ in a Hilbert space we have

$$
\|\alpha+\beta\|\le\|\alpha\|+\|\beta\|.
$$

Derive the triangle inequality from the Cauchy–Schwarz inequality.
:::

:::{exercise}
Consider a Hilbert space $\HH$ and an orthonormal system of vectors
$(\ket{e_i})_{i\in I}$ of $\HH$.  Show that the system is *linearly
independent*, i.e. the only linear relation

$$
\sum_{i\in I} c_i\ket{e_i}=\mathbf{0}
$$

is the one where all $c_i$ are equal to $0$.
:::

:::{exercise}
:label: exercise-orthogonal

Consider a linear subspace $W$ of a Hilbert space $\HH$.  Show that
the orthogonal complement $W^\perp$ is again a linear subspace.
:::


## Login Success

![ ](https://example.com/success-icon.png)

Click the green button to continue.