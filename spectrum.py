"""
Spectral analysis functions.
"""

import numpy as np
from scipy.signal import detrend


def binavg(x: np.ndarray, binsize: int) -> np.ndarray:
    """Bin-average over binsize elements.

    Parameters
    ----------
    x : np.ndarray
        Input array.
    binsize : int
        Number of elements to average over.

    Returns
    -------
    np.ndarray
        The binned average of x.
    """
    return np.array([np.mean(x[n : n + binsize]) for n in range(0, len(x), binsize)])


def blackman_harris(n: int) -> np.ndarray:
    """Return the n-point Blackman-Harris window.

    Parameters
    ----------
    n : int
        Number of points in the output window.

    Returns
    -------
    np.ndarray
        The output of the Blackman-Harris window function.
    """
    x = np.linspace(0, 2 * np.pi, n, endpoint=False)
    p = [0.35875, -0.48829, 0.14128, -0.01168]
    res = np.zeros((n))
    for i in range(4):
        res += p[i] * np.cos(i * x)
    return res


def filter_by_frequency(
    x: np.ndarray, dt: float, fmin: float = None, fmax: float = None
) -> np.ndarray:
    """Filter x in frequency space.

    Parameters
    ----------
    x : np.ndarray
        Input array.
    dt : float
        Time step.
    fmin : float, optional
        Minimum frequency, by default None
    fmax : float, optional
        Maximum frequency, by default None

    Returns
    -------
    np.ndarray
        Filtered x with energy excluded from f < fmin and f > fmax.
    """
    f = np.fft.fftfreq(x.shape[-1], dt)
    s = np.fft.fft(x)
    if fmin:
        s = np.where((f < fmin) & (f > -fmin), 0, s)
    if fmax:
        s = np.where((f > fmax) | (f < -fmax), 0, s)
    return np.fft.ifft(s).real.astype(x.dtype)


def integrate_by_frequency(
    x: np.ndarray, dt: float, fmin: float = None, fmax: float = None
) -> np.ndarray:
    """Integrate x in frequency space.

    Parameters
    ----------
    x : np.ndarray
        Input array.
    dt : float
        Time step.
    fmin : float, optional
        Minimum frequency, by default None
    fmax : float, optional
        Maximum frequency, by default None

    Returns
    -------
    np.ndarray
        The integral of x.
    """
    f = np.fft.fftfreq(x.shape[-1], dt)
    s = np.fft.fft(x)
    s[..., 1:] /= 1j * 2 * np.pi * f[1:]
    if fmin:
        s = np.where((f < fmin) & (f > -fmin), 0, s)
    if fmax:
        s = np.where((f > fmax) | (f < -fmax), 0, s)
    return np.fft.ifft(s).real.astype(x.dtype)


def power_spectrum(
    x: np.ndarray, dt: float, binsize: int = 1
) -> tuple[np.ndarray, np.ndarray]:
    """Return the power spectrum of x with a sampling interval dt, with the
    Blackman-Harris window filter applied on the edges.

    Optionally, average over binsize if provided.

    Parameters
    ----------
    x : np.ndarray
        Input array.
    dt : float
        Time step.
    binsize : int, optional
        Number of elements to average over, by default 1.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        The power spectrum and the corresponding frequencies.
    """

    N = x.size
    window = blackman_harris(N)
    Sx = np.fft.fft(window * detrend(x))[: N // 2]
    C = dt / (np.pi * np.sum(window**2))
    df = 2 * np.pi / (dt * N)
    f = np.array([i * df for i in range(N // 2)]) / (2 * np.pi)

    if binsize > 1:
        Sxx = 2 * np.pi * C * binavg(np.abs(Sx) ** 2, binsize)
        f = binavg(f, binsize)
        df *= binsize
    else:
        Sxx = 2 * np.pi * C * np.abs(Sx) ** 2

    return Sxx.astype(np.float32), f.astype(np.float32)


def cross_spectrum(
    x: np.ndarray,
    y: np.ndarray,
    dt: float,
    binsize: int = 1,
    return_complex: bool = True,
) -> tuple:
    """Return the power spectrum of x with a sampling interval dt, with the
    Blackman-Harris window filter applied on the edges.

    Optionally, average over binsize if provided.

    Parameters
    ----------
    x : np.ndarray
        First input array.
    y : np.ndarray
        Second input array.
    dt : float
        Time step.
    binsize : int, optional
        Number of elements to average over, by default 1.
    return_complex : bool, optional
        Return the complex cross spectrum, by default True; otherwise, return
        only the real component.

    Returns
    -------
    tuple
        A tuple of NumPy arrays of Sxx, Syy, Sxy, phase, coherence, and frequency
    """

    N = x.size
    window = blackman_harris(N)
    Sx = np.fft.fft(window * detrend(x))[: N // 2]
    Sy = np.fft.fft(window * detrend(y))[: N // 2]
    df = 2 * np.pi / (dt * N)
    f = np.array([i * df for i in range(N // 2)]) / (2 * np.pi)
    C = dt / (np.pi * np.sum(window**2))

    if binsize > 1:
        Sxx = 2 * np.pi * C * binavg(np.abs(Sx) ** 2, binsize)
        Syy = 2 * np.pi * C * binavg(np.abs(Sy) ** 2, binsize)
        Sxy = 2 * np.pi * C * binavg(np.conj(Sx) * Sy, binsize)
        f = binavg(f, binsize)
        df *= binsize
    else:
        Sxx = 2 * np.pi * C * np.abs(Sx) ** 2
        Syy = 2 * np.pi * C * np.abs(Sy) ** 2
        Sxy = 2 * np.pi * C * np.conj(Sx) * Sy

    phase = np.arctan2(-np.imag(Sxy), np.real(Sxy))
    coherence = np.abs(Sxy / np.sqrt(Sxx * Syy))

    if return_complex:
        return (
            Sxx.astype(np.complex64),
            Syy.astype(np.complex64),
            Sxy.astype(np.complex64),
            phase.astype(np.complex64),
            coherence.astype(np.complex64),
            f.astype(np.float32),
        )
    else:
        return (
            Sxx.astype(np.float32),
            Syy.astype(np.float32),
            Sxy.astype(np.float32),
            phase.astype(np.float32),
            coherence.astype(np.float32),
            f.astype(np.float32),
        )
