"""Generated from Smithy shape ``com.amazonaws.supportauthz#SupportPermitStatus``."""

from typing import Literal, TypeAlias, cast

"""<p>The status of a support permit.</p>"""
SupportPermitStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "DELETING",
]


# --- restJson1 ser/de ---
def serialize_json(value: SupportPermitStatus) -> str:
    return value


def deserialize_json(data: str) -> SupportPermitStatus:
    return cast(SupportPermitStatus, data)
