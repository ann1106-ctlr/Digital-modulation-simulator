import numpy as np
import matplotlib.pyplot as plt

# Digital Modulation Simulator
# Supports ASK, FSK and BPSK

# -----------------------------
# User Input
# -----------------------------

bits = input("Enter binary sequence (example: 101101): ")

while not all(bit in "01" for bit in bits):
    print("Invalid input! Enter only 0s and 1s.")
    bits = input("Enter binary sequence: ")

modulation = input("Enter modulation type (ASK/FSK/BPSK): ").upper()

while modulation not in ["ASK", "FSK", "BPSK"]:
    print("Invalid modulation type!")
    modulation = input("Enter ASK, FSK or BPSK: ").upper()

# Convert binary string to array
data = np.array([int(bit) for bit in bits])

# -----------------------------
# Parameters
# -----------------------------

bit_duration = 1
samples_per_bit = 100

fc = 5       # Carrier frequency
f1 = 8       # Frequency for bit 1
f0 = 3       # Frequency for bit 0

# Time axis
t = np.linspace(
    0,
    len(data) * bit_duration,
    len(data) * samples_per_bit,
    endpoint=False
)

# Repeat each bit over its duration
digital_signal = np.repeat(data, samples_per_bit)

# -----------------------------
# Carrier Signal
# -----------------------------

carrier = np.sin(2 * np.pi * fc * t)

# -----------------------------
# Modulation
# -----------------------------

if modulation == "ASK":

    # Amplitude Shift Keying
    modulated_signal = digital_signal * carrier

elif modulation == "FSK":

    # Frequency Shift Keying
    modulated_signal = np.zeros(len(t))

    for i, bit in enumerate(data):

        start = i * samples_per_bit
        end = (i + 1) * samples_per_bit

        if bit == 1:
            modulated_signal[start:end] = np.sin(
                2 * np.pi * f1 * t[start:end]
            )
        else:
            modulated_signal[start:end] = np.sin(
                2 * np.pi * f0 * t[start:end]
            )

elif modulation == "BPSK":

    # Binary Phase Shift Keying
    modulated_signal = np.zeros(len(t))

    for i, bit in enumerate(data):

        start = i * samples_per_bit
        end = (i + 1) * samples_per_bit

        if bit == 1:
            modulated_signal[start:end] = np.sin(
                2 * np.pi * fc * t[start:end]
            )
        else:
            modulated_signal[start:end] = np.sin(
                2 * np.pi * fc * t[start:end] + np.pi
            )

# -----------------------------
# Plot Signals
# -----------------------------

plt.figure(figsize=(12, 8))

# Input Signal
plt.subplot(3, 1, 1)
plt.plot(t, digital_signal)
plt.title("Input Digital Signal")
plt.ylabel("Bit")
plt.grid(True)

# Carrier Signal
plt.subplot(3, 1, 2)
plt.plot(t, carrier)
plt.title("Carrier Signal")
plt.ylabel("Amplitude")
plt.grid(True)

# Modulated Signal
plt.subplot(3, 1, 3)
plt.plot(t, modulated_signal)
plt.title(modulation + " Modulated Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()

# -----------------------------
# Display Results
# -----------------------------

print("\n-----------------------------")
print("DIGITAL MODULATION SIMULATOR")
print("-----------------------------")

print("Input Binary Data :", bits)
print("Modulation Type   :", modulation)

print("\nSimulation completed successfully!")