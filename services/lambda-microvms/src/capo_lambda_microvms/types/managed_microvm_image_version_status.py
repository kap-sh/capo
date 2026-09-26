"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#ManagedMicrovmImageVersionStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The lifecycle status of a managed MicroVM image version.</p>"""
ManagedMicrovmImageVersionStatus: TypeAlias = Literal[
    "AVAILABLE",
    "DEPRECATED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ManagedMicrovmImageVersionStatus) -> str:
    return value


def deserialize_json(data: str) -> ManagedMicrovmImageVersionStatus:
    return cast(ManagedMicrovmImageVersionStatus, data)
