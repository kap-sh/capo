"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#AttemptStatus``."""

from typing import Literal, TypeAlias, cast

"""How the most recent attempt at something ended. <p>`Status` rather than `State` because each of these describes the progress of a process — an edit, a hand-over to the delivery platform — rather than a resource's lifecycle. The resource's lifecycle is `State`, and it is a separate member. <p>Named for the attempt — *how did the last attempt at this end?* — and not for the thing attempted, so a second attempt axis can share it rather than copy it. <p>A member of this type is **omitted before the first attempt**: absence means "never tried", which is a third answer and not a fourth value."""
AttemptStatus: TypeAlias = Literal[
    "IN_PROGRESS",
    "SUCCEEDED",
    "FAILED",
]


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AttemptStatus) -> str:
    return value


def deserialize_cbor(data: str) -> AttemptStatus:
    return cast(AttemptStatus, data)
