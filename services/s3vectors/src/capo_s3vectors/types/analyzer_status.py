"""Generated from Smithy shape ``com.amazonaws.s3vectors#AnalyzerStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The backfill status of a text search analyzer.</p>"""
AnalyzerStatus: TypeAlias = Literal[
    "ACTIVE",
    "BUILDING",
]


# --- restJson1 ser/de ---
def serialize_json(value: AnalyzerStatus) -> str:
    return value


def deserialize_json(data: str) -> AnalyzerStatus:
    return cast(AnalyzerStatus, data)
