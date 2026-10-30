"""Generated from Smithy shape ``com.amazonaws.continuum#SignalBasis``."""

from typing import Literal, TypeAlias, cast

"""Where an assessed value came from, strongest evidence first. A customer weighing an assessment reads this to tell a fact read out of their own code from the producer's inference. The first three values name a source that states the value directly. The last two do not: INFERRED means the producer reasoned its way to the value, and NO_EVIDENCE_DEFAULT means it had nothing to reason from and used a default."""
SignalBasis: TypeAlias = Literal[
    "CODE",
    "GRAPH",
    "FINDING",
    "INFERRED",
    "NO_EVIDENCE_DEFAULT",
]


# --- restJson1 ser/de ---
def serialize_json(value: SignalBasis) -> str:
    return value


def deserialize_json(data: str) -> SignalBasis:
    return cast(SignalBasis, data)
