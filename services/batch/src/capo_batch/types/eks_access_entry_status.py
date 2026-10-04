"""Generated from Smithy shape ``com.amazonaws.batch#EksAccessEntryStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The observed state of the Batch-managed Amazon EKS access entry on a compute environment.</p>"""
EksAccessEntryStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: EksAccessEntryStatus) -> str:
    return value


def deserialize_json(data: str) -> EksAccessEntryStatus:
    return cast(EksAccessEntryStatus, data)
