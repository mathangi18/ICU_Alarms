import os
import numpy as np
import pandas as pd
import wfdb
from tqdm import tqdm

# CONFIGURATION
WAVEFORM_ROOT = r"D:\waveforms"
OUTPUT_CSV = r"D:\waveforms\waveform_features.csv"

# FEATURE EXTRACTION FUNCTION
def extract_features(signal):
    signal = np.asarray(signal).flatten()

    return {
        "mean": np.mean(signal),
        "std": np.std(signal),
        "min": np.min(signal),
        "max": np.max(signal),
        "range": np.max(signal) - np.min(signal),
        "energy": np.sum(signal ** 2),
        "length": len(signal),
    }

# MAIN LOOP
rows = []

for record_id in tqdm(os.listdir(WAVEFORM_ROOT), desc="Processing records"):
    record_path = os.path.join(WAVEFORM_ROOT, record_id)

    if not os.path.isdir(record_path):
        continue

    for file in os.listdir(record_path):
        if file.endswith(".hea"):
            base_name = file.replace(".hea", "")
            record, event = base_name.split("_")

            try:
                signals, fields = wfdb.rdsamp(os.path.join(record_path, base_name))
            except Exception as e:
                continue  # skip unreadable files

            # If multiple channels exist, average them
            if signals.ndim > 1:
                signal = signals.mean(axis=1)
            else:
                signal = signals

            feats = extract_features(signal)
            feats["record"] = record
            feats["event"] = event

            rows.append(feats)

# SAVE FEATURES
df_features = pd.DataFrame(rows)
df_features.to_csv(OUTPUT_CSV, index=False)

print("Saved waveform features to:", OUTPUT_CSV)
print("Shape:", df_features.shape)
