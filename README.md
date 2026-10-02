# 🎓 Master University Mathematics, Sciences & Computing LaTeX Notes Suite

Welcome to the comprehensive repository of university lecture notes, LaTeX monographs, vector geometric figures, university semester examination papers, scientific computing code suites, and Beamer lecture presentations.

---

## 🗂️ Complete Repository Architecture

```
.
├── Core Lecture Notes & Master PDFs (Root)
│   ├── Abstract_Algebra_Notes.pdf / .tex             # Core MATMJ51 Course Notes
│   ├── Analytic_Geometry_Notes.pdf / .tex            # Core MATMJ52 Course Notes
│   ├── Calculus_Analysis_Notes.pdf / .tex            # Core Calculus & Analysis Lecture Notes
│   ├── Coordinate_Geometry_Notes.pdf / .tex          # Coordinate Geometry Master Reference
│   ├── Food_Chemistry_and_Adulteration_Notes.pdf/.tex # Chemistry Interdisciplinary Notes
│   ├── Common_Adulterants_in_Food.pdf / .tex         # Food Adulteration Quick Reference & Summary
│   ├── Metric_Spaces_Notes.pdf / .tex                # Core MATMJ53 Course Notes
│   ├── Metric_Spaces_New_Lectures.pdf / .tex         # Metric Spaces Advanced Lectures Supplement
│   └── Numerical_Analysis_Notes.pdf / .tex           # Core MATMJ54 Course Notes
│
├── classical_and_rigid_body_mechanics/               # ⚙️ Classical & Rigid Body Mechanics
│   ├── complete_mechanics_proofs_manual.pdf/.tex     # Master Mechanics Proofs Manual (Forces, SHM, Orbits)
│   ├── Tensor_Analysis_Complete_Notes.pdf/.tex       # Tensor Calculus & Coordinate Transformations
│   ├── MTB202_Statics_and_Dynamics_Notes.pdf/.tex    # MTB-202 Statics & Dynamics Notes
│   ├── Classical_Mechanics_Statics_Notes.pdf/.tex    # Equilibrium & Catenary Notes
│   └── part1_forces.tex ... part9_cheat_sheet.tex    # Modular Chapter LaTeX Sources
│
├── numerical_computing_python/                       # 🐍 Python Scientific Computing Suite
│   ├── detailed/                                     # 20 Complete Numerical Method Implementations (.py)
│   ├── handbook.tex & handbook.pdf                   # Complete Practical Laboratory Handbook
│   ├── codes_by_sciqb.tex & codes_by_sciqb.pdf       # sciqb Numerical Computing Reference
│   ├── Numerical_Computing_Python_Handbook.pdf       # Compiled Master Computing Manual
│   └── generate_handbook.py                          # Automated PDF Handbook Generator
│
├── metric_spaces_monograph/                          # 🌐 Metric Spaces 2nd Edition Monograph
│   ├── Metric_Spaces_Comprehensive_Monograph.pdf     # Publication-Grade Complete Monograph
│   ├── main.tex & preamble.tex                       # Master Monograph LaTeX Source
│   └── chapters/ (ch01 - ch07 + appendices)          # 7 Full-Length Rigorous Chapters
│
├── abstract_algebra_monograph/                       # 🧮 Abstract Algebra Monograph & Lectures
│   ├── Abstract_Algebra_Monograph.pdf / main.tex     # 5-Unit Monograph (Groups, Rings, Fields, Polynomials)
│   ├── chapters/ (unit1 - unit5)                     # Modular Unit Sources
│   ├── toc_gen/                                      # Monograph Cover & Table of Contents Suite
│   └── shreya_lecture_notes/                         # Complete Class Lecture Transcripts & Proofs (Part 1 & 2)
│
├── analytical_geometry_modular/                      # 📐 Analytical Geometry Enhanced Suite
│   ├── analytical_geometry_notes.pdf / .tex          # Enhanced Lecture Notes (Pages 1–69) by sciqb
│   └── ch1_polar_conics.tex ... ch6_the_sphere       # Modular Chapters with TikZ Vector Visuals
│
├── numerical_analysis_modular/                       # 📊 Numerical Analysis Enhanced Suite
│   ├── numerical_analysis_notes.pdf / .tex           # Enhanced Lecture Notes (Pages 1–68) by sciqb
│   └── na_ch1_root_finding ... na_ch6_quadrature     # Complete Modular Chapters with Proofs
│
├── solutions_and_problem_sets/                       # ✍️ Solved Problem Manuals & Question Sets
│   ├── Conic_Sections_Polar_Coordinates_Solutions    # Step-by-step Polar Conic Exercises
│   ├── numerical_analysis_solutions.pdf / .tex       # Numerical Methods Examination Solutions
│   ├── numerical_analysis_2019_solutions.pdf/.tex    # 2019 University Examination Solutions
│   └── exercise_4_2_solutions.pdf / .tex             # Algebra Exercise Solutions Manual
│
├── university_exam_papers_latex/                     # 📚 University Semester Examination Papers (LaTeX)
│   ├── Mathematics/                                  # 61+ University Maths Papers (BSc/BA Sem I-VI)
│   ├── Computer_Science/                             # 85+ Computer Science Exam Papers
│   ├── Physics/                                      # 41+ Physics Exam Papers
│   ├── Chemistry/                                    # 42+ Chemistry Exam Papers
│   ├── Statistics/                                   # 56+ Statistics Exam Papers
│   ├── Botany/                                       # 34+ Botany Exam Papers
│   ├── Zoology/                                      # 39+ Zoology Exam Papers
│   ├── Geography/                                    # 34+ Geography Exam Papers
│   ├── Geology/                                      # 35+ Geology Exam Papers
│   └── Commerce/                                     # 220+ Commerce Exam Papers (Sem I-VI)
│
├── additional_course_notes_latex/                    # 📝 Additional Topic Notes & LaTeX Derivations
│   ├── Conformal_Mapping/                            # Conformal Mapping & Complex Transformations
│   ├── Quantum_Planck_Derivation/                    # Planck's Law & Modern Physics Foundations
│   ├── Machine_Learning_Foundations/                 # MLF Complete Foundations & Notes
│   ├── Geography_Master_Notes/                       # Human Geography & Resource Planning Notes
│   ├── Group_Actions_and_Rings_NRE/                  # Group Actions, Stabilizers & Rings Suite
│   ├── Calculus_and_Antiderivatives/                 # Antiderivatives & Differential Calculus Notes
│   ├── Numerical_Methods_Supplements/                # Iterative Methods & Complete Lecture Notes
│   └── Academic_and_Project_Reports/                 # LaTeX Templates & Academic Reports
│
├── dbms_nptel_beamer_lectures/                       # 🗄️ Database Management Systems (Beamer Slides)
│   └── Week 1/ ... Week 12/                          # 64 Comprehensive Lecture Slides PDFs
│
├── figures/                                          # Vector Graphics Suite (Analytic Geometry)
├── export/                                           # 📦 Master Central PDF Distribution Directory
└── newton rapso.py                                   # Standalone Newton-Raphson Solver
```

---

## 🚀 Quick Start: Running Python Numerical Codes

The `numerical_computing_python/detailed/` folder contains 20 production-ready, pure Python 3 implementations with formatted iteration convergence tables.

```bash
# Example: Run the Newton-Raphson solver
python3 numerical_computing_python/detailed/03_newton_raphson_detailed.py

# Example: Run Runge-Kutta 4th Order (RK4) ODE solver
python3 numerical_computing_python/detailed/18_rk4_detailed.py
```

### Included Methods:
1. **Root Finding**: Bisection, Regula Falsi, Newton-Raphson, Secant, Fixed-Point Iteration.
2. **Linear Systems**: Gaussian Elimination (with Partial Pivoting), Gauss-Jordan Inversion, Gauss-Jacobi, Gauss-Seidel.
3. **Interpolation**: Lagrange Polynomial, Newton's Divided Difference, Newton's Forward Difference.
4. **Numerical Quadrature**: Composite Trapezoidal Rule, Simpson's 1/3 Rule, Simpson's 3/8 Rule.
5. **ODEs**: Forward Euler, Modified Euler / Heun's Method, Classical 4th-Order Runge-Kutta (RK4).
6. **Eigenvalues & Fitting**: Power Method for Dominant Eigenvalue, Least-Squares Linear Curve Fitting.

---

## 🛠️ Building LaTeX Notes Locally

Requirements: A modern TeX distribution (`pdflatex`, `xelatex`, or MacTeX).

```bash
# Compile root course notes:
pdflatex -interaction=nonstopmode Abstract_Algebra_Notes.tex
pdflatex -interaction=nonstopmode Metric_Spaces_Notes.tex
pdflatex -interaction=nonstopmode Common_Adulterants_in_Food.tex

# Compile Classical Mechanics master manual:
cd classical_and_rigid_body_mechanics && pdflatex -interaction=nonstopmode main.tex

# Compile Metric Spaces monograph:
cd metric_spaces_monograph && pdflatex -interaction=nonstopmode main.tex

# Compile Abstract Algebra monograph:
cd abstract_algebra_monograph && pdflatex -interaction=nonstopmode main.tex
```

---

## 🤝 Contributing & Collaboration

Contributions, corrections, proof enhancements, and additions are welcome! Feel free to open an issue or submit a pull request.
