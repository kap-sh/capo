"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#GetCampaignAssetResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_partnercentral_marketing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_asset


class GetCampaignAssetResponse(TypedDict, closed=True):
    asset: "capo_partnercentral_marketing.types.campaign_asset.CampaignAsset"
    """The asset resource."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetCampaignAssetResponse) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.campaign_asset

    out["Asset"] = capo_partnercentral_marketing.types.campaign_asset.serialize_cbor(
        value["asset"]
    )
    return out


def deserialize_cbor(data: dict) -> GetCampaignAssetResponse:
    out: GetCampaignAssetResponse = {}  # type: ignore[typeddict-item]
    if data.get("Asset") is not None:
        import capo_partnercentral_marketing.types.campaign_asset

        out["asset"] = (
            capo_partnercentral_marketing.types.campaign_asset.deserialize_cbor(
                data["Asset"]
            )
        )
    else:
        raise DeserializationError("GetCampaignAssetResponse.asset required")
    return out


def redact_sensitive(value: GetCampaignAssetResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "asset" in value:
        import capo_partnercentral_marketing.types.campaign_asset

        out["asset"] = (
            capo_partnercentral_marketing.types.campaign_asset.redact_sensitive(
                value["asset"]
            )
        )
    return out
