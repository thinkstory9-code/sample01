"""Original generative composition: '숨 고르기 (Room to Breathe)'.

Written for this booklet; pitch/rhythm arrangement and all sound waves are
created here from basic mathematical oscillators, envelopes and deterministic
noise. No external recordings, licensed samples, loops, or melodies are used.

Requirements to regenerate WAV: python, numpy, soundfile. To create MP3 as
included with the website: ffmpeg -i room-to-breathe.wav -codec:a libmp3lame
-q:a 4 room-to-breathe.mp3
"""

from pathlib import Path
import math
import numpy as np
import soundfile as sf

SAMPLE_RATE = 32000
BPM = 68
BEAT = 60 / BPM
BARS = 24
BAR = 4 * BEAT
LENGTH = BARS * BAR
N = round(LENGTH * SAMPLE_RATE)
RNG = np.random.default_rng(62026)

# Distinctive four-bar harmonic movement explored across six variations.
# Each entry is (bass, arpeggio tones, warm ambient tones).
CHORDS = [
    ('G2', ['G3', 'B3', 'D4', 'F#4', 'A4'], ['G3', 'D4', 'F#4']),
    ('F#2', ['F#3', 'A3', 'D4', 'E4'], ['F#3', 'A3', 'D4']),
    ('E2', ['E3', 'G3', 'B3', 'F#4'], ['E3', 'B3', 'F#4']),
    ('A2', ['A3', 'D4', 'E4', 'G4'], ['A3', 'D4', 'G4']),
    ('B2', ['B3', 'D4', 'F#4', 'A4'], ['B3', 'D4', 'A4']),
    ('G2', ['G3', 'B3', 'D4', 'F#4', 'A4'], ['G3', 'B3', 'F#4']),
    ('D2', ['D3', 'F#3', 'A3', 'E4'], ['D3', 'A3', 'E4']),
    ('C#3', ['C#4', 'E4', 'A4', 'B4'], ['C#4', 'E4', 'A4']),
    ('G2', ['G3', 'B3', 'D4', 'F#4'], ['G3', 'D4', 'F#4']),
    ('F#2', ['F#3', 'A3', 'C#4', 'E4'], ['F#3', 'C#4', 'E4']),
    ('E2', ['E3', 'G3', 'B3', 'D4', 'F#4'], ['E3', 'B3', 'F#4']),
    ('A2', ['A3', 'D4', 'E4', 'G4'], ['A3', 'D4', 'G4']),
    ('D2', ['D3', 'F#3', 'A3', 'C#4', 'E4'], ['D3', 'A3', 'C#4']),
    ('F#2', ['F#3', 'A3', 'C#4', 'E4'], ['F#3', 'C#4', 'E4']),
    ('G2', ['G3', 'B3', 'D4', 'F#4', 'A4'], ['G3', 'D4', 'F#4']),
    ('A2', ['A3', 'C#4', 'E4', 'B4'], ['A3', 'E4', 'B4']),
    ('B2', ['B3', 'D4', 'E4', 'F#4', 'A4'], ['B3', 'D4', 'E4']),
    ('G2', ['G3', 'B3', 'D4', 'F#4'], ['G3', 'B3', 'F#4']),
    ('F#2', ['F#3', 'A3', 'D4', 'E4'], ['F#3', 'A3', 'D4']),
    ('A2', ['A3', 'C#4', 'E4', 'B4'], ['A3', 'E4', 'B4']),
    ('G2', ['G3', 'B3', 'D4', 'F#4', 'A4'], ['G3', 'D4', 'A4']),
    ('D2', ['D3', 'F#3', 'A3', 'E4'], ['D3', 'A3', 'E4']),
    ('E2', ['E3', 'G3', 'B3', 'F#4'], ['E3', 'B3', 'F#4']),
    ('A2', ['A3', 'D4', 'E4', 'G4'], ['A3', 'D4', 'G4']),
]

# Every note of this melody was composed specifically for the page.
# (beat offset, pitch, duration in beats) for each four-beat bar.
MELODY = [
    [(1.0, 'A4', .85), (2.15, 'B4', .85), (3.25, 'F#4', .55)],
    [(.7, 'F#4', 1.1), (2.3, 'E4', 1.2)],
    [(1.0, 'G4', .8), (2.12, 'B4', .8), (3.2, 'A4', .6)],
    [(1.2, 'A4', 1.65)],
    [(.65, 'F#4', .7), (1.72, 'D5', 1.2), (3.2, 'C#5', .55)],
    [(.75, 'B4', .9), (2.15, 'A4', .9)],
    [(1, 'F#4', .82), (2.2, 'E4', .67), (3.2, 'F#4', .58)],
    [(1, 'E4', 2)],
    [(.72, 'D5', 1.18), (2.32, 'B4', 1.07)],
    [(1.22, 'C#5', .82), (2.27, 'B4', 1.12)],
    [(.82, 'G4', 1.25), (2.43, 'F#4', 1.05)],
    [(.66, 'E4', .72), (1.65, 'A4', 1.38)],
    [(.63, 'F#4', .77), (1.76, 'A4', .8), (2.82, 'E5', 1.05)],
    [(1.18, 'C#5', 1.13), (2.79, 'A4', .85)],
    [(.82, 'B4', .85), (2.03, 'D5', 1.48)],
    [(1.0, 'C#5', .8), (2.13, 'B4', .86)],
    [(.76, 'A4', 1.08), (2.25, 'F#4', 1.12)],
    [(.91, 'B4', .87), (2.22, 'D5', .99)],
    [(.72, 'A4', .75), (2.02, 'F#4', 1.38)],
    [(1.3, 'E4', 1.75)],
    [(.8, 'G4', .86), (2.03, 'A4', .9), (3.08, 'B4', .72)],
    [(.78, 'A4', .88), (2.02, 'F#4', 1.12)],
    [(1.1, 'G4', .82), (2.41, 'E4', 1.12)],
    [(1.23, 'E4', 1.48), (3.3, 'F#4', .54)],
]

PITCHES = {'C': 0, 'C#': 1, 'D': 2, 'D#': 3, 'E': 4, 'F': 5, 'F#': 6,
           'G': 7, 'G#': 8, 'A': 9, 'A#': 10, 'B': 11}


def freq(note):
    name, octave = note[:-1], int(note[-1])
    midi = (octave + 1) * 12 + PITCHES[name]
    return 440.0 * 2 ** ((midi - 69) / 12)


def soft_key(note, duration, velocity=0.5):
    """Synthesized muted piano, no soundfont / external samples."""
    f = freq(note)
    length = min(duration + 3.7, 6.5)
    t = np.arange(round(length * SAMPLE_RATE), dtype=np.float32) / SAMPLE_RATE
    piano = np.zeros_like(t)
    # Mild detuning of upper strings gives acoustic-style natural warmth.
    for i, weight in enumerate((1, .32, .115, .043, .014), start=1):
        inharm = i * math.sqrt(1 + .00031 * i * i)
        phase = 0.19 * i
        fall = (1.35 + 3.7 / (i ** .9)) * (440 / max(f, 130)) ** .18
        piano += weight * np.sin(2 * np.pi * f * inharm * t + phase) * np.exp(-t / fall)
    # Felt damping + a near-silent, low-passed synthetic hammer transient.
    env = (1 - np.exp(-t * 120)) * np.where(t < duration, 1.0, np.exp(-(t - duration) / .68))
    piano *= env * (0.20 * velocity)
    transient_len = min(len(t), round(.05 * SAMPLE_RATE))
    noise = RNG.standard_normal(transient_len).astype(np.float32)
    noise = np.convolve(noise, np.ones(12) / 12, mode='same')
    piano[:transient_len] += noise * np.exp(-np.arange(transient_len) / (SAMPLE_RATE * .012)) * (.004 * velocity)
    return piano


def glow(note, duration, velocity=.15):
    """Gentle synthetic pad, sculpted from detuned sine waves."""
    f = freq(note)
    length = duration + 3.4
    t = np.arange(round(length * SAMPLE_RATE), dtype=np.float32) / SAMPLE_RATE
    result = np.zeros_like(t)
    for detune, gain in ((-.0018, .42), (0, .50), (.0016, .42)):
        result += gain * np.sin(2 * np.pi * f * (1 + detune) * t)
    result += .16 * np.sin(2 * np.pi * f * 2.001 * t)
    a = (1 - np.exp(-t / 1.0))
    r = np.where(t < duration, 1., np.exp(-(t - duration) / 2.2))
    pulse = .90 + .10 * np.sin(2 * np.pi * .12 * t + f / 90)
    return result * a * r * pulse * (.058 * velocity)


def add_periodic(buf, waveform, start_time, gain_l=1, gain_r=1):
    ix = int(round(start_time * SAMPLE_RATE)) % N
    length = len(waveform)
    pos = 0
    while pos < length:
        count = min(length - pos, N - ix)
        buf[ix: ix+count, 0] += waveform[pos:pos+count] * gain_l
        buf[ix: ix+count, 1] += waveform[pos:pos+count] * gain_r
        pos += count
        ix = 0


def main():
    # Circular synthesis means the tail of bar 24 carries smoothly into bar 1.
    mix = np.zeros((N, 2), dtype=np.float32)
    for bar_index, ((bass, arp, pad), melody) in enumerate(zip(CHORDS, MELODY)):
        begin = bar_index * BAR
        movement = (bar_index // 4) % 3
        # One soft, low root at the beginning of each measure.
        add_periodic(mix, soft_key(bass, 2.65 * BEAT, .41), begin, .96, .89)
        arpeggios = [0, 1.5, 2.45, 3.4]
        order = [0, 2, 1, 3] if bar_index % 2 else [0, 1, 3, 2]
        for j, beat in enumerate(arpeggios):
            note = arp[order[j] % len(arp)]
            level = .39 + (.045 if j == 0 else 0) + .01 * movement
            soft = soft_key(note, .8 * BEAT, level)
            pan = .15 + (j / 3) * .68
            add_periodic(mix, soft, begin + beat * BEAT, 1.1 - .34 * pan, .73 + .34 * pan)
        # Chord bed played quietly beneath piano.
        for j, note in enumerate(pad):
            warm = glow(note, 3.5 * BEAT, .21 if j == 0 else .17)
            add_periodic(mix, warm, begin + .05 * BEAT, .89 + .15 * j, 1.16 - .13 * j)
        for j, (beat, note, dur) in enumerate(melody):
            vel = .51 + .035 * ((bar_index + j) % 3)
            voice = soft_key(note, dur * BEAT, vel)
            add_periodic(mix, voice, begin + beat * BEAT, .90, 1.06)

    # Original, synthesised reverb with different diffuse timings per channel.
    # Circular echo preserves continuity at loop boundaries.
    dry = mix.copy()
    for sec, level in ((.14, .10), (.23, .085), (.37, .075), (.53, .060),
                       (.71, .055), (.94, .038), (1.3, .025), (1.73, .017)):
        offset = round(sec * SAMPLE_RATE)
        mix[:,0] += np.roll(dry[:,1], offset) * level
        mix[:,1] += np.roll(dry[:,0], offset + 187) * level

    # Gentle tanh soft limiting. Quiet, non-distracting level for background use.
    mix = np.tanh(mix * 1.45)
    peak = float(np.max(np.abs(mix)))
    mix *= (.80 / max(peak, 1e-7))
    print(f'length: {LENGTH:.2f}s, sample rate: {SAMPLE_RATE}Hz')
    print(f'peak: {np.max(np.abs(mix)):.3f}, rms: {np.sqrt(np.mean(mix ** 2)):.3f}')
    out = Path(__file__).resolve().parent / 'room-to-breathe.wav'
    sf.write(out, mix, SAMPLE_RATE, subtype='PCM_16')
    print('saved:', out)

if __name__ == '__main__':
    main()
