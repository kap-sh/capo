"""Generated from Smithy shape ``com.amazonaws.batch#EksAccessEntryDesiredState``."""

from typing import Literal, TypeAlias, cast

"""<p>The desired state for the Batch-managed Amazon EKS access entry on a compute environment.</p>"""
EksAccessEntryDesiredState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "INHERIT_FROM_CLUSTER",
]


# --- restJson1 ser/de ---
def serialize_json(value: EksAccessEntryDesiredState) -> str:
    return value


def deserialize_json(data: str) -> EksAccessEntryDesiredState:
    return cast(EksAccessEntryDesiredState, data)
