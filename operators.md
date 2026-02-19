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

# Operators on Hilbert spaces

Recommended reference: {cite:t}`griffiths`, in particular Section 3.1.

## Operators

An *operator* or *linear map* on a Hilbert space $\HH$ is a map

$$
T\colon\HH\to\HH
$$

such that

- $T(c\ket\alpha) = c(T\ket\alpha)$
- $T(\ket\alpha+\ket\beta) = T\ket\alpha+T\ket\beta$

:::{note}
It is also possible to define linear maps between different
Hilbert spaces, but we will not go into this.
:::

:::{note}
In physics, operators are often denoted with a hat, so what we call
$T$ would be written as $\hat T$.  One reason for this is to
distinguish a physical quantity (like momentum or energy) from the
corresponding mathematical operator.  Since we do not consider
physical quantities in this module, we do not use the hat notation.
:::

Operators form a vector space: the sum of two operators $T$ and $U$
is defined by the formula

$$
(T+U)\ket\alpha=T\ket\alpha+U\ket\alpha
$$

and multiplication of an operator $T$ by a scalar $c$ is defined by
the formula

$$
(cT)\ket\alpha=c(T\ket\alpha).
$$

Like matrices (but unlike vectors), operators can be *composed*: if
$T$ and $U$ are two operators, then $TU$ is the operator defined by

$$
(TU)\ket\alpha=T(U\ket\alpha).
$$

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz
display_quiz("_static/quizzes/hilbert-spaces-and-operators.json")
```

## Matrix entries

In physics, quantities of the form

$$
\bra\alpha T\ket\beta
$$

are often of special interest.  These are called *matrix entries* of
$T$, especially if $\ket\alpha$ and $\ket\beta$ are basis vectors in
some fixed orthonormal basis of $\HH$.

:::{prf:example}
Consider a linear map $A$ on $\CC^n$, viewed as a matrix.  Taking the
matrix entries as above, where $\alpha$ and $\beta$ range over the
standard basis vectors, we obtain the usual matrix entries of $A$; see
{ref}`matrix-entry`.
:::

:::{note}

A remark on notation: you will often see notation like
$\braket{\alpha|T\beta}$.  This is literally meaningless: the operator
$T$ can be applied to vectors, which we denote by $\ket\beta$, while
the symbol $\beta$ is just a label.  However, in practice it is very
convenient and completely unambiguous to write
$\braket{\alpha|T\beta}$ instead of the strictly speaking more correct
$\bra\alpha(T\ket\beta)$.

Similarly, we will write $\braket{T\alpha|\beta}$ to mean the inner
product of $T\ket\alpha$ with $\ket\beta$.  Extending this notation to
scalars $c$, we can also write

$$
\braket{c\alpha|\beta}=\overline{\braket{\beta|c\alpha}}
=\bar c\overline{\braket{\beta|\alpha}}
=\bar c\braket{\alpha|\beta}.
$$

:::

## The adjoint of an operator

Given an operator $T$ on a Hilbert space $\HH$, there exists an
operator $T^\dagger$ with the property

$$
\braket{T^\dagger\alpha|\beta}=\braket{\alpha|T\beta}
\quad\text{for all }\ket\alpha,\ket\beta\in\HH.
$$

The operator $T^\dagger$ is called the *adjoint* of $T$.

:::{prf:property} Properties of the adjoint

For all operators $T$, $U$ and scalars $c$, we have

1. $(cT)^\dagger = \bar c T^\dagger$

2. $(TU)^\dagger = U^\dagger T^\dagger$

3. $(T^\dagger)^\dagger = T$

:::

:::{prf:example}

Take $\HH=\CC^n$ with the standard inner product.  For a matrix $A$,
we write $A^\dagger$ for the conjugate transpose of $A$.  We extend
this to vectors by viewing column vectors as $n\times 1$-matrices and
row vectors as $1\times n$-matrices.  For all
$\ket\alpha,\ket\beta\in\HH$ we then have

$$
\braket{\alpha|A|\beta}=\ket{\alpha}^\dagger A\ket\beta
=(A^\dagger\ket{\alpha})^\dagger\ket\beta
=\braket{A^\dagger\alpha|\beta}.
$$

This shows that the adjoint of the operator $A$ corresponds to the
conjugate transpose of $A$ viewed as a matrix.

:::

## Hermitian operators

:::{prf:definition} Hermitian operator

An operator $T$ on a Hilbert space $\HH$ is called *Hermitian* if it
is equal to its own adjoint, i.e.

$$
T = T^\dagger.
$$

:::

It is clear from the definition that all real symmetric matrices are
Hermitian.

:::{prf:example}
The matrix

$$
\begin{pmatrix}
3& 2+i& 4i\\
2-i& 1& 1-i\\
-4i& 1+i& 3
\end{pmatrix}
$$

is Hermitian.
:::

The following two results are of fundamental importance in quantum
mechanics.  Together, they explain why in the mathematical formalism
of quantum mechanics, Hermitian operators correspond to physical
observables.

::::{prf:theorem}

The eigenvalues of a Hermitian operator $T$ are real.

:::{prf:proof}
Suppose $\lambda$ is an eigenvalue of $T$ and $\ket\alpha$ is a
corresponding eigenvector.  Then we have

$$
\lambda\braket{\alpha|\alpha}=\braket{\alpha|T\alpha}
=\braket{T\alpha|\alpha}=\braket{\lambda\alpha|\alpha}
=\bar\lambda\braket{\alpha|\alpha}.
$$

Since $\braket{\alpha|\alpha}$ is non-zero, we can divide by it and
obtain $\lambda=\bar\lambda$.
:::

::::

:::{prf:theorem} Spectral theorem

If $T$ is a Hermitian operator on a Hilbert space $\HH$, then there
exists an orthonormal basis of $\HH$ that consists of eigenvectors for
$T$.

:::

## Unitary operators

:::{prf:definition} Unitary operator

An operator $T$ on a Hilbert space $\HH$ is called *unitary* if the
adjoint $T^\dagger$ is a two-sided inverse of $T$, i.e.

$$
TT^\dagger = \id\quad\text{and}\quad T^\dagger T=\id.
$$

:::

Alternatively, $T$ is unitary whenever $T$ preserves inner products;
see {ref}`unitary-inner-product` for a precise statement.

:::{prf:example}
For any angle $\phi$, the matrix

$$
\begin{pmatrix}
\cos\phi& \sin\phi\\
i\sin\phi& -i\cos\phi
\end{pmatrix}
$$

is unitary.
:::

It follows immediately from the definition that the identity operator
on a Hilbert space (sending every vector to itself) is unitary, and if
$T$ is a unitary operator, then its inverse $T^{-1}$ (which equals
$T^\dagger$) is also unitary.  Similarly, if $T$ and $U$ are unitary
operators, then so is the product $TU$.  This means that the
collection of all unitary operators on a Hilbert space $\HH$ has the
mathematical structure of a
[group](https://en.wikipedia.org/wiki/Group_(mathematics)).

## Orthogonal projection

Consider a Hilbert space $\HH$ and a linear subspace (see
{prf:ref}`linear-subspace`).  One can show that every vector
$\ket\alpha\in\HH$ can be decomposed uniquely as

$$
\ket\alpha = \ket{\alpha}_W + \ket{\alpha}_{W^\perp}
\quad\text{with}\quad\ket{\alpha}_W\text{ in }W\quad\text{and}\quad
\ket{\alpha}_{W^\perp}\text{ in }W^\perp.
$$

:::{prf:definition} Orthogonal projection
Given a Hilbert space $\HH$ and a linear subspace $W$ of $\HH$, the
*orthogonal projection* of $\HH$ onto $W$ is the map that sends every
vector $\ket\alpha$ to $\ket\alpha_W$.
:::

Orthogonal projections onto linear subspaces turn out to be important
examples of linear maps.

:::{prf:example}
:label: projection-dim1

Let $W$ be a one-dimensional linear subspace of a Hilbert space $\HH$.
Then for any unit vector $\ket e$ in $W$, the operator $\ketbra{e}{e}$
sending every vector $\ket\psi$ to $\ket e
\braket{e|\psi}=(\braket{e|\psi})\ket e$ is the orthogonal projection
onto $W$.
:::

## Density operators

:::{note}
The topic of this section is usually not treated in BSc-level
mathematics courses.  We include it because density matrices are a
fundamental mathematical concept in quantum physics and are important
examples of Hermitian operators.
:::

*Density operators* on Hilbert spaces, or *density matrices*, play a
central role in situations where quantum states are combined with
*classical* uncertainty.  They describe mixed states (ensembles of
quantum systems) rather than individual (‘pure’) quantum states.
Density operators are intensively used in the theory of entanglement
and in quantum information theory, for example.

:::{prf:definition} Density operator
A *density operator* on a Hilbert space $\HH$ is an operator
$\rho\colon\HH\to\HH$ with the following properties:

1. $\rho$ is Hermitian;
2. $\rho$ is *positive semi-definite*, i.e. for all $\ket\alpha\in\HH$
   we have $\bra\alpha\rho\ket\alpha\ge0$;
3. $\rho$ has trace 1.

A *density matrix* is the matrix of a density operator relative to
some choice of basis of $\HH$.
:::

When $\HH$ is finite-dimensional, the trace of $\rho$ is simply the
trace of the matrix of $\rho$ with respect to any choice of basis for
$\HH$; see {prf:ref}`trace`.  When $\HH$ is infinite-dimensional, the
definition is somewhat more complicated; see [Trace class
(Wikipedia)](https://en.wikipedia.org/wiki/Trace_class)

:::{prf:example}
The matrix

$$
\rho = \frac{1}{5}\begin{pmatrix} 3& 1+2i\\ 1-2i& 2\end{pmatrix}
$$

represents a density operator on the Hilbert space $\CC^2$ with the
standard inner product.
:::

In {numref}`density-dim2`, you will classify all the possible density
matrices in dimension 2.

:::{prf:example}
Let $\ket e$ be a unit vector in $\HH$.  The operator $\ketbra{e}{e}$
sending every vector $\ket\psi$ to $\ket e
\braket{e|\psi}=(\braket{e|\psi})\ket e$ is a density operator.
:::

The operator $\ketbra{e}{e}$ considered above is nothing but the
orthogonal projection operator onto the 1-dimensional linear subspace
$\CC\ket e$ of $\HH$; see {prf:ref}`projection-dim1`.

:::{prf:definition}
A density operator $\rho\colon\HH\to\HH$ is *pure* when $\rho$ is the
orthogonal projection onto a 1-dimensional linear subspace of $\HH$,
and *mixed* otherwise.
:::

On a finite-dimensional Hilbert space, an operator $\rho$ is a density
operator precisely when there exist unit vectors $e_1,\ldots,e_n$ and
real numbers $p_1,\ldots,p_n\ge0$ with $p_1+\cdots+p_n=1$ such that
$\rho$ can be expressed as the *convex combination*

$$
\rho = \sum_{i=1}^n p_i\ketbra{e_i}{e_i}
$$

of the pure density operators $\ketbra{e_i}{e_i}$.  Given a density
operator $\rho$, there are in general multiple ways of expressing
$\rho$ as such a convex combination.  By definition, $\rho$ is pure
precisely when it admits a decomposition as above with $n=1$.
Furthermore, it can be shown that $\rho$ is pure precisely when it
satisfies the identity $\rho^2=\rho$.

## Exponential of an operator

Recall (see [](taylor-exponential)) that the exponential function can
be characterised by the Taylor series

$$
\exp(x) = \sum_{n=0}^\infty\frac{1}{n!}x^n.
$$

In quantum physics, it is frequently useful to apply this formula not
just to (real or complex) numbers, but to operators as well.  One
reason is that there is an important application to differential
equations.

:::{prf:definition} Exponential of an operator
If $T$ is an operator on a Hilbert space $\HH$, then the *exponential*
of $T$ is the operator

$$
\exp(T) = \sum_{n=0}^\infty\frac{1}{n!}T^n.
$$
:::

In the case where $\HH=\CC^n$, an operator $T$ corresponds to an
$n\times n$-matrix $A$.  The same formula as above then defines the
*matrix exponential* $\exp(A)$ of $A$.

:::{warning}
Since operators do not commute in general, the exponential does *not*
have the property $\exp(T+U)=\exp(T)\exp(U)$ as one might expect from
the case of ordinary exponentials.
:::

We have seen in {prf:ref}`diffeq-exp` that the solution of the
differential equation

$$
\dot x(t) = \lambda x(t),\quad x(0)=x_0
$$

is given by

$$
x(t) = x_0 \exp(\lambda t)
$$

Using the operator exponential, we can solve the higher-dimensional
variant

$$
\frac{d}{dt}\ket{x(t)} = T\ket{x(t)},\quad \ket{x(0)}=\ket{x_0}.
$$

Namely, the solution is

$$
\ket{x(t)} = \exp(Tt)\ket{x_0}.
$$

***

## Exercises

:::{exercise}
:label: matrix-entry

Consider a matrix $A=(A_{i,j})_{i,j=1}^n$ and the standard basis
$(\ket{e_i})_{i=1}^n$ of $\CC^n$.  Check that the matrix entry
$\braket{e_i|A|e_j}$ is simply the actual matrix entry $A_{i,j}$.
:::

:::{exercise}
:label: unitary-inner-product

Show that an operator $T$ is unitary precisely when it satisfies
$\braket{T\alpha|T\beta}=\braket{\alpha|\beta}$ for all vectors
$\ket\alpha$, $\ket\beta$.
:::

:::{exercise}
:label: pauli-matrices

Check that the *Pauli matrices*

$$
\sigma_x = \begin{pmatrix}0& 1\\1& 0\end{pmatrix},\quad
\sigma_y = \begin{pmatrix}0& -i\\i& 0\end{pmatrix},\quad
\sigma_z = \begin{pmatrix}1& 0\\0& -1\end{pmatrix}
$$

are both Hermitian and unitary.
:::

:::{exercise}
Verify the description of orthogonal projections onto one-dimensional
linear subspaces given in {prf:ref}`projection-dim1`.
:::

:::{exercise}
Consider the Hilbert space $\HH=\CC^2$ with the standard inner
product.  Show that an operator $p\colon\HH\to\HH$ is the orthogonal
projection onto some one-dimensional linear subspace of $\HH$
precisely when $p$ is given by a matrix of the form

$$
p = \begin{pmatrix} a& b - ci\\ b + ci& d \end{pmatrix}
$$

where $a,b,c,d$ are real numbers satisfying

$$
a+d=1\quad\text{and}\quad b^2+c^2 = ad.
$$
:::

:::{exercise}
:label: density-dim2

1.  Show that the density operators $\rho$ on the Hilbert space
    $\CC^2$ with the standard inner product are precisely the
    operators given by matrices of the form

    $$
    \rho = \begin{pmatrix} a& b - ci\\ b + ci& d \end{pmatrix}
    $$

    where $a,b,c,d$ are real numbers satisfying

    $$
    a+d=1\quad\text{and}\quad b^2+c^2\le ad.
    $$

2.  Deduce that the density operators $\rho$ as above are precisely
    the operators given by matrices of the form

    $$
    \rho=\frac{1}{2}(I_2+r_x\sigma_x+r_y\sigma_y+r_z\sigma_z)
    $$

    where $\sigma_x$, $\sigma_y$, $\sigma_z$ are the Pauli matrices
    (see {numref}`pauli-matrices`) and $r_x$, $r_y$, $r_z$ are real
    numbers satisfying $r_x^2+r_y^2+r_z^2\le1$.

3.  Show that a density operator $\rho$ is pure precisely when the
    numbers $r_x$, $r_y$, $r_z$ in the above expression satisfy
    $r_x^2+r_y^2+r_z^2=1$.

This shows that density operators for a 2-dimensional system can be
visualised as points of the unit ball in $\RR^3$.  The pure states are
those on the unit sphere (the boundary of the unit ball), often called
the *Bloch sphere* in this context; the mixed states are those in the
interior.
:::

:::{exercise}
Suppose $D$ is a *diagonal* $n\times n$-matrix, viewed as an operator
on the space $\CC^n$.  Find an expression for the matrix exponential
$\exp(D)$.
:::

:::{exercise}
Consider a square matrix $D$ and an invertible matrix $P$.  Show that
the matrix exponential of $PDP^{-1}$ satisfies

$$
\exp(PDP^{-1}) = P\exp(D)P^{-1}.
$$

(This formula is especially useful in the case where $D$ is diagonal,
since together with the previous exercise it allows us to efficiently
compute the exponential of a diagonalisable matrix.)
:::
