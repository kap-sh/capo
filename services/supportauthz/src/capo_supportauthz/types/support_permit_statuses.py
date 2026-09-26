"""Generated from Smithy shape ``com.amazonaws.supportauthz#SupportPermitStatuses``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_supportauthz.types.support_permit_status

SupportPermitStatuses: TypeAlias = list[
    "capo_supportauthz.types.support_permit_status.SupportPermitStatus"
]


# --- restJson1 ser/de ---
def serialize_json(value: SupportPermitStatuses) -> list:
    import capo_supportauthz.types.support_permit_status

    out: list = []
    for item in value:
        out.append(capo_supportauthz.types.support_permit_status.serialize_json(item))
    return out


def deserialize_json(data: list) -> SupportPermitStatuses:
    import capo_supportauthz.types.support_permit_status

    out: SupportPermitStatuses = []
    for item in data:
        if item is None:
            continue
        out.append(capo_supportauthz.types.support_permit_status.deserialize_json(item))
    return out
