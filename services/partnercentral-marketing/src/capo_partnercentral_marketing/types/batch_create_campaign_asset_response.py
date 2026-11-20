"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#BatchCreateCampaignAssetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.batch_create_campaign_asset_errors
    import capo_partnercentral_marketing.types.batch_create_campaign_asset_results


class BatchCreateCampaignAssetResponse(TypedDict, closed=True):
    errors: "capo_partnercentral_marketing.types.batch_create_campaign_asset_errors.BatchCreateCampaignAssetErrors"
    """One entry per blueprint that could not be instantiated. Empty, never absent, when all entries succeeded."""
    successful: NotRequired[
        "capo_partnercentral_marketing.types.batch_create_campaign_asset_results.BatchCreateCampaignAssetResults"
    ]
    """One entry per asset that exists as a result of this call, whether created here or already present."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: BatchCreateCampaignAssetResponse) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.batch_create_campaign_asset_errors

    out["Errors"] = (
        capo_partnercentral_marketing.types.batch_create_campaign_asset_errors.serialize_cbor(
            value["errors"]
        )
    )
    if "successful" in value:
        import capo_partnercentral_marketing.types.batch_create_campaign_asset_results

        out["Successful"] = (
            capo_partnercentral_marketing.types.batch_create_campaign_asset_results.serialize_cbor(
                value["successful"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> BatchCreateCampaignAssetResponse:
    out: BatchCreateCampaignAssetResponse = {}  # type: ignore[typeddict-item]
    if data.get("Errors") is not None:
        import capo_partnercentral_marketing.types.batch_create_campaign_asset_errors

        out["errors"] = (
            capo_partnercentral_marketing.types.batch_create_campaign_asset_errors.deserialize_cbor(
                data["Errors"]
            )
        )
    else:
        out["errors"] = []
    if data.get("Successful") is not None:
        import capo_partnercentral_marketing.types.batch_create_campaign_asset_results

        out["successful"] = (
            capo_partnercentral_marketing.types.batch_create_campaign_asset_results.deserialize_cbor(
                data["Successful"]
            )
        )
    return out
