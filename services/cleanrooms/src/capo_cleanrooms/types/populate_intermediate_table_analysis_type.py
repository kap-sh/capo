"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PopulateIntermediateTableAnalysisType``."""

from typing import Literal, TypeAlias, cast

PopulateIntermediateTableAnalysisType: TypeAlias = Literal[
    "QUERY",
    "JOB",
]


# --- restJson1 ser/de ---
def serialize_json(value: PopulateIntermediateTableAnalysisType) -> str:
    return value


def deserialize_json(data: str) -> PopulateIntermediateTableAnalysisType:
    return cast(PopulateIntermediateTableAnalysisType, data)
