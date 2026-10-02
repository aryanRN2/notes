# Abstract Algebra Notes: Group Actions & Ring Theory

This directory contains the calibrated and logically arranged LaTeX notes on **Group Actions, Permutations, and Introduction to Ring Theory**, compiled into a publication-quality PDF document.

## 📄 Master PDF & Source

- **Master Document**: [`main.tex`](file:///Users/aryanmaurya/nre/latex/main.tex)
- **Compiled PDF**: [`main.pdf`](file:///Users/aryanmaurya/nre/latex/main.pdf) (Also mirrored at [`/Users/aryanmaurya/nre/main.pdf`](file:///Users/aryanmaurya/nre/main.pdf))
- **Total Pages**: 21 pages (with clickable Table of Contents and PDF bookmarks)

---

## 🧭 Logical Ordering & Source File Mapping

The uploaded note fragments originally had non-chronological numbering and OCR cite artifacts. They have been calibrated and arranged into **11 coherent modular sections** organized under two thematic parts:

### Part I: Group Actions and Permutation Representations

| Section | Title | Modular File | Original Source Files | Topics Covered |
| :--- | :--- | :--- | :--- | :--- |
| **§ 1** | Group Actions: Left and Right Actions | [`01_group_actions_intro.tex`](file:///Users/aryanmaurya/nre/latex/sections/01_group_actions_intro.tex) | `25.tex`, `20.tex` | Left and right group actions, trivial action, left and right regular actions. |
| **§ 2** | Actions by Conjugation | [`02_conjugation_actions.tex`](file:///Users/aryanmaurya/nre/latex/sections/02_conjugation_actions.tex) | `24.tex`, `23.tex` | Conjugation on elements of $G$, left cosets $G/H$, and subgroups. |
| **§ 3** | Group Actions & Permutation Representations | [`03_permutation_representations.tex`](file:///Users/aryanmaurya/nre/latex/sections/03_permutation_representations.tex) | `23.tex`, `21.tex` *(dup: `22.tex`)*, `16.tex`, `19.tex`, `17.tex` | Equivalence between actions and homomorphisms $G \to \operatorname{Sym}(A)$, **Cayley's Theorem**. |
| **§ 4** | Kernel of an Action | [`04_kernel_of_action.tex`](file:///Users/aryanmaurya/nre/latex/sections/04_kernel_of_action.tex) | `17.tex`, `14.tex`, `15.tex` | Definition of $\ker *$, proof that $\ker * \le G$ and $\ker F = \ker *$. |
| **§ 5** | Orbits and Stabilizers | [`05_orbits_and_stabilizers.tex`](file:///Users/aryanmaurya/nre/latex/sections/05_orbits_and_stabilizers.tex) | `15.tex`, `11.tex` | Stabilizer $G_a \le G$, **Orbit-Stabilizer Theorem** bijection and $|G| = \|G^a\| \cdot \|G_a\|$. |
| **§ 6** | Orbits as Equivalence Classes & Conjugacy Classes | [`06_orbits_as_equivalence_classes.tex`](file:///Users/aryanmaurya/nre/latex/sections/06_orbits_as_equivalence_classes.tex) | `13.tex`, `12.tex`, `10.tex` | Equivalence relation induced by an action, orbit decomposition, conjugacy classes, equivalence relation proof. |
| **§ 7** | The Class Equation and Center of $p$-Groups | [`07_class_equation_and_p_groups.tex`](file:///Users/aryanmaurya/nre/latex/sections/07_class_equation_and_p_groups.tex) | `10.tex`, `6.tex` *(dups: `7.tex`, `8.tex`, `9.tex`)*, `2.tex` | Class equation, non-trivial center of $p$-groups ($\|Z(G)\| \ge p$), groups of order $p^2$ are abelian. |
| **§ 8** | Conjugacy Classes in the Symmetric Group $S_n$ | [`08_conjugacy_classes_in_Sn.tex`](file:///Users/aryanmaurya/nre/latex/sections/08_conjugacy_classes_in_Sn.tex) | `2.tex`, `4.tex` (part 1) | Cycle type formula in $S_n$, conjugacy class sizes and calculations in $S_4$ and $S_5$. |

### Part II: Introduction to Ring Theory

| Section | Title | Modular File | Original Source Files | Topics Covered |
| :--- | :--- | :--- | :--- | :--- |
| **§ 9** | Introduction to Ring Theory: Definitions & Axioms | [`09_intro_to_rings.tex`](file:///Users/aryanmaurya/nre/latex/sections/09_intro_to_rings.tex) | `4.tex` (part 2), `3.tex` | Ring axioms $(R, +, \cdot)$, zero element, ring with unity, commutative ring. |
| **§ 10** | Examples of Rings | [`10_ring_examples.tex`](file:///Users/aryanmaurya/nre/latex/sections/10_ring_examples.tex) | `3.tex`, `1.tex` | $\mathbb{Z}, \mathbb{Q}, \mathbb{R}, \mathbb{C}, \mathbb{Z}_n, \mathbb{Z}[\sqrt{p}]$, Gaussian integers $\mathbb{Z}[i]$, matrix rings $M_n(\mathbb{R}), M_n(\mathbb{Z})$. |
| **§ 11** | Special Matrix Ring: Identity & Inverse Computations | [`11_matrix_ring_with_identical_entries.tex`](file:///Users/aryanmaurya/nre/latex/sections/11_matrix_ring_with_identical_entries.tex) | `1.tex` | Ring $A = \left\{\begin{bmatrix} x & x \\ x & x \end{bmatrix}\right\}$, proof of commutativity, non-standard unity $E = \begin{bmatrix} 1/2 & 1/2 \\ 1/2 & 1/2 \end{bmatrix}$, and inverse computation. |

---

## 🛠️ How to Recompile

To recompile the document using `pdflatex`:

```bash
cd /Users/aryanmaurya/nre/latex
pdflatex -interaction=nonstopmode main.tex
pdflatex -interaction=nonstopmode main.tex
```
*(Running twice ensures that all cross-references, Table of Contents entries, and PDF bookmarks are correctly updated.)*
