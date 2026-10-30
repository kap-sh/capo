"""Generated from Smithy shape ``com.amazonaws.continuum#FindingStatus``."""

from typing import Literal, TypeAlias, cast

"""The lifecycle status of a finding as it moves through Continuum's processing pipeline. CONFIRMED and DISCARDED are terminal states -- a CONFIRMED finding is promoted into a separate Issue (not yet implemented), which owns the subsequent remediation lifecycle; the finding's own status does not change after that."""
FindingStatus: TypeAlias = Literal[
    "SUBMITTED",
    "VALIDATING",
    "CONFIRMED",
    "DISCARDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: FindingStatus) -> str:
    return value


def deserialize_json(data: str) -> FindingStatus:
    return cast(FindingStatus, data)
