"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#TrafficSplitStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a traffic shift.</p>"""
TrafficSplitStatus: TypeAlias = Literal[
    "InProgress",
    "Completed",
    "Failed",
]


# --- restJson1 ser/de ---
def serialize_json(value: TrafficSplitStatus) -> str:
    return value


def deserialize_json(data: str) -> TrafficSplitStatus:
    return cast(TrafficSplitStatus, data)
