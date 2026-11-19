"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#GroundTruthField``."""

from typing import Literal, TypeAlias, cast

"""<p>A reference field in a dataset example.</p>"""
GroundTruthField: TypeAlias = Literal[
    "expected_response",
    "expected_trajectory",
]


# --- restJson1 ser/de ---
def serialize_json(value: GroundTruthField) -> str:
    return value


def deserialize_json(data: str) -> GroundTruthField:
    return cast(GroundTruthField, data)
