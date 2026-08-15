# University Mathematics Course Notes & Master Revision Suite

Comprehensive, rigorously typed LaTeX lecture notes, vector geometric figures, and quick revision cheat sheets for university mathematics courses.

---

## 📚 Course Modules & PDFs

All compiled PDF documents are available in the [`export/`](export/) directory:

| Course Code | Subject Title | Master PDF | LaTeX Source | Key Topics |
| :--- | :--- | :--- | :--- | :--- |
| **MATMJ51** | **Abstract Algebra** | [`export/Abstract_Algebra_Notes.pdf`](export/Abstract_Algebra_Notes.pdf) | [`Abstract_Algebra_Notes.tex`](Abstract_Algebra_Notes.tex) | Groups, Cyclic Groups, Permutations ($S_n, A_n$), Cosets, Lagrange's Theorem, Normal Subgroups, Quotient Groups, Homomorphisms, Isomorphism Theorems |
| **MATMJ52** | **Analytical Geometry** | [`export/Coordinate_Geometry_Notes.pdf`](export/Coordinate_Geometry_Notes.pdf) | [`Coordinate_Geometry_Notes.tex`](Coordinate_Geometry_Notes.tex) | Polar Coordinates, Straight Lines, Circles, Polar Conics ($l/r = 1 + e\cos\theta$), Chords, Tangents, Normals, Chord of Contact, Polars |
| **MATMJ53** | **Metric & Matrix Spaces** | [`export/Metric_Spaces_Notes.pdf`](export/Metric_Spaces_Notes.pdf) | [`Metric_Spaces_Notes.tex`](Metric_Spaces_Notes.tex) | Metric Axioms ($L_1, L_2, L_\infty$, Discrete, Matrix Frobenius Norm), Open Spheres, Open Sets, Limit Points, Derived Sets, Closed Sets, Closures |
| **MATMJ54** | **Numerical Analysis** | [`export/Numerical_Analysis_Notes.pdf`](export/Numerical_Analysis_Notes.pdf) | [`Numerical_Analysis_Notes.tex`](Numerical_Analysis_Notes.tex) | Bisection, Regula-Falsi, Secant ($p \approx 1.618$), Newton-Raphson ($p = 2$), Fixed-Point Iteration, Fast Division-Free Inverses, Error Recurrences |

---

## 📐 Vector Graphics Suite

All geometric figures for analytical geometry are generated using Python Matplotlib with exact analytic geometry coordinates and embedded as vector PDFs in [`figures/`](figures/):

- `fig1_polar_coordinates.pdf`: Polar coordinate system projection ($x=r\cos\theta, y=r\sin\theta$).
- `fig2_polar_straight_line.pdf`: Polar straight line normal form ($p = r\cos(\theta-\alpha)$).
- `fig3_polar_circle_general.pdf`: General polar circle with Law of Cosines $\triangle POC$.
- `fig4_polar_circle_cases.pdf`: Standard polar circle configurations ($r = 2a\cos\theta, r = 2a\sin\theta$).
- `fig5_polar_conic_focus_directrix.pdf`: Focus-directrix projection proving $l/r = 1 + e\cos\theta$.
- `fig6_chord_of_conic.pdf`: Conic chord subtending angle $2\beta$ at focus.
- `fig7_tangent_and_normal.pdf`: Tangent line and orthogonal normal line at point of contact.
- `fig8_chord_of_contact.pdf`: Tangents and chord of contact from external point $A(r_1, \theta_1)$.

To regenerate the vector diagrams:
```bash
python3 figures/generate_geometry_figures.py
```

---

## ⚡ Quick Revision Cheat Sheets

Each master note concludes with a **Master Quick Revision Cheat Sheet** module containing:
1. Axioms, definitions, and standard forms.
2. Complete classification and property tables.
3. Order of convergence and asymptotic error bounds.
4. Key exam formulas and short proof summaries.

---

## 🛠️ Building the Notes Locally

Prerequisites: A modern TeX distribution (`pdflatex`, `xelatex`, or MacTeX) and Python 3 with `matplotlib` and `numpy`.

To compile any note:
```bash
pdflatex -interaction=nonstopmode Abstract_Algebra_Notes.tex
pdflatex -interaction=nonstopmode Coordinate_Geometry_Notes.tex
pdflatex -interaction=nonstopmode Metric_Spaces_Notes.tex
pdflatex -interaction=nonstopmode Numerical_Analysis_Notes.tex
```

---

## 🤝 Contributing & Collaboration

Contributions, corrections, and improvements are welcome! Feel free to open an issue or submit a pull request.
