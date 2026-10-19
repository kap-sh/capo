"""Generated from Smithy shape ``com.amazonaws.connectcampaignsv2#PutProfileOutboundRequestBatchRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaignsv2.types.campaign_id
    import capo_connectcampaignsv2.types.profile_outbound_request_list


class PutProfileOutboundRequestBatchRequest(TypedDict, closed=True):
    id: "capo_connectcampaignsv2.types.campaign_id.CampaignId"
    profile_outbound_requests: "capo_connectcampaignsv2.types.profile_outbound_request_list.ProfileOutboundRequestList"


# --- restJson1 ser/de ---
def serialize_json(value: PutProfileOutboundRequestBatchRequest) -> dict:
    out: dict = {}
    import capo_connectcampaignsv2.types.profile_outbound_request_list

    out["profileOutboundRequests"] = (
        capo_connectcampaignsv2.types.profile_outbound_request_list.serialize_json(
            value["profile_outbound_requests"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutProfileOutboundRequestBatchRequest:
    out: PutProfileOutboundRequestBatchRequest = {}  # type: ignore[typeddict-item]
    if data.get("profileOutboundRequests") is not None:
        import capo_connectcampaignsv2.types.profile_outbound_request_list

        out["profile_outbound_requests"] = (
            capo_connectcampaignsv2.types.profile_outbound_request_list.deserialize_json(
                data["profileOutboundRequests"]
            )
        )
    else:
        out["profile_outbound_requests"] = []
    return out
