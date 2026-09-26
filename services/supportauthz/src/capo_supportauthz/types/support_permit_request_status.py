"""Generated from Smithy shape ``com.amazonaws.supportauthz#SupportPermitRequestStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a support permit request.</p>"""
SupportPermitRequestStatus: TypeAlias = Literal[
    "PENDING",
    "ACCEPTED",
    "REJECTED",
    "CANCELLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SupportPermitRequestStatus) -> str:
    return value


def deserialize_json(data: str) -> SupportPermitRequestStatus:
    return cast(SupportPermitRequestStatus, data)
