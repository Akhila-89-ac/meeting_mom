import os
import sys

from src.data_loaders.load_data import load_abstracts, load_publications
from src.preprocessing.cleaning import (
    clean_abstract,
    clean_instrument,
    deduplicate_pmids,
    filter_valid_entries,
)

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


def main() -> None:
    # Step 1: Load abstract map
    abstract_map = load_abstracts("data/raw/abstract_all.csv")

    # Step 2: Load and merge publication files
    publication_df = load_publications(
        [
            "data/raw/PublicationsData(in).csv",
            "data/raw/PublicationsData_update_04242025(in).csv",
        ]
    )

    # Step 3: Filter and deduplicate
    filtered_df = filter_valid_entries(publication_df)
    filtered_df = deduplicate_pmids(filtered_df)

    # Step 4: Enrich with abstract and clean instrument names
    filtered_df["raw_abstract"] = filtered_df["pmid"].apply(
        lambda x: abstract_map.get(str(x), "")
    )
    filtered_df["abstract"] = filtered_df["raw_abstract"].apply(clean_abstract)
    filtered_df["clean_instrument"] = filtered_df["Instrument"].apply(clean_instrument)

    # Step 5: Save to disk
    output_path = "data/processed/cleaned_zeiss_publications.csv"
    filtered_df.to_csv(output_path, index=False)
    print(f"[SUCCESS] Cleaned dataset written to: {output_path}")


if __name__ == "__main__":
    main()
