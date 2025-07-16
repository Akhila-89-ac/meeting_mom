import re
from typing import Optional

from pandas import DataFrame


def clean_abstract(text: Optional[str]) -> str:
    """Normalize whitespace in abstracts."""
    return re.sub(r"\s+", " ", str(text)).strip()


def clean_instrument(instrument: Optional[str]) -> Optional[str]:
    """Map known instrument variants to canonical form."""
    if not isinstance(instrument, str):
        return instrument
    instrument = instrument.strip()
    mapping = {
        "LSM880": "LSM 990",
        "LSM 880": "LSM 990",
        "LSM880 NLO": "LSM 990",
        "LSM 880 NLO": "LSM 990",
        "LSM880NLO": "LSM 990",
        "LSM 880NLO": "LSM 990",
        "ZEN": "ZEN",
        "LSM 800": "LSM 910",
        "LSM800": "LSM 910",
        "LSM710": "LSM 990 with Airyscan 2",
        "LSM 700": "LSM 900 with Airyscan 2",
        "LSM 710": "LSM 900 with Airyscan 2",
        "LSM700": "LSM 900 with Airyscan 2",
        "LSM780": "LSM 990 with Airyscan 2",
        "LSM780NLO": "LSM 990 with Airyscan 2",
        "LSM780 NLO": "LSM 990 with Airyscan 2",
        "LSM 780 NLO": "LSM 990 with Airyscan 2",
        "LSM 780": "LSM 990 with Airyscan 2",
        "LSM900": "LSM 900",
        "LSM980": "LSM 990",
        "LSM 980 NLO": "LSM 990",
        "LSM 980": "LSM 990",
        "LSM980 NLO": "LSM 990",
        "ZEN Black": "ZEN",
        "ZEN Blue": "ZEN",
        "ZEN Lite": "ZEN",
        "ZENBlue": "ZEN",
        "ZEN black edition": "ZEN",
        "ZEN (black edition)": "ZEN",
        "ZENBlack": "ZEN",
        "ZENLite": "ZEN Lite",
        "ZEN Desk": "ZEN Desk",
        "Axiovision": "ZEN",
        "Auriga 40": "Crossbeam Family",
        "Auriga40": "Crossbeam Family",
        "Auriga Compact": "Crossbeam Family",
        "Auriga 60": "Crossbeam Family",
        "Auriga": "Crossbeam Family",
        "FIB SEM": "Crossbeam Family",
        "FIB-SEM": "Crossbeam Family",
        "FIBSEM": "Crossbeam Family",
        "Gemini 550": "GeminiSEM Family",
        "Gemini560": "GeminiSEM Family",
        "Gemini 560": "GeminiSEM Family",
        "Gemini 360": "GeminiSEM Family",
        "Gemini": "GeminiSEM Family",
        "Gemini 460": "GeminiSEM Family",
        "ORION Nanofab": "GeminiSEM Family",
        "Elyra PS . 1": "Elyra 7",
        "Elyra PS 1": "Elyra 7",
        "Elyra PS.1": "Elyra 7",
        "ELYRA P1": "Elyra 7",
        "ELYRA P 1": "Elyra 7",
        "ELYRA P . 1": "Elyra 7",
        "ELYRA P.1": "Elyra 7",
        "ELYRA S . 1": "Elyra 7",
        "ELYRA S 1": "Elyra 7",
        "ELYRA S.1": "Elyra 7",
        "ELYRA S1": "Elyra 7",
        "Elyra PS1": "Elyra 7",
        "Elyra 7": "Elyra 7",
        "ELYRA 7": "Elyra 7",
        "SUPRA55": "GeminiSEM Family",
        "SUPRA40": "GeminiSEM Family",
        "SUPRA25": "GeminiSEM Family",
        "SUPRA 25": "GeminiSEM Family",
        "SUPRA35": "GeminiSEM Family",
        "SUPRA60": "GeminiSEM Family",
        "SUPRA 40": "GeminiSEM Family",
        "SUPRA 35": "GeminiSEM Family",
        "SUPRA 55": "GeminiSEM Family",
        "SUPRA 50": "GeminiSEM Family",
        "SUPRA 60": "GeminiSEM Family",
        "ULTRA 60": "Xradia Ultra Series",
        "ULTRA60": "Xradia Ultra Series",
        "ULTRA 55": "Xradia Ultra Series",
        "ULTRA PLUS": "Xradia Ultra Series",
        "ULTRAPLUS": "Xradia Ultra Series",
        "ULTRA55": "Xradia Ultra Series",
        "Evo10": "Evo Family",
        "Evo15": "Evo Family",
        "Evo25": "Evo Family",
        "Evo 10": "Evo Family",
        "Evo 15": "Evo Family",
        "Evo 25": "Evo Family",
        "Evos": "Evo Family",
        "Cheetah EVO": "Evo Family",
        "Evo": "Evo Family",
        "Sigma": "Sigma Family",
        "arivis Cloud": "Arivis Cloud",
        "Lightsheet Z 1": "Lightsheet 7",
        "Lightsheet Z.1": "Lightsheet 7",
        "Lightsheet Z . 1": "Lightsheet 7",
        "Lightsheet Z1": "Lightsheet 7",
        "Lightsheet7": "Lightsheet 7",
        "Crossbeam 540": "Crossbeam Family",
        "Crossbeam540": "Crossbeam Family",
        "Crossbeam350": "Crossbeam Family",
        "Crossbeam 340": "Crossbeam Family",
        "Crossbeam 550 L": "Crossbeam Family",
        "Crossbeam 1540": "Crossbeam Family",
        "Crossbeam 550L": "Crossbeam Family",
        "Crossbeam550": "Crossbeam Family",
        "Crossbeam NVision 40": "Crossbeam Family",
        "Crossbeam 1540 EsB": "Crossbeam Family",
        "Crossbeam340": "Crossbeam Family",
        "NVision 40": "Crossbeam Family",
        "NVision40": "Crossbeam Family",
        "Crossbeam 550 cryo": "Crossbeam Family",
        "Crossbeam 550": "Crossbeam Family",
        "Crossbeam 350": "Crossbeam Family",
        "Neon40EsB": "Crossbeam Family",
        "Neon 40 EsB": "Crossbeam Family",
        "Neon 40EsB": "Crossbeam Family",
        "AxioObserver5": "AxioObserver 5",
        "AxioObserver 7": "AxioObserver 5",
        "Cell Observer SD": "AxioObserver 5",
        "CellObserver SD": "AxioObserver 5",
        "Stemi305": "Stemi 305",
        "Stemi508": "Stemi 508",
        "Axiovert A 1": "Axiovert 5",
        "AxiovertA1": "Axiovert 5",
        "Axiovert A1": "Axiovert 5",
        "Axiovert RL": "Axiovert 5",
        "SmartZoom5": "SmartZoom 5",
        "Axiolab5": "Axiolab 5",
        "Axioscope5": "Axioscope 5",
        "axioscan7": "axioscan 7",
        "axioscan": "axioscan 7",
        "axio scan 7": "axioscan 7",
        "AxioObserver7": "AxioObserver 5",
        "Airyscan2": "LSM 990 with Airyscan 2",
        "Airyscan": "LSM 900 with Airyscan 2",
        "Airyscan 2": "LSM 990 with Airyscan 2",
        "AxioZoom V 16": "AxioZoom V16",
        "AxioZoomV16": "AxioZoom V16",
        "AxioObserver3": "AxioObserver 5",
        "AxioObserver 3": "AxioObserver 5",
        "SmartZoom 5": "Axiolab 5",
        "SmartSEM": "SmartSEM",
        "Labscope": "LabScope",
        "Vision4D": "Arivis Pro",
        "Vision 4D": "Arivis Pro",
        "Smartproof 5": "SmartZoom 5",
        "Smartproof5": "SmartZoom 5",
        "ZENCore": "ZEN Core",
        "ZEN core": "ZEN Core",
        "ZEN Core": "ZEN Core",
        "arivis Pro": "Arivis Pro",
        "ART": "ART",
        "Dragonfly": "Dragonfly",
        "Scout-and-Scan": "Scout-and-Scan",
        "Scout and Scan": "Scout-and-Scan",
        "arivis": "Arivis",
        "Sigma360": "Sigma Family",
        "Sigma 360": "Sigma Family",
        "Sigma": "Sigma Family",
        "Lattice Lightsheet": "Lattice Lightsheet 7",
        "LSM7 MP": "LSM 900",
        "LSM7MP": "LSM 900",
        "LSM 7MP": "LSM 900",
        "LSM 7 MP": "LSM 900",
    }
    return mapping.get(instrument, instrument)


def filter_valid_entries(df: DataFrame) -> DataFrame:
    """Drop rows with missing fields and Zeiss-only records with numeric PMIDs."""
    print(f"[INFO] Starting filter: {df.shape[0]} rows")
    df = df.dropna(
        subset=[
            "articleTitle",
            "Instrument",
            "Category",
            "sciLeadsSuperResearcherId",
            "Classification 1",
        ]
    )
    df["pmid"] = df["pmid"].astype(str)
    df = df[df["pmid"].str.isnumeric()]
    df = df[df["Company"].str.lower() == "zeiss"]
    print(f"[INFO] Filtered to {df.shape[0]} valid Zeiss entries.")
    return df


def deduplicate_pmids(df: DataFrame) -> DataFrame:
    """Ensure unique publication entries by PMID."""
    before = df.shape[0]
    df = df.drop_duplicates(subset="pmid")
    after = df.shape[0]
    print(f"[INFO] Removed {before - after} duplicate PMIDs. Final: {after}")
    return df
