"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#FindingTargetType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of location in a session that a finding points to: a span ID, a trace ID, or a span name.</p>"""
FindingTargetType: TypeAlias = Literal[
    "SPAN_ID",
    "TRACE_ID",
    "SPAN_NAME",
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingTargetType) -> str:
    return value


def deserialize_json(data: str) -> FindingTargetType:
    return cast(FindingTargetType, data)
