"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CreateCampaignResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_id
    import capo_partnercentral_marketing.types.taggable_resource_arn


class CreateCampaignResponse(TypedDict, closed=True):
    id: "capo_partnercentral_marketing.types.campaign_id.CampaignId"
    """The new campaign's identifier."""
    arn: "capo_partnercentral_marketing.types.taggable_resource_arn.TaggableResourceArn"
    """The new campaign's ARN."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateCampaignResponse) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Arn"] = value["arn"]
    return out


def deserialize_cbor(data: dict) -> CreateCampaignResponse:
    out: CreateCampaignResponse = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    return out
