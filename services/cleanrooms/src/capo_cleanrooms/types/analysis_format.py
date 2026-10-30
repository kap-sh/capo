"""Generated from Smithy shape ``com.amazonaws.cleanrooms#AnalysisFormat``."""

from typing import Literal, TypeAlias, cast

AnalysisFormat: TypeAlias = Literal[
    "SQL",
    "PYSPARK_1_0",
    "PYSPARK_2_0",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisFormat) -> str:
    return value


def deserialize_json(data: str) -> AnalysisFormat:
    return cast(AnalysisFormat, data)
