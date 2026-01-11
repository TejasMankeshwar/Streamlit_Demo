import streamlit as st
import numpy as np
from typing import Any

# Sidebar controls
iterations = st.sidebar.slider("Level of detail", 2, 20, 10, 1)
separation = st.sidebar.slider("Separation", 0.7, 2.0, 0.7885)

progress_bar = st.sidebar.progress(0)
frame_text = st.sidebar.empty()
image = st.empty()

# Grid setup
m, n, scale = 960, 640, 400
x = np.linspace(-m / scale, m / scale, num=m).reshape((1, m))
y = np.linspace(-n / scale, n / scale, num=n).reshape((n, 1))

# Animation loop
for frame_num, a in enumerate(np.linspace(0.0, 4 * np.pi, 100)):
    progress_bar.progress(frame_num)
    frame_text.text(f"Frame {frame_num+1}/100")

    # Complex plane setup
    c = separation * np.exp(1j * a)
    Z = np.tile(x, (n, 1)) + 1j * np.tile(y, (1, m))
    C = np.full((n, m), c)
    M: Any = np.full((n, m), True, dtype=bool)
    N = np.zeros((n, m))

    # Mandelbrot iterations
    for i in range(iterations):
        Z[M] = Z[M] * Z[M] + C[M]
        escaped = np.abs(Z) > 2
        N[escaped & M] = i
        M[escaped] = False

    # Display image
    image.image(1.0 - (N / N.max()), use_column_width=True)


# Cleanup UI elements
progress_bar.empty()
frame_text.empty()

st.button("Re-run")
