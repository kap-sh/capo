"""Generated from Smithy shape ``com.amazonaws.connectcampaigns#PutDialRequestBatchRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcampaigns.types.campaign_id
    import capo_connectcampaigns.types.dial_request_list


class PutDialRequestBatchRequest(TypedDict, closed=True):
    id: "capo_connectcampaigns.types.campaign_id.CampaignId"
    dial_requests: "capo_connectcampaigns.types.dial_request_list.DialRequestList"


# --- restJson1 ser/de ---
def serialize_json(value: PutDialRequestBatchRequest) -> dict:
    out: dict = {}
    import capo_connectcampaigns.types.dial_request_list

    out["dialRequests"] = capo_connectcampaigns.types.dial_request_list.serialize_json(
        value["dial_requests"]
    )
    return out


def deserialize_json(data: dict) -> PutDialRequestBatchRequest:
    out: PutDialRequestBatchRequest = {}  # type: ignore[typeddict-item]
    if data.get("dialRequests") is not None:
        import capo_connectcampaigns.types.dial_request_list

        out["dial_requests"] = (
            capo_connectcampaigns.types.dial_request_list.deserialize_json(
                data["dialRequests"]
            )
        )
    else:
        out["dial_requests"] = []
    return out


def redact_sensitive(value: PutDialRequestBatchRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "dial_requests" in value:
        import capo_connectcampaigns.types.dial_request_list

        out["dial_requests"] = (
            capo_connectcampaigns.types.dial_request_list.redact_sensitive(
                value["dial_requests"]
            )
        )
    return out
