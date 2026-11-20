"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetExportFailureReason``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_asset_export_failure_code
    import capo_partnercentral_marketing.types.error_message


class CampaignAssetExportFailureReason(TypedDict, closed=True):
    code: "capo_partnercentral_marketing.types.campaign_asset_export_failure_code.CampaignAssetExportFailureCode"
    """Machine-readable failure cause."""
    message: "capo_partnercentral_marketing.types.error_message.ErrorMessage"
    """Human-readable explanation."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetExportFailureReason) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.campaign_asset_export_failure_code

    out["Code"] = (
        capo_partnercentral_marketing.types.campaign_asset_export_failure_code.serialize_cbor(
            value["code"]
        )
    )
    out["Message"] = value["message"]
    return out


def deserialize_cbor(data: dict) -> CampaignAssetExportFailureReason:
    out: CampaignAssetExportFailureReason = {}  # type: ignore[typeddict-item]
    if data.get("Code") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_export_failure_code

        out["code"] = (
            capo_partnercentral_marketing.types.campaign_asset_export_failure_code.deserialize_cbor(
                data["Code"]
            )
        )
    else:
        import typing

        out["code"] = typing.cast(
            "capo_partnercentral_marketing.types.campaign_asset_export_failure_code.CampaignAssetExportFailureCode",
            "",
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    else:
        out["message"] = ""
    return out
