"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignAssetActivationOutcome``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_asset_activation_status
    import capo_partnercentral_marketing.types.campaign_asset_id
    import capo_partnercentral_marketing.types.campaign_asset_state_reason
    import capo_partnercentral_marketing.types.error_message


class CampaignAssetActivationOutcome(TypedDict, closed=True):
    campaign_asset_id: (
        "capo_partnercentral_marketing.types.campaign_asset_id.CampaignAssetId"
    )
    """The asset this outcome belongs to."""
    status: "capo_partnercentral_marketing.types.campaign_asset_activation_status.CampaignAssetActivationStatus"
    """This asset's contribution to the task's status."""
    reason: NotRequired[
        "capo_partnercentral_marketing.types.campaign_asset_state_reason.CampaignAssetStateReason"
    ]
    """Why the activation did not succeed. Present when status is FAILED."""
    message: NotRequired[
        "capo_partnercentral_marketing.types.error_message.ErrorMessage"
    ]
    """A description of `Reason` for display. Don't parse it. For a mailing-credit shortfall it states the credits needed and remaining."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignAssetActivationOutcome) -> dict:
    out: dict = {}
    out["CampaignAssetId"] = value["campaign_asset_id"]
    import capo_partnercentral_marketing.types.campaign_asset_activation_status

    out["Status"] = (
        capo_partnercentral_marketing.types.campaign_asset_activation_status.serialize_cbor(
            value["status"]
        )
    )
    if "reason" in value:
        import capo_partnercentral_marketing.types.campaign_asset_state_reason

        out["Reason"] = (
            capo_partnercentral_marketing.types.campaign_asset_state_reason.serialize_cbor(
                value["reason"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    return out


def deserialize_cbor(data: dict) -> CampaignAssetActivationOutcome:
    out: CampaignAssetActivationOutcome = {}  # type: ignore[typeddict-item]
    if data.get("CampaignAssetId") is not None:
        out["campaign_asset_id"] = data["CampaignAssetId"]
    else:
        out["campaign_asset_id"] = ""
    if data.get("Status") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_activation_status

        out["status"] = (
            capo_partnercentral_marketing.types.campaign_asset_activation_status.deserialize_cbor(
                data["Status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_partnercentral_marketing.types.campaign_asset_activation_status.CampaignAssetActivationStatus",
            "",
        )
    if data.get("Reason") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_state_reason

        out["reason"] = (
            capo_partnercentral_marketing.types.campaign_asset_state_reason.deserialize_cbor(
                data["Reason"]
            )
        )
    if data.get("Message") is not None:
        out["message"] = data["Message"]
    return out
