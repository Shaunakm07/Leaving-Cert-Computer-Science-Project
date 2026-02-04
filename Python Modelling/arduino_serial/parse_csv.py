import pandas as pd
import re

INPUT_CSV = "serial_cleaned_data.csv"
OUTPUT_CSV = "serial_parsed_only.csv"

NUM = r"([-+]?\d*\.?\d+)"  # matches 0, 21.40, .5, -3.2

PATTERNS = {
    # tolerate corrupted "Moisture" like "oisture"
    "moisture": re.compile(rf"(?i)\b(?:current\s+)?(?:m+)?oisture\s*:\s*{NUM}\b"),
    "temperature": re.compile(rf"(?i)\b(?:current\s+)?temperature\s*:\s*{NUM}\b"),
    "humidity": re.compile(rf"(?i)\b(?:current\s+)?humidity\s*:\s*{NUM}\b"),
}

def normalize_text(s: str) -> str:
    s = str(s).replace("\t", " ")
    s = re.sub(r"\s+", " ", s).strip()
    return s

def extract(pattern, s: str):
    m = pattern.search(s)
    return float(m.group(1)) if m else None

# Load
df = pd.read_csv(INPUT_CSV)

# Parse from cleaned_data
text = df["cleaned_data"].apply(normalize_text)

df["moisture"] = text.apply(lambda s: extract(PATTERNS["moisture"], s))
df["temperature"] = text.apply(lambda s: extract(PATTERNS["temperature"], s))
df["humidity"] = text.apply(lambda s: extract(PATTERNS["humidity"], s))

# Keep only timestamp + parsed columns (drop original data)
out = df[["timestamp", "moisture", "temperature", "humidity"]].copy()

# Optional: drop rows where parsing failed
out = out.dropna(subset=["moisture", "temperature", "humidity"])

# Save
out.to_csv(OUTPUT_CSV, index=False)

print(f"Saved parsed-only CSV to: {OUTPUT_CSV}")
print(out.head())
