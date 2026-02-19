# Mathematics for Quantum Physics

TESTTTT

*Mathematics for Quantum Physics* gives you a compact introduction
to the basic mathematical tools commonly used in quantum mechanics.
Throughout the course, we provide examples and applications, but at
the core, this is still a mathematics course. 

The exercises at the end of each section are an important part of the
material.  We recommend doing as many of these as possible, as this is
crucial for being able to apply these mathematical tools in practice.

:::{admonition} Learning goals

After following this course, you will understand the following
concepts and be able to apply them:
- Analysis
  - Taylor series
  - Fourier series and Fourier transforms
  - Differential equations
- Linear algebra
  - Matrix operations
  - Eigenvalues and eigenvectors
  - Diagonalisation
  - Hilbert spaces
- Probability theory
  - Random variables
  - Probability distributions
  - Central limit theorem
:::

As Griffiths writes in the preface to {cite}`griffiths`:

> Is all this baggage really necessary?  Perhaps not, but physics is
> like carpentry: Using the right tool makes the job *easier*, not
> more difficult, and teaching quantum mechanics without the
> appropriate mathematical equipment is like asking the student to dig
> a foundation with a screwdriver.

## Prerequisites

We assume that you are familiar with the following topics:

- differential and integral calculus
- infinite series
- complex numbers and complex functions, at the level of [Chapter
  1](https://mathforquantum.quantumtinkerer.tudelft.nl/1_complex_numbers/)
  of the lecture notes also titled [Mathematics for Quantum
  Physics](https://mathforquantum.quantumtinkerer.tudelft.nl/)
- basic arithmetic with matrices, in particular the topics covered in
  the appendix ([](basic-matrix-arithmetic)).

When studying the chapters on linear algebra, you may find it useful
to have a look at the open interactive textbook on [Linear
Algebra](https://interactivetextbooks.tudelft.nl/linear-algebra/).
This covers some of the material from a different viewpoint (still
aimed at applications, but not specifically in physics) and has some
additional topics like dynamical systems and matrix decompositions.

## Notational conventions

We write $\bar z$ for the complex conjugate of a complex number $z$,
following the convention in mathematics.  In physics and other applied
fields, the complex conjugate is often denoted by $z^*$.

:::{warning}
In some web browsers (notably Firefox), the horizontal bar for complex
conjugation is invisible for some formulas and zoom levels.  In case
the formulas $\overline{A}$ and $A$ look identical, try zooming in or
out!
:::

In the section on [](hilbert-spaces), we adopt the
“bra-ket” notation from physics for inner products on Hilbert spaces.
We also use the notation $A^\dagger$ for the Hermitean adjoint of an
operator $A$ or the conjugate transpose of a matrix $A$.

For Fourier series and Fourier transforms, we have chosen a
normalisation convention with a factor of $2\pi$ inside complex
exponentials.  This is natural in the context of periodic functions
with period 1, and avoids normalising factors.

## Contributing

Whether you are a student taking this course or an instructor reusing
the materials, we welcome all contributions.  The source code is
available in a TU Delft [GitLab
repository](https://gitlab.tudelft.nl/opentextbooks/MQP/).  Please
[contact the author](mailto:P.J.Bruin@math.leidenuniv.nl) if you have
any suggestions or corrections!

## Acknowledgements

[Chapter 4](differential-equations) was adapted from the notes for the
course [Mathematics for Quantum
Physics](https://mathforquantum.quantumtinkerer.tudelft.nl/) (part of
the Quantum Science and Quantum Information minor at TU Delft) by
Sonia Conesa Boj, Michael Wimmer and others.

I would like to thank Sarah Arpin for various additions and
corrections to these notes, and Michal Kuchar and Gonçalo Meneses for
developing the interactive content.

These notes were built using [Jupyter Book](https://jupyterbook.org/).
Parts of the technical “infrastructure” were adapted from the [Jupyter
Book demo](https://idemalab.tudelft.nl/jupyterbookdemo/) by Timon
Idema.

## References

:::{bibliography}
:::
