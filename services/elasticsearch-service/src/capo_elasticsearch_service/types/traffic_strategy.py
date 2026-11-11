"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#TrafficStrategy``."""

from typing import Literal, TypeAlias, cast

"""<p>The strategy used to shift traffic between the primary and cloned clusters.</p>"""
TrafficStrategy: TypeAlias = Literal["ShiftReadTrafficPercent",]


# --- restJson1 ser/de ---
def serialize_json(value: TrafficStrategy) -> str:
    return value


def deserialize_json(data: str) -> TrafficStrategy:
    return cast(TrafficStrategy, data)
