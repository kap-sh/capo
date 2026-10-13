"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#PutOutboundRequestBatchRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_connectcampaignsv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.campaign_id
    import capo_connectcampaignsv2.types.outbound_request_list


class PutOutboundRequestBatchRequest(TypedDict, closed=True):
    id: "capo_connectcampaignsv2.types.campaign_id.CampaignId"
    outbound_requests: (
        "capo_connectcampaignsv2.types.outbound_request_list.OutboundRequestList"
    )


# --- restJson1 ser/de ---
def serialize_json(value: PutOutboundRequestBatchRequest) -> dict:
    out: dict = {}
    import capo_connectcampaignsv2.types.outbound_request_list

    out["outboundRequests"] = (
        capo_connectcampaignsv2.types.outbound_request_list.serialize_json(
            value["outbound_requests"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutOutboundRequestBatchRequest:
    out: PutOutboundRequestBatchRequest = {}  # type: ignore[typeddict-item]
    if data.get("outboundRequests") is not None:
        import capo_connectcampaignsv2.types.outbound_request_list

        out["outbound_requests"] = (
            capo_connectcampaignsv2.types.outbound_request_list.deserialize_json(
                data["outboundRequests"]
            )
        )
    else:
        raise DeserializationError(
            "PutOutboundRequestBatchRequest.outbound_requests required"
        )
    return out


def redact_sensitive(value: PutOutboundRequestBatchRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "outbound_requests" in value:
        import capo_connectcampaignsv2.types.outbound_request_list

        out["outbound_requests"] = (
            capo_connectcampaignsv2.types.outbound_request_list.redact_sensitive(
                value["outbound_requests"]
            )
        )
    return out
