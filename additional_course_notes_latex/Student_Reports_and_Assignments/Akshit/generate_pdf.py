import subprocess

tex_content = r"""\documentclass[10pt,a4paper]{article}
\usepackage[margin=1.2cm]{geometry}
\usepackage[table,xcdraw]{xcolor}
\usepackage{array}
\usepackage{booktabs}
\usepackage{microtype}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{multicol}

% Colors
\definecolor{headerblue}{RGB}{24, 76, 120}
\definecolor{accentblue}{RGB}{220, 235, 245}
\definecolor{rowlight}{RGB}{245, 248, 252}
\definecolor{rowdark}{RGB}{255, 255, 255}

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0.4pt}
\fancyhead[L]{\small\textbf{B.Sc. (Hons.) Mathematics --- Vth Semester (2026--2027)}}
\fancyhead[R]{\small\textbf{Group M1 List}}
\fancyfoot[C]{\small Page \thepage}

\renewcommand{\familydefault}{\sfdefault}

\begin{document}

\begin{center}
    {\LARGE \textbf{\color{headerblue} Department of Mathematics, Institute of Science}}\\[4pt]
    {\large \textbf{Major --- B.Sc. (Hons.) Vth Semester (Session 2026--2027)}}\\[4pt]
    {\Large \textbf{\color{headerblue} Group M1 --- Student List}}\\[4pt]
    \small \textbf{Total Students: 69} \quad | \quad Arranged in Original Sequence with Serial Numbers
\end{center}

\vspace{6pt}

\setlength{\tabcolsep}{6pt}
\renewcommand{\arraystretch}{1.2}

\rowcolors{2}{rowlight}{rowdark}
\begin{multicols}{2}
\noindent
\begin{tabular}{>{\boldmath\bfseries\color{headerblue}}r c l}
\rowcolor{headerblue}
\color{white}S.No. & \color{white}Exams Roll No. & \color{white}Student Name \\
1 & 24229MAT002 & Anchal Singh KANWAR \\
2 & 24229MAT003 & Anjali Kharwar \\
3 & 24229MAT004 & Anju Saroj \\
4 & 24229MAT005 & Anushka Singh \\
5 & 24229MAT007 & Ayushi Gupta \\
6 & 24229MAT008 & Chandani Sonkar \\
7 & 24229MAT009 & Deepika Dubey \\
8 & 24229MAT010 & Deeptanshi Yadav \\
9 & 24229MAT011 & Divyanshi Verma \\
10 & 24229MAT012 & Kamlini Singh \\
11 & 24229MAT013 & Kaushilya \\
12 & 24229MAT014 & Khyati Chaubey \\
13 & 24229MAT015 & Komal Kumari \\
14 & 24229MAT016 & Kumari Bhumi Sharma \\
15 & 24229MAT017 & Mini Yadav \\
16 & 24229MAT018 & Mithu Kumari \\
17 & 24229MAT019 & Monika Bagriya \\
18 & 24229MAT020 & Palak \\
19 & 24229MAT021 & Prachi \\
20 & 24229MAT022 & Pragya Yadav \\
21 & 24229MAT023 & Purvi Jethwa \\
22 & 24229MAT024 & Roshani Kumari \\
23 & 24229MAT025 & Sakshi Gautam \\
24 & 24229MAT026 & Samriddhi Kumari \\
25 & 24229MAT028 & Shraddha Verma \\
26 & 24229MAT029 & Shubhi Shukla \\
27 & 24229MAT030 & Shweta Pandey \\
28 & 24229MAT031 & Suman Jaiswal \\
29 & 24229MAT032 & Vandana Maurya \\
30 & 24229MAT033 & Vijeta Kumari \\
31 & 24220MAT003 & Aayushi Singh \\
32 & 24220MAT004 & Abdul Mustakeem \\
33 & 24220MAT005 & Abhinav Pal \\
34 & 24220MAT006 & Abhishek Gupta \\
35 & 24220MAT007 & Abhishek Kumar \\
\end{tabular}

\vfill\null
\columnbreak

\noindent
\begin{tabular}{>{\boldmath\bfseries\color{headerblue}}r c l}
\rowcolor{headerblue}
\color{white}S.No. & \color{white}Exams Roll No. & \color{white}Student Name \\
36 & 24220MAT008 & Abhishek Kumar \\
37 & 24220MAT009 & Abhishek Meena \\
38 & 24220MAT010 & Abhishek Rajput \\
39 & 24220MAT012 & Achal Kumar \\
40 & 24220MAT013 & Adarsh Kumar \\
41 & 24220MAT014 & Adarsh Pathak \\
42 & 24220MAT015 & Aditi Kumari \\
43 & 24220MAT016 & Aditya Pandey \\
44 & 24220MAT017 & Aditya Patel \\
45 & 24220MAT019 & Aditya Yadav \\
46 & 24220MAT021 & Akash Rai \\
47 & 24220MAT022 & Akhilesh Yadav \\
48 & 24220MAT023 & Akshatra Dev Upadhyay \\
49 & 24220MAT024 & Akshit Agarwal \\
50 & 24220MAT028 & Amandeep \\
51 & 24220MAT029 & Ambuj Singh \\
52 & 24220MAT032 & Aniket Ray \\
53 & 24220MAT033 & Aniket Verma \\
54 & 24220MAT034 & Anjali Kumari \\
55 & 24220MAT035 & Ankesh Dhakar \\
56 & 24220MAT036 & Ankit Kumar Yadav \\
57 & 24220MAT038 & Ankit Yadav \\
58 & 24220MAT039 & ANKITA MONDAL \\
59 & 24220MAT040 & Ankush Lodhi \\
60 & 24220MAT041 & Anmol Tiwari \\
61 & 24220MAT042 & Anshika Mishra \\
62 & 24220MAT044 & Anshuman Singh \\
63 & 24220MAT045 & Anushka Nandy \\
64 & 24220MAT046 & Anvisha Yadav \\
65 & 24220MAT049 & Arya Tripathi \\
66 & 24220MAT051 & Aryan Maurya \\
67 & 24220MAT052 & Ashana Maurya \\
68 & 24220MAT053 & ASHISH KUMAR \\
69 & 24220MAT055 & Asmita Maurya \\
\end{tabular}

\end{multicols}

\end{document}
"""

with open("m1_students_list.tex", "w") as f:
    f.write(tex_content)

print("Wrote m1_students_list.tex")
