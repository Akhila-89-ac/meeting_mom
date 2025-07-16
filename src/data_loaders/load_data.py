from typing import Dict, List

import pandas as pd


def load_abstracts(path: str) -> Dict[str, str]:
    """Load abstract data and map PMID to abstract text."""
    try:
        df = pd.read_csv(path)
        df = df.rename(columns={"PMID": "pmid", "Abstract": "abstract"})
        abstract_map = dict(zip(df["pmid"].astype(str), df["abstract"]))
        print(f"[INFO] Loaded {len(abstract_map)} abstract entries.")
        return abstract_map
    except Exception as e:
        print(f"[ERROR] Failed to load abstracts: {e}")
        raise


def load_publications(paths: List[str]) -> pd.DataFrame:
    """Load multiple publication files and concatenate them."""
    try:
        dfs = [pd.read_csv(p, low_memory=False) for p in paths]
        merged_df = pd.concat(dfs, axis=0, ignore_index=True)
        row_count = merged_df.shape[0]
        file_count = len(paths)
        print(f"[INFO] Loaded {row_count} publication rows from {file_count} files.")

        return merged_df
    except Exception as e:
        print(f"[ERROR] Failed to load publication files: {e}")
        raise
