import numpy as np

# Waveform Generation Functions
def generate_waveforms(t):
    """Generates standard waveforms for a given time vector."""
    sine = np.sin(2 * np.pi * t)
    square = np.sign(np.sin(2 * np.pi * t))
    triangular = 2 * np.abs(2 * (t - np.floor(t + 0.5))) - 1
    complex_wave = (
        0.6 * np.sin(2 * np.pi * t) +  # Fundamental frequency
        0.3 * np.sin(2 * np.pi * 3 * t) +  # 3rd harmonic
        0.1 * np.sin(2 * np.pi * 5 * t)    # 5th harmonic
    )
    return {"Sine": sine, "Square": square, "Triangular": triangular, "Complex": complex_wave}

def compute_gaussian(a):
    """Generates a Gaussian function for a given parameter a."""
    x = np.linspace(-2, 2, 101)
    f = np.exp(-np.pi * a * x**2)
    return x, f

def compute_fourier_transform(wave, t=None, a=None):
    """Computes the Fourier transform of a waveform or Gaussian."""
    if t is not None:  # Fourier Transform of a waveform
        fft = np.fft.fft(wave)
        freqs = np.fft.fftfreq(len(t), d=(t[1] - t[0]))
        return freqs, np.abs(fft)
    if a is not None:  # Fourier Transform of a Gaussian
        y = np.linspace(-2, 2, 101)
        fhat = a**(-1/2) * np.exp(-np.pi / a * y**2)
        return y, fhat

# Annotation Utility
def make_annotations(a, upper_title, lower_title):
    """Creates annotations for interactive plots."""
    return [
        dict(text=f'{upper_title} with a={a:.2f}', xref="paper", yref="paper",
             showarrow=False, x=0.5, y=1.05, font=dict(size=14)),
        dict(text=f'{lower_title} with a={a:.2f}', xref="paper", yref="paper",
             showarrow=False, x=0.5, y=0.45, font=dict(size=14))
    ]

# Slider Utility
def create_slider_steps(a_values, gaussians, fourier_transforms, upper_title, lower_title):
    """Generates slider steps for interactive plots."""
    return [
        dict(
            method="update",
            args=[
                {"x": [gaussians[i][0], fourier_transforms[i][0]],
                 "y": [gaussians[i][1], fourier_transforms[i][1]]},
                {"annotations": make_annotations(a, upper_title, lower_title)}
            ],
            label=f'{a:.1f}'
        )
        for i, a in enumerate(a_values)
    ]
