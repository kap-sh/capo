"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#UpdateCampaignAssetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.activation_issue_list
    import capo_partnercentral_marketing.types.campaign_asset_id
    import capo_partnercentral_marketing.types.campaign_asset_state


class UpdateCampaignAssetResponse(TypedDict, closed=True):
    id: "capo_partnercentral_marketing.types.campaign_asset_id.CampaignAssetId"
    """The asset identifier."""
    state: "capo_partnercentral_marketing.types.campaign_asset_state.CampaignAssetState"
    """The asset's state, **unchanged**. An update never moves it, so a live asset stays ACTIVE while its edited values take effect for the next activation. There is no edit-outcome member: a 200 means every submitted value applied, and every failure is a refusal on the call itself (DG-040 Decision 11)."""
    activation_issues: (
        "capo_partnercentral_marketing.types.activation_issue_list.ActivationIssueList"
    )
    """What must be fixed on this asset before it can be activated. Empty when the asset is ready. Issues don't block saving: an asset can be saved incomplete and fixed over several updates. `StartCampaignAssetActivationTask` refuses an asset that still has issues: an issue blocks activation when only an edit to the asset can change the outcome. Most issues name the field to fix in `FieldId`. Fix it with `UpdateCampaignAsset`, then read this list again. Besides the issues computed from the asset's content, the list carries what the last activation found: `CONTENT_REJECTED` and `PARTNER_IMAGE_REJECTED` when moderation refused a field. Editing that field removes its issue. A `CONTENT_REJECTED` without a `FieldId` means the text was refused as a whole; editing any text field removes it. Problems with the campaign's own settings, such as a missing recipient list, and with the partner's profile, such as a missing logo, are reported on `Campaign.ActivationIssues`, not here."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: UpdateCampaignAssetResponse) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import capo_partnercentral_marketing.types.campaign_asset_state

    out["State"] = (
        capo_partnercentral_marketing.types.campaign_asset_state.serialize_cbor(
            value["state"]
        )
    )
    import capo_partnercentral_marketing.types.activation_issue_list

    out["ActivationIssues"] = (
        capo_partnercentral_marketing.types.activation_issue_list.serialize_cbor(
            value["activation_issues"]
        )
    )
    return out


def deserialize_cbor(data: dict) -> UpdateCampaignAssetResponse:
    out: UpdateCampaignAssetResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("ActivationIssues") is not None:
        import capo_partnercentral_marketing.types.activation_issue_list

        out["activation_issues"] = (
            capo_partnercentral_marketing.types.activation_issue_list.deserialize_cbor(
                data["ActivationIssues"]
            )
        )
    else:
        out["activation_issues"] = []
    return out
