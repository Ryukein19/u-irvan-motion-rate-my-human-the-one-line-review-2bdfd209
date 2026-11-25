import os
# One-liner entry (105 chars): the line below is the whole submission.
# Writes to /output/entry.txt.
LINE = "Five stars, but he docks one every time I ask a question, then wonders why I never ask questions anymore."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
