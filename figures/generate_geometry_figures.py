import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

# Set publication quality styling
plt.rcParams.update({
    'font.size': 11,
    'font.family': 'sans-serif',
    'axes.labelsize': 12,
    'axes.titlesize': 13,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'lines.linewidth': 2,
    'figure.autolayout': True,
    'savefig.dpi': 300,
    'savefig.bbox': 'tight'
})

out_dir = "/Users/aryanmaurya/class notes/figures"
os.makedirs(out_dir, exist_ok=True)

# Color Palette
NAVY = "#1A365D"
TEAL = "#0D9488"
BLUE = "#3182CE"
GOLD = "#D69E2E"
RED  = "#E53E3E"
SLATE = "#4A5568"

# -------------------------------------------------------------
# Figure 1: Polar Coordinate System & Cartesian Projection
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6, 4.5))
ax.set_aspect('equal')

# Initial line OX
ax.annotate('', xy=(5.0, 0), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", color=NAVY, lw=2.5))
ax.plot(0, 0, 'o', color=NAVY, markersize=7)
ax.text(-0.25, -0.3, r'Pole $O(0,0)$', color=NAVY, fontweight='bold', fontsize=11)
ax.text(5.1, -0.05, r'Initial Line $OX$', color=NAVY, fontweight='bold', fontsize=11)

r_val = 3.6
theta_deg = 38.0
theta_rad = np.deg2rad(theta_deg)
px = r_val * np.cos(theta_rad)
py = r_val * np.sin(theta_rad)

# Radius vector OP
ax.plot([0, px], [0, py], color=TEAL, lw=2.5)
ax.plot(px, py, 'o', color=TEAL, markersize=8)
ax.text(px + 0.15, py + 0.1, r'$P(r, \theta)$', color=TEAL, fontweight='bold', fontsize=12)
ax.text(px/2 - 0.25, py/2 + 0.2, r'Radius Vector $r$', color=TEAL, fontweight='bold', fontsize=11)

# Angle theta arc
arc_theta = np.linspace(0, theta_rad, 50)
arc_r = 1.0
ax.plot(arc_r * np.cos(arc_theta), arc_r * np.sin(arc_theta), color=BLUE, lw=2)
ax.text(1.15, 0.35, r'$\theta$ (Vectorial Angle)', color=BLUE, fontweight='bold', fontsize=11)

# Cartesian projection PM and OM
ax.plot([px, px], [0, py], '--', color=SLATE, lw=1.5)
ax.plot([0, px], [py, py], '--', color=SLATE, lw=1.5)
ax.plot(px, 0, 'o', color=SLATE, markersize=5)
ax.text(px + 0.05, -0.35, r'$M(x, 0)$', color=SLATE, fontsize=10)
ax.text(px/2 - 0.2, -0.35, r'$x = r\cos\theta$', color=SLATE, fontsize=10)
ax.text(-1.4, py, r'$y = r\sin\theta$', color=SLATE, fontsize=10)

# Right angle square at M
sq_sz = 0.22
ax.plot([px - sq_sz, px - sq_sz, px], [0, sq_sz, sq_sz], color=SLATE, lw=1.2)

ax.set_xlim(-1.8, 6.0)
ax.set_ylim(-0.8, 3.2)
ax.axis('off')
ax.set_title("Polar Coordinate System & Projections", color=NAVY, fontweight='bold', pad=12)
plt.savefig(os.path.join(out_dir, "fig1_polar_coordinates.pdf"))
plt.savefig(os.path.join(out_dir, "fig1_polar_coordinates.png"))
plt.close()

# -------------------------------------------------------------
# Figure 2: Polar Straight Line p = r cos(theta - alpha)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.5, 5))
ax.set_aspect('equal')

# Initial line OX
ax.annotate('', xy=(6.0, 0), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", color=NAVY, lw=2.5))
ax.plot(0, 0, 'o', color=NAVY, markersize=7)
ax.text(-0.3, -0.3, r'Pole $O$', color=NAVY, fontweight='bold', fontsize=11)
ax.text(6.1, -0.05, r'$OX$', color=NAVY, fontweight='bold', fontsize=11)

p_len = 2.4
alpha_deg = 32.0
alpha_rad = np.deg2rad(alpha_deg)
nx = p_len * np.cos(alpha_rad)
ny = p_len * np.sin(alpha_rad)

# Normal vector ON
ax.plot([0, nx], [0, ny], color=RED, lw=2.5)
ax.plot(nx, ny, 'o', color=RED, markersize=7)
ax.text(nx/2 - 0.25, ny/2 + 0.2, r'$p$', color=RED, fontweight='bold', fontsize=12)
ax.text(nx + 0.15, ny + 0.15, r'$N(p, \alpha)$', color=RED, fontweight='bold', fontsize=11)

# Line RS perpendicular to ON
dir_x = -np.sin(alpha_rad)
dir_y = np.cos(alpha_rad)
t_vals = np.linspace(-2.2, 2.5, 100)
line_x = nx + t_vals * dir_x
line_y = ny + t_vals * dir_y
ax.plot(line_x, line_y, color=TEAL, lw=2.5)
ax.text(line_x[-1] - 0.2, line_y[-1] + 0.2, r'Line $RS$', color=TEAL, fontweight='bold', fontsize=12)

# Point R(r, theta) on the line for t = 1.8
t_R = 1.8
rx = nx + t_R * dir_x
ry = ny + t_R * dir_y
theta_R_rad = np.arctan2(ry, rx)

ax.plot([0, rx], [0, ry], color=BLUE, lw=2)
ax.plot(rx, ry, 'o', color=BLUE, markersize=7)
ax.text(rx - 0.7, ry + 0.15, r'$R(r, \theta)$', color=BLUE, fontweight='bold', fontsize=11)
ax.text(rx/2 - 0.35, ry/2 + 0.1, r'$r$', color=BLUE, fontweight='bold', fontsize=11)

# Normal right angle square at N
sq_len = 0.25
u_norm = np.array([np.cos(alpha_rad), np.sin(alpha_rad)])
u_line = np.array([dir_x, dir_y])
pt1 = np.array([nx, ny]) - sq_len * u_norm
pt2 = pt1 + sq_len * u_line
pt3 = np.array([nx, ny]) + sq_len * u_line
ax.plot([pt1[0], pt2[0], pt3[0]], [pt1[1], pt2[1], pt3[1]], color=RED, lw=1.5)

# Angle arcs
arc_a = np.linspace(0, alpha_rad, 40)
ax.plot(1.1 * np.cos(arc_a), 1.1 * np.sin(arc_a), color=RED, lw=1.8)
ax.text(1.3, 0.3, r'$\alpha$', color=RED, fontweight='bold', fontsize=11)

arc_th = np.linspace(0, theta_R_rad, 60)
ax.plot(0.7 * np.cos(arc_th), 0.7 * np.sin(arc_th), color=BLUE, lw=1.8)
ax.text(0.45, 0.85, r'$\theta$', color=BLUE, fontweight='bold', fontsize=11)

arc_diff = np.linspace(alpha_rad, theta_R_rad, 40)
ax.plot(1.6 * np.cos(arc_diff), 1.6 * np.sin(arc_diff), color=GOLD, lw=2)
ax.text(1.3, 1.45, r'$\theta - \alpha$', color=GOLD, fontweight='bold', fontsize=11)

ax.set_xlim(-0.8, 6.5)
ax.set_ylim(-1.0, 4.2)
ax.axis('off')
ax.set_title(r"Polar Straight Line: $p = r\cos(\theta - \alpha)$", color=NAVY, fontweight='bold', pad=12)
plt.savefig(os.path.join(out_dir, "fig2_polar_straight_line.pdf"))
plt.savefig(os.path.join(out_dir, "fig2_polar_straight_line.png"))
plt.close()

# -------------------------------------------------------------
# Figure 3: Polar Circle r^2 - 2rR cos(theta - alpha) + R^2 - a^2 = 0
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.5, 5))
ax.set_aspect('equal')

# Initial line OX
ax.annotate('', xy=(6.0, 0), xytext=(0, 0),
            arrowprops=dict(arrowstyle="->", color=NAVY, lw=2.5))
ax.plot(0, 0, 'o', color=NAVY, markersize=7)
ax.text(-0.3, -0.3, r'Pole $O$', color=NAVY, fontweight='bold', fontsize=11)
ax.text(6.1, -0.05, r'$OX$', color=NAVY, fontweight='bold', fontsize=11)

R_val = 3.2
alpha_c = np.deg2rad(28.0)
cx = R_val * np.cos(alpha_c)
cy = R_val * np.sin(alpha_c)
radius_a = 1.8

# Draw circle
circle = patches.Circle((cx, cy), radius_a, edgecolor=TEAL, facecolor=TEAL, alpha=0.1, lw=2.5)
circle_edge = patches.Circle((cx, cy), radius_a, edgecolor=TEAL, facecolor='none', lw=2.5)
ax.add_patch(circle)
ax.add_patch(circle_edge)

# Center C point and segment OC = R
ax.plot([0, cx], [0, cy], color=RED, lw=2.2)
ax.plot(cx, cy, 'o', color=RED, markersize=7)
ax.text(cx + 0.15, cy - 0.15, r'$C(R, \alpha)$', color=RED, fontweight='bold', fontsize=11)
ax.text(cx/2, cy/2 - 0.3, r'$R$', color=RED, fontweight='bold', fontsize=11)

# Secant ray from O at theta = 55 deg
theta_sec = np.deg2rad(55.0)
b_term = 2 * (cx * np.cos(theta_sec) + cy * np.sin(theta_sec))
c_term = cx**2 + cy**2 - radius_a**2
disc = b_term**2 - 4 * c_term
r1 = (b_term - np.sqrt(disc)) / 2
r2 = (b_term + np.sqrt(disc)) / 2

px = r1 * np.cos(theta_sec)
py = r1 * np.sin(theta_sec)
qx = r2 * np.cos(theta_sec)
qy = r2 * np.sin(theta_sec)

# Secant line
ax.plot([0, qx * 1.15], [0, qy * 1.15], color=BLUE, lw=2)
ax.plot(px, py, 'o', color=BLUE, markersize=7)
ax.plot(qx, qy, 'o', color=BLUE, markersize=7)
ax.text(px - 0.65, py + 0.15, r'$P(r, \theta)$', color=BLUE, fontweight='bold', fontsize=11)
ax.text(qx + 0.15, qy + 0.15, r'$Q$', color=BLUE, fontweight='bold', fontsize=11)
ax.text(px/2 - 0.35, py/2 + 0.2, r'$r$', color=BLUE, fontweight='bold', fontsize=11)

# Radius lines CP and CQ
ax.plot([cx, px], [cy, py], color=GOLD, lw=2.2)
ax.plot([cx, qx], [cy, qy], '--', color=GOLD, lw=1.5)
ax.text((cx + px)/2 - 0.25, (cy + py)/2 + 0.15, r'$a$', color=GOLD, fontweight='bold', fontsize=12)

# Angle arcs
arc_a = np.linspace(0, alpha_c, 40)
ax.plot(1.1 * np.cos(arc_a), 1.1 * np.sin(arc_a), color=RED, lw=1.8)
ax.text(1.3, 0.25, r'$\alpha$', color=RED, fontweight='bold', fontsize=11)

arc_th = np.linspace(0, theta_sec, 50)
ax.plot(0.7 * np.cos(arc_th), 0.7 * np.sin(arc_th), color=BLUE, lw=1.8)
ax.text(0.45, 0.75, r'$\theta$', color=BLUE, fontweight='bold', fontsize=11)

arc_diff = np.linspace(alpha_c, theta_sec, 40)
ax.plot(1.6 * np.cos(arc_diff), 1.6 * np.sin(arc_diff), color=GOLD, lw=2)
ax.text(1.5, 1.25, r'$\theta - \alpha$', color=GOLD, fontweight='bold', fontsize=11)

ax.set_xlim(-0.8, 6.2)
ax.set_ylim(-0.8, 4.5)
ax.axis('off')
ax.set_title(r"Polar Circle: $r^2 - 2rR\cos(\theta - \alpha) + R^2 - a^2 = 0$", color=NAVY, fontweight='bold', pad=12)
plt.savefig(os.path.join(out_dir, "fig3_polar_circle_general.pdf"))
plt.savefig(os.path.join(out_dir, "fig3_polar_circle_general.png"))
plt.close()

# -------------------------------------------------------------
# Figure 4: Particular Cases of Circle (r = 2a cos theta & r = 2a sin theta)
# -------------------------------------------------------------
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4.5))

# Subplot 1: r = 2a cos(theta)
ax1.set_aspect('equal')
a_rad = 1.6
circle1 = patches.Circle((a_rad, 0), a_rad, edgecolor=TEAL, facecolor=TEAL, alpha=0.1, lw=2.5)
circle1_e = patches.Circle((a_rad, 0), a_rad, edgecolor=TEAL, facecolor='none', lw=2.5)
ax1.add_patch(circle1)
ax1.add_patch(circle1_e)

ax1.annotate('', xy=(3.8, 0), xytext=(-0.8, 0), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2))
ax1.annotate('', xy=(0, 2.3), xytext=(0, -2.3), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2))
ax1.plot(0, 0, 'o', color=NAVY, markersize=7)
ax1.plot(a_rad, 0, 'o', color=RED, markersize=7)
ax1.text(-0.35, -0.35, r'$O$', color=NAVY, fontweight='bold', fontsize=11)
ax1.text(a_rad - 0.1, -0.4, r'$C(a, 0)$', color=RED, fontweight='bold', fontsize=11)
ax1.text(3.9, -0.1, r'$OX$', color=NAVY, fontweight='bold', fontsize=11)
ax1.set_xlim(-1.0, 4.2)
ax1.set_ylim(-2.5, 2.5)
ax1.axis('off')
ax1.set_title(r"Case 1: $r = 2a\cos\theta$ (Pole on circle, $OX$ along diameter)", color=NAVY, fontweight='bold', fontsize=11)

# Subplot 2: r = 2a sin(theta)
ax2.set_aspect('equal')
circle2 = patches.Circle((0, a_rad), a_rad, edgecolor=BLUE, facecolor=BLUE, alpha=0.1, lw=2.5)
circle2_e = patches.Circle((0, a_rad), a_rad, edgecolor=BLUE, facecolor='none', lw=2.5)
ax2.add_patch(circle2)
ax2.add_patch(circle2_e)

ax2.annotate('', xy=(2.3, 0), xytext=(-2.3, 0), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2))
ax2.annotate('', xy=(0, 3.8), xytext=(0, -0.8), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2))
ax2.plot(0, 0, 'o', color=NAVY, markersize=7)
ax2.plot(0, a_rad, 'o', color=RED, markersize=7)
ax2.text(-0.35, -0.35, r'$O$', color=NAVY, fontweight='bold', fontsize=11)
ax2.text(0.15, a_rad - 0.1, r'$C(a, \pi/2)$', color=RED, fontweight='bold', fontsize=11)
ax2.text(2.4, -0.1, r'$OX$ (Tangent)', color=NAVY, fontweight='bold', fontsize=11)
ax2.set_xlim(-2.5, 2.5)
ax2.set_ylim(-1.0, 4.2)
ax2.axis('off')
ax2.set_title(r"Case 2: $r = 2a\sin\theta$ (Pole on circle, $OX$ is tangent)", color=NAVY, fontweight='bold', fontsize=11)

plt.savefig(os.path.join(out_dir, "fig4_polar_circle_cases.pdf"))
plt.savefig(os.path.join(out_dir, "fig4_polar_circle_cases.png"))
plt.close()

# -------------------------------------------------------------
# Figure 5: Conic Section Focus-Directrix Projection l/r = 1 + e cos theta
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.5, 5))
ax.set_aspect('equal')

e = 0.65
l = 2.4
d_dir = l / e  # ~3.69
x_dir = -d_dir

ax.annotate('', xy=(4.2, 0), xytext=(-4.8, 0), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2.2))
ax.plot(0, 0, 'o', color=NAVY, markersize=8)
ax.text(4.3, -0.05, r'Axis / Initial Line', color=NAVY, fontweight='bold', fontsize=11)

# Directrix vertical line XM
ax.plot([x_dir, x_dir], [-2.8, 3.2], color=SLATE, lw=2.5)
ax.plot(x_dir, 0, 'o', color=SLATE, markersize=6)
ax.text(x_dir - 1.3, 2.9, r'Directrix $XM$', color=SLATE, fontweight='bold', fontsize=11)
ax.text(x_dir - 0.35, -0.35, r'$X$', color=SLATE, fontweight='bold', fontsize=11)

# Conic curve
th_conic = np.linspace(-np.deg2rad(115), np.deg2rad(115), 300)
r_conic = l / (1 + e * np.cos(th_conic))
xc = r_conic * np.cos(th_conic)
yc = r_conic * np.sin(th_conic)
ax.plot(xc, yc, color=TEAL, lw=2.8, label=r'Conic $\frac{l}{r} = 1 + e\cos\theta$')

# Semi-latus rectum SL
ax.plot([0, 0], [0, l], color=RED, lw=2.5)
ax.plot(0, l, 'o', color=RED, markersize=7)
ax.text(0.15, l/2 + 0.3, r'$SL = l$', color=RED, fontweight='bold', fontsize=11, ha='left', va='center')
ax.text(0.15, l + 0.15, r'$L(l, \pi/2)$', color=RED, fontweight='bold', fontsize=11)

# Point P(r, theta) for theta = 35 deg
th_P = np.deg2rad(35.0)
r_P = l / (1 + e * np.cos(th_P))
px = r_P * np.cos(th_P)
py = r_P * np.sin(th_P)

# Radius vector SP
ax.plot([0, px], [0, py], color=BLUE, lw=2.2)
ax.plot(px, py, 'o', color=BLUE, markersize=8)
ax.text(px + 0.15, py + 0.1, r'$P(r, \theta)$', color=BLUE, fontweight='bold', fontsize=12)
ax.text(px/2 - 0.15, py/2 + 0.25, r'$r$', color=BLUE, fontweight='bold', fontsize=11)

# Perpendicular PN to axis
ax.plot([px, px], [0, py], '--', color=SLATE, lw=1.8)
ax.plot(px, 0, 'o', color=SLATE, markersize=6)
ax.text(px, -0.4, r'$N$', color=SLATE, fontweight='bold', fontsize=11, ha='center')

# Perpendicular PM to directrix
ax.plot([x_dir, px], [py, py], '--', color=GOLD, lw=2)
ax.plot(x_dir, py, 'o', color=GOLD, markersize=6)
ax.text(x_dir - 0.45, py, r'$M$', color=GOLD, fontweight='bold', fontsize=11, va='center')
ax.text(x_dir/2, py + 0.3, r'$PM = SX + SN = \frac{l}{e} - r\cos\theta$', color=GOLD, fontweight='bold', fontsize=10, ha='center')

# Focus S label
ax.text(-0.15, -0.4, r'Focus $S$ (Pole)', color=NAVY, fontweight='bold', fontsize=11, ha='right')

# Double arrow for SX = l/e
ax.annotate('', xy=(0, -0.7), xytext=(x_dir, -0.7),
            arrowprops=dict(arrowstyle="<->", color=SLATE, lw=1.5))
ax.text(x_dir/2 - 0.4, -1.0, r'$SX = \frac{l}{e}$', color=SLATE, fontweight='bold', fontsize=10)

# Angle theta arc
arc_th = np.linspace(0, th_P, 50)
ax.plot(0.8 * np.cos(arc_th), 0.8 * np.sin(arc_th), color=BLUE, lw=1.8)
ax.text(0.95, 0.25, r'$\theta$', color=BLUE, fontweight='bold', fontsize=11)

ax.set_xlim(-5.2, 4.8)
ax.set_ylim(-2.6, 3.5)
ax.axis('off')
ax.set_title(r"Conic Focus-Directrix Projection: $\frac{l}{r} = 1 + e\cos\theta$", color=NAVY, fontweight='bold', pad=12)
plt.savefig(os.path.join(out_dir, "fig5_polar_conic_focus_directrix.pdf"))
plt.savefig(os.path.join(out_dir, "fig5_polar_conic_focus_directrix.png"))
plt.close()

# -------------------------------------------------------------
# Figure 6: Chord of a Conic PQ joining P(alpha - beta) and Q(alpha + beta)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.5, 5))
ax.set_aspect('equal')

e = 0.6
l = 2.2
alpha = np.deg2rad(35.0)
beta = np.deg2rad(38.0)

th_P = alpha - beta
th_Q = alpha + beta
r_P = l / (1 + e * np.cos(th_P))
r_Q = l / (1 + e * np.cos(th_Q))

px = r_P * np.cos(th_P)
py = r_P * np.sin(th_P)
qx = r_Q * np.cos(th_Q)
qy = r_Q * np.sin(th_Q)

# Draw full conic curve
th_c = np.linspace(-np.deg2rad(105), np.deg2rad(105), 300)
r_c = l / (1 + e * np.cos(th_c))
ax.plot(r_c * np.cos(th_c), r_c * np.sin(th_c), color=TEAL, lw=2.8, label=r'Conic $\frac{l}{r} = 1 + e\cos\theta$')

# Focus S
ax.annotate('', xy=(4.0, 0), xytext=(-0.8, 0), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2))
ax.plot(0, 0, 'o', color=NAVY, markersize=7)
ax.text(-0.35, -0.35, r'Focus $S$', color=NAVY, fontweight='bold', fontsize=11)
ax.text(4.1, -0.05, r'Initial Line', color=NAVY, fontweight='bold', fontsize=11)

# Radius vectors SP and SQ
ax.plot([0, px], [0, py], color=BLUE, lw=1.8)
ax.plot([0, qx], [0, qy], color=BLUE, lw=1.8)
ax.plot(px, py, 'o', color=BLUE, markersize=8)
ax.plot(qx, qy, 'o', color=BLUE, markersize=8)
ax.text(px + 0.15, py - 0.2, r'$P(r_1, \alpha - \beta)$', color=BLUE, fontweight='bold', fontsize=11)
ax.text(qx + 0.15, qy + 0.1, r'$Q(r_2, \alpha + \beta)$', color=BLUE, fontweight='bold', fontsize=11)

# True chord line passing through P and Q
ext_t = np.linspace(-0.25, 1.25, 50)
chord_x = px + ext_t * (qx - px)
chord_y = py + ext_t * (qy - py)
ax.plot(chord_x, chord_y, color=RED, lw=2.5, label='Chord $PQ$')
ax.text(chord_x[-1] + 0.1, chord_y[-1], r'Chord $PQ$', color=RED, fontweight='bold', fontsize=11)

# Angle bisector at angle alpha
bisect_len = 3.0
ax.plot([0, bisect_len * np.cos(alpha)], [0, bisect_len * np.sin(alpha)], '--', color=GOLD, lw=1.8)
ax.text(bisect_len * np.cos(alpha) + 0.1, bisect_len * np.sin(alpha), r'Bisector $\alpha$', color=GOLD, fontweight='bold', fontsize=10)

# Subtended angle 2 beta annotation
arc_sub = np.linspace(th_P, th_Q, 50)
ax.plot(1.2 * np.cos(arc_sub), 1.2 * np.sin(arc_sub), color=RED, lw=1.8)
ax.text(1.35, 0.6, r'$2\beta$', color=RED, fontweight='bold', fontsize=11)

ax.set_xlim(-0.8, 4.8)
ax.set_ylim(-2.0, 3.5)
ax.axis('off')
ax.set_title(r"Chord of a Conic: $\frac{l}{r} = e\cos\theta + \sec\beta\cos(\theta - \alpha)$", color=NAVY, fontweight='bold', pad=12)
plt.savefig(os.path.join(out_dir, "fig6_chord_of_conic.pdf"))
plt.savefig(os.path.join(out_dir, "fig6_chord_of_conic.png"))
plt.close()

# -------------------------------------------------------------
# Figure 7: Tangent and Normal to a Conic
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(6.5, 5))
ax.set_aspect('equal')

e = 0.6
l = 2.2
alpha = np.deg2rad(45.0)
r0 = l / (1 + e * np.cos(alpha))
px = r0 * np.cos(alpha)
py = r0 * np.sin(alpha)

# Draw full conic curve
th_c = np.linspace(-np.deg2rad(105), np.deg2rad(105), 300)
r_c = l / (1 + e * np.cos(th_c))
ax.plot(r_c * np.cos(th_c), r_c * np.sin(th_c), color=TEAL, lw=2.8, label=r'Conic $\frac{l}{r} = 1 + e\cos\theta$')

# Focus S
ax.annotate('', xy=(3.8, 0), xytext=(-0.8, 0), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2))
ax.plot(0, 0, 'o', color=NAVY, markersize=7)
ax.text(-0.35, -0.35, r'Focus $S$', color=NAVY, fontweight='bold', fontsize=11)
ax.text(3.9, -0.05, r'Initial Line', color=NAVY, fontweight='bold', fontsize=11)

# Point of contact P(r0, alpha)
ax.plot([0, px], [0, py], color=BLUE, lw=1.8)
ax.plot(px, py, 'o', color=BLUE, markersize=8)
ax.text(px + 0.35, py + 0.05, r'Point of Contact $P(r_0, \alpha)$', color=BLUE, fontweight='bold', fontsize=11)

# Exact Tangent line: (e + cos alpha) x + (sin alpha) y = l
nT_x = e + np.cos(alpha)
nT_y = np.sin(alpha)
norm_T = np.hypot(nT_x, nT_y)
vT_x = -nT_y / norm_T
vT_y = nT_x / norm_T

t_range = np.linspace(-2.2, 2.0, 50)
tangent_x = px + t_range * vT_x
tangent_y = py + t_range * vT_y
ax.plot(tangent_x, tangent_y, color=RED, lw=2.5, label='Tangent Line')
ax.text(tangent_x[0] - 0.2, tangent_y[0] + 0.15, r'Tangent $\frac{l}{r} = e\cos\theta + \cos(\theta - \alpha)$', color=RED, fontweight='bold', fontsize=10)

# Exact Normal line perpendicular to tangent at P
vN_x = nT_x / norm_T
vN_y = nT_y / norm_T
n_range = np.linspace(-1.5, 2.0, 50)
normal_x = px + n_range * vN_x
normal_y = py + n_range * vN_y
ax.plot(normal_x, normal_y, color=GOLD, lw=2.5, label='Normal Line')
ax.text(normal_x[-1] + 0.1, normal_y[-1], r'Normal Line', color=GOLD, fontweight='bold', fontsize=11)

# Right angle square between tangent and normal at P
sq_sz = 0.22
pt1 = np.array([px, py]) + sq_sz * np.array([vT_x, vT_y])
pt2 = pt1 + sq_sz * np.array([vN_x, vN_y])
pt3 = np.array([px, py]) + sq_sz * np.array([vN_x, vN_y])
ax.plot([pt1[0], pt2[0], pt3[0]], [pt1[1], pt2[1], pt3[1]], color=SLATE, lw=1.5)

ax.set_xlim(-0.8, 4.8)
ax.set_ylim(-1.8, 3.8)
ax.axis('off')
ax.set_title(r"Tangent and Normal to a Conic at Point of Contact $P(\alpha)$", color=NAVY, fontweight='bold', pad=12)
plt.savefig(os.path.join(out_dir, "fig7_tangent_and_normal.pdf"))
plt.savefig(os.path.join(out_dir, "fig7_tangent_and_normal.png"))
plt.close()

# -------------------------------------------------------------
# Figure 8: Chord of Contact of Tangents from an External Point A(r1, theta1)
# -------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7, 5.2))
ax.set_aspect('equal')

e = 0.6
l = 2.2

xA = 3.2
yA = 0.6
r1 = np.hypot(xA, yA)
theta1 = np.arctan2(yA, xA)

cos_beta = (l - e * xA) / r1
beta = np.arccos(cos_beta)

phi_P = theta1 - beta
phi_Q = theta1 + beta

r_P = l / (1 + e * np.cos(phi_P))
r_Q = l / (1 + e * np.cos(phi_Q))

px = r_P * np.cos(phi_P)
py = r_P * np.sin(phi_P)
qx = r_Q * np.cos(phi_Q)
qy = r_Q * np.sin(phi_Q)

# Draw full conic curve
th_c = np.linspace(-np.deg2rad(105), np.deg2rad(105), 300)
r_c = l / (1 + e * np.cos(th_c))
ax.plot(r_c * np.cos(th_c), r_c * np.sin(th_c), color=TEAL, lw=2.8, label=r'Conic $\frac{l}{r} = 1 + e\cos\theta$')

# Focus S
ax.annotate('', xy=(4.5, 0), xytext=(-0.8, 0), arrowprops=dict(arrowstyle="->", color=NAVY, lw=2))
ax.plot(0, 0, 'o', color=NAVY, markersize=7)
ax.text(-0.35, -0.35, r'Focus $S$', color=NAVY, fontweight='bold', fontsize=11)
ax.text(4.6, -0.05, r'Initial Line', color=NAVY, fontweight='bold', fontsize=11)

# External point A
ax.plot(xA, yA, 'o', color=RED, markersize=8)
ax.text(xA + 0.15, yA - 0.1, r'External Point $A(r_1, \theta_1)$', color=RED, fontweight='bold', fontsize=11)

# Contact points P and Q on the conic curve
ax.plot(px, py, 'o', color=BLUE, markersize=8)
ax.plot(qx, qy, 'o', color=BLUE, markersize=8)
ax.text(px + 0.15, py - 0.3, r'Contact Point $P(\alpha - \beta)$', color=BLUE, fontweight='bold', fontsize=11)
ax.text(qx - 1.2, qy + 0.2, r'Contact Point $Q(\alpha + \beta)$', color=BLUE, fontweight='bold', fontsize=11)

# True Tangent AP: segment from A through P and slightly beyond
t_AP = np.linspace(-0.25, 1.0, 50)
tan_AP_x = px + t_AP * (xA - px)
tan_AP_y = py + t_AP * (yA - py)
ax.plot(tan_AP_x, tan_AP_y, color=RED, lw=2.2, label='Tangent $AP$')

# True Tangent AQ: segment from A through Q and slightly beyond
t_AQ = np.linspace(-0.25, 1.0, 50)
tan_AQ_x = qx + t_AQ * (xA - qx)
tan_AQ_y = qy + t_AQ * (yA - qy)
ax.plot(tan_AQ_x, tan_AQ_y, color=RED, lw=2.2, label='Tangent $AQ$')

# True Chord of Contact PQ: straight line connecting contact points P and Q
ax.plot([px, qx], [py, qy], color=NAVY, lw=2.8, label='Chord of Contact $PQ$')
ax.text((px + qx)/2 - 1.5, (py + qy)/2, r'Chord of Contact $PQ$', color=NAVY, fontweight='bold', fontsize=11)

ax.set_xlim(-0.8, 5.2)
ax.set_ylim(-2.6, 3.5)
ax.axis('off')
ax.set_title(r"Chord of Contact of Tangents from External Point $A(r_1, \theta_1)$", color=NAVY, fontweight='bold', pad=12)
plt.savefig(os.path.join(out_dir, "fig8_chord_of_contact.pdf"))
plt.savefig(os.path.join(out_dir, "fig8_chord_of_contact.png"))
plt.close()

print("All 8 mathematical figures successfully regenerated in:", out_dir)
