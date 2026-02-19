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

# Matrix operations

## Matrices as linear maps

Very often, an $m\times n$-matrix $A$ with real entries represents a
*linear map* from the space $\RR^n$ of vectors of length $n$ to the
space $\RR^m$ of vectors of length $m$.  Similarly, a matrix with
complex entries represents a linear map from $\CC^n$ to $\CC^m$.  This
map is defined by the matrix-vector product.

:::{prf:definition}
Given a real (resp. complex) $m\times n$-matrix $A$, the *linear map*
associated with $A$ is the map that sends each vector $\vv\in\RR^n$ to
the vector $A\vv\in\RR^m$ (resp. each vector $\vv\in\CC^n$ to the
vector $A\vv\in\CC^m$).
:::

:::{note}
Matrix multiplication is defined so that the product $AB$ represents
the linear map gotten by first applying $B$ and then $A$.  In other
words, we have

$$
(AB)\vv = A(B\vv)
$$(matrix-mult-linear-map)

Note that on the left we have one matrix multiplication and one
matrix-vector multiplication, while on the right we just have two
matrix-vector multiplications.
:::

In quantum physics, matrices are very often square and have
some additional properties that make them suitable as operators on a
physical system or observables of such a system.  We will come back to
this in the section on [](operators).

Many of the definitions below are specifically for square matrices.  A
first example is that of commutators, which play an extremely
important role in quantum physics.

:::{prf:definition} Commutator
Given two $n\times n$-matrices $A$ and $B$, the *commutator* of $A$
and $B$ is the $n\times n$-matrix

$$
[A,B]=AB-BA.
$$
:::

## Transpose and adjoint

:::{prf:definition} Transpose
The *transpose* of an $m\times n$-matrix $A$ is the $n\times
m$-matrix $A^\top$ defined by

$$
(A^\top)_{i,j}=A_{j,i}.
$$
:::

:::{prf:definition} Adjoint
The *adjoint* of an $m\times n$-matrix $A$ is the $n\times m$-matrix
$A^\dagger$ obtained by applying the complex conjugate and the
transpose operation:

$$
(A^\dagger)_{i,j}=\overline{A_{j,i}}.
$$
:::

The *adjoint* of $A$ is also known as the *conjugate transpose* or *Hermitian transpose* of $A$. The *adjoint* is also sometimes used to refer to the adjugate of a matrix, or the tranpose of the cofactor matrix, but we will not use the term in this manner.

## Trace, determinant and characteristic polynomial

:::{prf:definition} Trace
:label: trace

The *trace* of an $n\times n$-matrix $A$ is the sum of the diagonal
entries of $A$:

$$
\tr A = \sum_{i=1}^n A_{i,i}.
$$
:::

The *determinant* of an $n\times n$-matrix $A$ can be defined in
various ways; you may have seen a different definition than the one
below.  We will make use of *permutations*.

We write $S_n$ for the set of all permutations of $\{1,\ldots,n\}$;
then $S_n$ has $n!$ elements.  To any $\sigma\in S_n$ we can attach a
*sign* $\sign(\sigma)\in\{\pm1\}$. The sign of a permutation is $(-1)^{N(\sigma)}$, where $N(\sigma)$ is the number of transpositions in the transposition decomposition of the permutation $\sigma$. 

:::{prf:definition} Determinant
The *determinant* of an $n\times n$-matrix $A$ is defined as

$$
\det A = \sum_{\sigma\in S_n} \sign(\sigma)
\prod_{i=1}^n A_{i,\sigma(i)}.
$$
:::

Using the Einstein summation convention and the Levi-Cività symbol
commonly used in physics, we can also write this as

$$
\det A=\epsilon^{i_1\cdots i_n} A_{1,i_1}\cdots A_{n,i_n}.
$$

Note that except in small cases, this is usually not how you compute a
determinant.  One option is to expand along a row or column, but this
is not much more efficient than directly using the definition.  To
compute the determinant of a larger matrices $A$, it is most
convenient to apply row (or column) operations to reduce $A$ to
triangular (or echelon) form and to use properties 4–6 below.

:::{prf:property} Properties of the determinant
:label: det-properties

1. A square matrix $A$ is invertible if and only if $\det(A)$ is
   non-zero.

2. Given two $n\times n$-matrices $A$ and $B$, we have

   $$
   \det(AB)=(\det A)(\det B).
   $$

3. The determinant of a diagonal matrix (and more generally of an
   upper or lower triangular matrix) is the product of the diagonal
   entries.

4. If $B$ is obtained from $A$ by scaling a row by a scalar $c$, then
   $\det B=c\det A$.

5. If $B$ is obtained from $A$ by swapping two rows, then $\det
   B=-\det A$.

6. If $B$ is obtained from $A$ by adding a multiple of a row to
   another row, then $\det B=\det A$.

Properties 4–6 also hold for columns instead of rows.
:::

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz
display_quiz("_static/quizzes/matrix-operations.json")
```

Finally, we define the *characteristic polynomial* of a square matrix;
this will be used in [](diagonalisation).

:::{prf:definition} Characteristic polynomial
:label: characteristic-polynomial

The *characteristic polynomial* of an $n\times n$-matrix $A$ is
the polynomial of degree $n$ in a variable $t$ defined by

$$
\chi_A(t) = \det(t\id-A).
$$
:::

:::{note}
An alternative definition of the characteristic polynomial (which
agrees with the one above up to a factor $(-1)^n$) is

$$
\chi_A(t) = \det(A-t\id).
$$
:::

***

## Exercises

:::{exercise}
Show that the definition of the matrix product $AB$ is the only one
for which {eq}`matrix-mult-linear-map` holds.
:::

:::{exercise}
Compute $[A,B]$ for $A=\begin{pmatrix}1& 2\\0& 1\end{pmatrix}$ and
$B=\begin{pmatrix}1& 0\\-1& 1\end{pmatrix}$.
:::

:::{exercise}
:label: trace-cyclic

Show that if $A$ is an $m\times n$-matrix and $B$ is an $n\times
m$-matrix, then we have $\tr(AB)=\tr(BA)$.
:::

:::{exercise}
Show that if $A$ is an $n\times n$-matrix and $c$ is a scalar, then

$$
\tr(cA)=c\tr A
\quad\text{and}
\det(cA)=c^n\det A.
$$
:::

:::{exercise}
Compute the characteristic polynomial of the matrices

$$
\begin{pmatrix}2& -1\\ 3& 2\end{pmatrix}
$$

and

$$
\begin{pmatrix}1& 0& a\\ 0& -1& b\\ 1& 0& c\end{pmatrix}
$$

(where $a$, $b$, $c$ are scalars).
:::
