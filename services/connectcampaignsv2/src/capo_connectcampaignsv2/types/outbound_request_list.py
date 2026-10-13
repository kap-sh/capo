"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#OutboundRequestList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.outbound_request

OutboundRequestList: TypeAlias = list[
    "capo_connectcampaignsv2.types.outbound_request.OutboundRequest"
]


# --- restJson1 ser/de ---
def serialize_json(value: OutboundRequestList) -> list:
    import capo_connectcampaignsv2.types.outbound_request

    out: list = []
    for item in value:
        out.append(capo_connectcampaignsv2.types.outbound_request.serialize_json(item))
    return out


def deserialize_json(data: list) -> OutboundRequestList:
    import capo_connectcampaignsv2.types.outbound_request

    out: OutboundRequestList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connectcampaignsv2.types.outbound_request.deserialize_json(item)
        )
    return out


def redact_sensitive(value: OutboundRequestList) -> list[Any]:
    import capo_connectcampaignsv2.types.outbound_request

    return [
        capo_connectcampaignsv2.types.outbound_request.redact_sensitive(item)
        for item in value
    ]
