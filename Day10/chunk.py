from datasets import load_dataset
import pandas as pd

ds = load_dataset("phihung/titanic", split="train", streaming=True)

chunk_size = 100
batch = []

for i, example in enumerate(ds):
    batch.append(example)

    if (i + 1) % chunk_size == 0:
        df_chunk = pd.DataFrame(batch)
        print(f"Processing chunk {i // chunk_size + 1}")
        print(df_chunk.head())
        batch = []
