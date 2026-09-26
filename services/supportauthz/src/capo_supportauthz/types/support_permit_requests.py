"""Generated from Smithy shape ``com.amazonaws.supportauthz#SupportPermitRequests``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_supportauthz.types.support_permit_request

SupportPermitRequests: TypeAlias = list[
    "capo_supportauthz.types.support_permit_request.SupportPermitRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: SupportPermitRequests) -> list:
    import capo_supportauthz.types.support_permit_request

    out: list = []
    for item in value:
        out.append(capo_supportauthz.types.support_permit_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> SupportPermitRequests:
    import capo_supportauthz.types.support_permit_request

    out: SupportPermitRequests = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_supportauthz.types.support_permit_request.deserialize_json(item)
        )
    return out
