"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#UpdateCampaignResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_id


class UpdateCampaignResponse(TypedDict, closed=True):
    id: "capo_partnercentral_marketing.types.campaign_id.CampaignId"
    """The campaign identifier."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateCampaignResponse) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    return out


def deserialize_cbor(data: dict) -> UpdateCampaignResponse:
    out: UpdateCampaignResponse = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    return out
