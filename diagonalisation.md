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

# Diagonalisation

A very common example of a basis transformation is *diagonalisation*
of a matrix.  For this we first introduce the concept of *eigenvalues*
and *eigenvectors*.  These concepts are fundamentally important in
quantum mechanics.

## Eigenvalues and eigenvectors

Consider an $n\times n$-matrix $T$ with complex entries.  We view $T$
as a linear map on $\CC^n$.

:::{prf:definition} Eigenvalues and eigenvectors
An *eigenvector* for $T$ is a non-zero vector $\vv$ such that

$$
T\vv = \lambda\vv
$$

for some scalar $\lambda$.  This $\lambda$ is called the
*eigenvalue* of $T$ acting on $\vv$.
:::

Writing $I$ for the $n\times n$ identity matrix, we see that if $\vv$
is an eigenvector with eigenvalue $\lambda$, then

$$
(A-\lambda I)\vv = 0.
$$

This means that $A-\lambda I$ is not invertible; equivalently, its
determinant vanishes.  Thus, if $\lambda$ is an eigenvalue of $A$, we
have

$$
\det(A-\lambda I)=0.
$$

This implies that the eigenvalues of $A$ are roots of the
characteristic polynomial $\chi_A$ (see
{prf:ref}`characteristic-polynomial`).  We can factor the
characteristic polynomial as

$$
\chi_A(t) = (t-\lambda_1)^{k_1}\cdots(t-\lambda_r)^{k_r}
$$

where $\lambda_1,\ldots,\lambda_r$ are the distinct roots of
$\chi_A(t)$ and each $k_i$ is an integer called the *multiplicity* of
$\lambda_i$ as a root of $\chi_A(t)$.

## Diagonalising a matrix

The idea of diagonalisation is that it is often easiest to understand
a linear map $A$ if we can find a basis of our space consisting of
vectors on which $A$ acts as multiplication by some scalar.

:::{prf:definition} Diagonalisation
An $n\times n$-matrix $A$ is *diagonalisable* if there exist a
diagonal matrix $D$ and an invertible $n\times n$-matrix $P$ such that

$$
A = PDP^{-1},
$$
:::

We can rewrite the above equation as $AP=PD$.  Let us write
$\vv_1,\ldots,\vv_n$ for the columns of $P$ and
$\lambda_1,\ldots,\lambda_n$ for the diagonal entries of $D$.  Then we
compute

$$
AP=\begin{pmatrix}A\vv_1& A\vv_2& \cdots & A\vv_n\end{pmatrix}
$$

and

$$
PD=\begin{pmatrix}\lambda_1\vv_1& A\vv_2& \cdots & \lambda_n\vv_n\end{pmatrix}
$$

We therefore see that the equation $AP=PD$ comes down to the $n$
equations $A\vv_i=\lambda_i\vv_i$.  In other words, each $\vv_i$ is an
eigenvector of $A$ and $\lambda_i$ is the corresponding eigenvalue.

The fact that $P$ is invertible means that the eigenvectors $\vv_i$
form a basis of $\CC^n$.  We obtain the following conclusion.

:::{prf:theorem}
An $n\times n$-matrix $A$ is diagonalisable precisely when there
exists a basis of $\CC^n$ consisting of eigenvectors for $A$.
:::

This also gives us a way to tell whether $A$ is diagonalisable, and if
so to determine matrices $D$ and $P$ as above:

1. Determine the eigenvalues $\lambda_1,\ldots,\lambda_r$ of $A$ by
   finding the roots of the characteristic polynomial $\chi_A$.

2. For each eigenvalue $\lambda_i$, say with multiplicity $k_i$,
   determine if there exist $k_i$ linearly independent eigenvectors
   $\vv_{\lambda_i,1},\ldots,\vv_{\lambda_i,k_i}$ with eigenvalue
   $\lambda_i$.

3. The matrix $A$ is diagonalisable if and only if there exist $k_i$
   linearly independent eigenvectors with eigenvalue $\lambda_i$ for
   all $i$.  In this case, the matrices

   $$
   D = \begin{pmatrix}
   \lambda_1 I_{k_1}& 0& \cdots& 0\\
   0& \lambda_2 I_{k_2}& \cdots& 0\\
   \vdots& \vdots& \ddots& \vdots\\
   0& 0& \cdots& \lambda_r I_{k_r}\\
   \end{pmatrix}
   $$

   and

   $$
   P = \begin{pmatrix}\vv_{\lambda_1,1}& \cdots& \vv_{\lambda_1,k_1}&
   \vv_{\lambda_2,1}& \cdots& \vv_{\lambda_2,k_2}&
   \cdots& \vv_{\lambda_r,1}& \cdots& \vv_{\lambda_r, k_r}\end{pmatrix}
   $$

   give a diagonalisation of $A$.

***

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz
display_quiz("_static/quizzes/diagonalisation.json")
```

## Exercises

:::{exercise}
Find the eigenvalues of the matrix

$$
\begin{pmatrix}-8& 6\\ -9& 7\end{pmatrix}
$$

and for each eigenvalue find a corresponding eigenvector.
:::

:::{exercise}
Diagonalise the matrix $\begin{pmatrix}a& 0\\ 0& d\end{pmatrix}$,
where $a$ and $d$ are arbitrary scalars.

(*Hint:* think twice before doing unnecessary computations!)
:::

:::{exercise}
Consider the rotation matrix

$$
\begin{pmatrix}\cos\phi& -\sin\phi\\ \sin\phi& \cos\phi\end{pmatrix}.
$$

(This represents a rotation around an angle $\phi$ in the
$(x,y)$-plane.)  Find the eigenvalues and eigenvectors of this matrix.

For which angles $\phi$ are the eigenvalues real?  Interpret your
answer geometrically.

:::

:::{exercise}
1. Assume $A=PDP^{-1}$ with $P$ invertible and $D$ a *scalar* matrix,
   i.e. $D$ is a scalar multiple of the identity matrix.  Show that
   $A=D$.

2. Consider a $2\times 2$-matrix $A$ with $\tr(A)^2=4\det A$.  Show
   that $A$ is diagonalisable precisely when $A$ is a scalar matrix.
:::
