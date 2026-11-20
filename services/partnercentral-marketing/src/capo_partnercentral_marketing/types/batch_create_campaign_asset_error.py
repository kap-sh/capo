"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#BatchCreateCampaignAssetError``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.identifier


class BatchCreateCampaignAssetError(TypedDict, closed=True):
    source_asset_template_id: (
        "capo_partnercentral_marketing.types.identifier.Identifier"
    )
    """The failing entry's request identifier, so a caller can match this error to the entry it sent."""
    code: "str"
    """Error code -- ResourceNotFoundException when the blueprint is not on the campaign's bound template, InternalServerException otherwise. Throttling never appears here: DG throttles per operation, so a throttle fails the whole batch."""
    message: "str"
    """Human-readable cause."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchCreateCampaignAssetError) -> dict:
    out: dict = {}
    out["SourceAssetTemplateId"] = value["source_asset_template_id"]
    out["Code"] = value["code"]
    out["Message"] = value["message"]
    return out


def deserialize_cbor(data: dict) -> BatchCreateCampaignAssetError:
    out: BatchCreateCampaignAssetError = {}  # type: ignore[typeddict-item]
    if data.get("SourceAssetTemplateId") is not None:
        out["source_asset_template_id"] = data["SourceAssetTemplateId"]
    else:
        out["source_asset_template_id"] = ""
    if data.get("Code") is not None:
        out["code"] = data["Code"]
    else:
        out["code"] = ""
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    return out
