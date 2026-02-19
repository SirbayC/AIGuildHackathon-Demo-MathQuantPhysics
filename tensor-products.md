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

# Tensor products

In the mathematical formalism of quantum mechanics, the state of a
system is a (unit) vector in a Hilbert space, as mentioned in
[](hilbert-spaces).  Likewise, a *composite* of two
quantum systems can be described by the *tensor product* of the
corresponding Hilbert spaces.

## Definition

In this section, $\HH_1$ and $\HH_2$ are two Hilbert spaces.

:::{prf:definition} Tensor product

The *tensor product* of $\HH_1$ and $\HH_2$ is a Hilbert space
$\HH_1\otimes\HH_2$.  This space contains vectors of the form

$$
\ket\alpha\ket\beta = \ket\alpha\otimes\ket\beta
$$

where $\ket\alpha$ is in $\HH_1$ and $\ket\beta$ is in $\HH_2$.  These
vectors are called *pure tensors*.  Importantly, $\HH_1\otimes\HH_2$
also contains linear combinations of such pure tensors (possibly with
infinitely many terms); these are called (non-pure) tensors.

The inner product between two pure tensors $\ket\alpha\ket\beta$ and
$\ket{\alpha'}\ket{\beta'}$ is by definition
$\braket{\alpha|\alpha'}\braket{\beta|\beta'}$.  (Note that the first
inner product is taken in $\HH_1$ and the second in $\HH_2$!)

:::

:::{prf:example}
:label: bell

Take $\HH_1=\HH_2=\CC^2$ and denote the standard basis by
$\ket0,\ket1$.  (This can be viewed as the state space of a single
qubit.)  There are four possibilities to pick one basis vector in
$\HH_1$ and one in $\HH_2$, giving rise to four pure tensors

$$
\ket{00}, \ket{01}, \ket{10}, \ket{11}
$$ (two-qubit-basis)

in $\HH_1\otimes\HH_2$, where $\ket{ij}$ is shorthand for $\ket i\ket
j$.

An example of a non-pure tensor in $\HH_1\otimes\HH_2$ is

$$
\frac{1}{\sqrt2}\bigl(\ket{00}+\ket{11}\bigr).
$$ (bell)

In {ref}`exercise-bell`, you will show that it is indeed impossible to
write this as a pure tensor.

:::

:::{warning}
The tensor product behaves very differently from the ‘normal’ product
(or *direct sum*) of two vector spaces.  For example, if $\HH_1=\CC^m$
and $\HH_2=\CC^n$, then the direct sum of $\HH_1$ and $\HH_2$ has
dimension $m+n$, while the tensor product has dimension $mn$.
:::

:::{note}
In quantum mechanics, a non-pure tensor in $\HH_1\otimes\HH_2$
represents an *entangled state* of a composite quantum system.
In {prf:ref}`bell`, the composite state consists of two qubits.
The non-pure state {eq}`bell` is known as a *Bell state*.
:::

## Orthonormal bases

We can easily write down a basis for a tensor product
$\HH_1\otimes\HH_2$ using bases of $\HH_1$ and $\HH_2$.  It turns out
that the ‘obvious’ definition works well with inner products.

:::{prf:property} Orthonormal basis of a tensor product
If $(\ket{e_i})_i$ is an orthonormal basis of $\HH_1$ and
$(\ket{f_j})_j$ is an orthonormal basis of $\HH_2$, then
$(\ket{e_i}\ket{f_j})_{i,j}$ is an orthonormal basis of
$\HH_1\otimes\HH_2$.
:::

:::{prf:example}
Take $\HH=\CC^2$ with basis $(\ket0,\ket1)$ and equipped with the
standard inner product.  Then the basis {eq}`two-qubit-basis` is an
(orthonormal) basis for $\HH\otimes\HH$.

More generally, an orthonormal basis for the $n$-fold tensor product
$\HH\otimes\cdots\otimes\HH$ consists of all $n$-bit strings.
:::

## Operators on a tensor product

If $A$ is an operator (i.e. a linear map) on $\HH_1$ and $B$ is a
linear map on $\HH_2$, then there is a linear map $A\otimes B$ on
$\HH_1\otimes\HH_2$.  This is defined on pure tensors by

$$
(A\otimes B)(\ket\alpha\ket\beta) = (A\ket\alpha)(B\ket\beta).
$$

However, just like not every tensor is a pure tensor, there are many
operators on $\HH_1\otimes\HH_2$ that cannot be written in the form
$T\otimes U$ (where $T$ and $U$ are operators on $\HH_1$ and $\HH_2$,
respectively).

:::{prf:example}
:label: cnot

In quantum computing, the CNOT gate acts as follows on the standard
basis of a two-qubit system:

$$
\begin{aligned}
\ket{00}&\longmapsto\ket{00}\\
\ket{01}&\longmapsto\ket{01}\\
\ket{10}&\longmapsto\ket{11}\\
\ket{11}&\longmapsto\ket{10}
\end{aligned}
$$
:::

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz
display_quiz("_static/quizzes/tensor_product.json")
```

***

## Exercises

:::{exercise}
:label: exercise-bell

1. Show that the tensor {eq}`bell` in $\CC^2\otimes\CC^2$ cannot be
   written as a pure tensor $\ket\alpha\ket\beta$.

2. More generally, can you find a criterion for when a state

   $$
   a_{00}\ket{00}+a_{01}\ket{01}+a_{10}\ket{10}+a_{11}\ket{11}
   $$

   can be written as a pure tensor?
:::

:::{exercise}
Show that the tensor {eq}`bell` has norm 1.
:::

:::{exercise}
Consider two operators $A$ and $B$ on $\CC^2$ given in matrix form as

$$
A = \begin{pmatrix}a_{1,1}& a_{1,2}\\
a_{2,1}& a_{2,2}\end{pmatrix},\quad
B = \begin{pmatrix}b_{1,1}& b_{1,2}\\
b_{2,1}& b_{2,2}\end{pmatrix}.
$$

Write down the matrix of the operator $A\otimes B$ on the standard
basis {eq}`two-qubit-basis` of $\CC^2\otimes\CC^2$.
:::

:::{exercise}
Write down the matrix of the CNOT operator (see {prf:ref}`cnot`) on
the standard basis {eq}`two-qubit-basis` of $\CC^2\otimes\CC^2$.
:::
