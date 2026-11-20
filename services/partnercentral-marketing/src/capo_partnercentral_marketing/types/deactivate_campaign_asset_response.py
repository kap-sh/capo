"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#DeactivateCampaignAssetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.attempt_status
    import capo_partnercentral_marketing.types.campaign_asset_id
    import capo_partnercentral_marketing.types.campaign_asset_state
    import capo_partnercentral_marketing.types.campaign_asset_state_reason


class DeactivateCampaignAssetResponse(TypedDict, closed=True):
    id: "capo_partnercentral_marketing.types.campaign_asset_id.CampaignAssetId"
    """The asset identifier."""
    state: "capo_partnercentral_marketing.types.campaign_asset_state.CampaignAssetState"
    """The asset's lifecycle position — INACTIVE once the stop is confirmed."""
    last_activation_status: NotRequired[
        "capo_partnercentral_marketing.types.attempt_status.AttemptStatus"
    ]
    """How the most recent *activation* attempt ended, which a stop does not change. Read with state, it is what separates a stopped asset (INACTIVE + SUCCEEDED) from one never activated (INACTIVE, this member absent). Omitted until a first activation has been attempted."""
    state_reason: NotRequired[
        "capo_partnercentral_marketing.types.campaign_asset_state_reason.CampaignAssetStateReason"
    ]
    """Why the asset sits where it does. Present when LastActivationStatus is FAILED, or on a deliberate INACTIVE."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeactivateCampaignAssetResponse) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import capo_partnercentral_marketing.types.campaign_asset_state

    out["State"] = (
        capo_partnercentral_marketing.types.campaign_asset_state.serialize_cbor(
            value["state"]
        )
    )
    if "last_activation_status" in value:
        import capo_partnercentral_marketing.types.attempt_status

        out["LastActivationStatus"] = (
            capo_partnercentral_marketing.types.attempt_status.serialize_cbor(
                value["last_activation_status"]
            )
        )
    if "state_reason" in value:
        import capo_partnercentral_marketing.types.campaign_asset_state_reason

        out["StateReason"] = (
            capo_partnercentral_marketing.types.campaign_asset_state_reason.serialize_cbor(
                value["state_reason"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DeactivateCampaignAssetResponse:
    out: DeactivateCampaignAssetResponse = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("State") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_state

        out["state"] = (
            capo_partnercentral_marketing.types.campaign_asset_state.deserialize_cbor(
                data["State"]
            )
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_partnercentral_marketing.types.campaign_asset_state.CampaignAssetState",
            "",
        )
    if data.get("LastActivationStatus") is not None:
        import capo_partnercentral_marketing.types.attempt_status

        out["last_activation_status"] = (
            capo_partnercentral_marketing.types.attempt_status.deserialize_cbor(
                data["LastActivationStatus"]
            )
        )
    if data.get("StateReason") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_state_reason

        out["state_reason"] = (
            capo_partnercentral_marketing.types.campaign_asset_state_reason.deserialize_cbor(
                data["StateReason"]
            )
        )
    return out
