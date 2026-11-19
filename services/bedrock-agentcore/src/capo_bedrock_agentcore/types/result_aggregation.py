"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ResultAggregation``."""

from typing import Literal, TypeAlias, cast

"""<p>How to combine per-trace or per-span evaluation results into one result for the session.</p>"""
ResultAggregation: TypeAlias = Literal[
    "Min",
    "Max",
    "Mean",
    "AllMatch",
    "AnyMatch",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResultAggregation) -> str:
    return value


def deserialize_json(data: str) -> ResultAggregation:
    return cast(ResultAggregation, data)
