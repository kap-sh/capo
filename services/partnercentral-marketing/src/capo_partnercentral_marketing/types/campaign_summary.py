"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#CampaignSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.asset_language
    import capo_partnercentral_marketing.types.campaign_id
    import capo_partnercentral_marketing.types.campaign_name
    import capo_partnercentral_marketing.types.campaign_state
    import capo_partnercentral_marketing.types.taggable_resource_arn
    import capo_partnercentral_marketing.types.timestamp
    import capo_partnercentral_marketing.types.utc_date


class CampaignSummary(TypedDict, closed=True):
    campaign_id: "capo_partnercentral_marketing.types.campaign_id.CampaignId"
    """The campaign identifier."""
    arn: "capo_partnercentral_marketing.types.taggable_resource_arn.TaggableResourceArn"
    """The campaign ARN. Present on the summary so a caller can tag a campaign straight from a list result without a GetCampaign per row — the same reason the audit timestamps are here."""
    name: "capo_partnercentral_marketing.types.campaign_name.CampaignName"
    """The display name."""
    state: "capo_partnercentral_marketing.types.campaign_state.CampaignState"
    """The campaign's state, derived on every read from `EndOn` and its assets. See `CampaignState`."""
    language: NotRequired[
        "capo_partnercentral_marketing.types.asset_language.AssetLanguage"
    ]
    """The language the campaign's assets are written and typeset in. See `Campaign$Language`."""
    start_on: NotRequired["capo_partnercentral_marketing.types.utc_date.UtcDate"]
    """The first day of the campaign's run window."""
    end_on: NotRequired["capo_partnercentral_marketing.types.utc_date.UtcDate"]
    """The last day of the campaign's run window."""
    created_at: NotRequired["capo_partnercentral_marketing.types.timestamp.Timestamp"]
    """Creation timestamp. Present on the summary so a caller can order a list by recency without reading each campaign in full."""
    updated_at: NotRequired["capo_partnercentral_marketing.types.timestamp.Timestamp"]
    """Last update timestamp. Present on the summary for the same reason as CreatedAt."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CampaignSummary) -> dict:
    out: dict = {}
    out["CampaignId"] = value["campaign_id"]
    out["Arn"] = value["arn"]
    out["Name"] = value["name"]
    import capo_partnercentral_marketing.types.campaign_state

    out["State"] = capo_partnercentral_marketing.types.campaign_state.serialize_cbor(
        value["state"]
    )
    if "language" in value:
        import capo_partnercentral_marketing.types.asset_language

        out["Language"] = (
            capo_partnercentral_marketing.types.asset_language.serialize_cbor(
                value["language"]
            )
        )
    if "start_on" in value:
        out["StartOn"] = value["start_on"]
    if "end_on" in value:
        out["EndOn"] = value["end_on"]
    if "created_at" in value:
        import capo_partnercentral_marketing.types.timestamp

        out["CreatedAt"] = capo_partnercentral_marketing.types.timestamp.serialize_cbor(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_partnercentral_marketing.types.timestamp

        out["UpdatedAt"] = capo_partnercentral_marketing.types.timestamp.serialize_cbor(
            value["updated_at"]
        )
    return out


def deserialize_cbor(data: dict) -> CampaignSummary:
    out: CampaignSummary = {}  # type: ignore[typeddict-item]
    if data.get("CampaignId") is not None:
        out["campaign_id"] = data["CampaignId"]
    else:
        out["campaign_id"] = ""
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("State") is not None:
        import capo_partnercentral_marketing.types.campaign_state

        out["state"] = (
            capo_partnercentral_marketing.types.campaign_state.deserialize_cbor(
                data["State"]
            )
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_partnercentral_marketing.types.campaign_state.CampaignState", ""
        )
    if data.get("Language") is not None:
        import capo_partnercentral_marketing.types.asset_language

        out["language"] = (
            capo_partnercentral_marketing.types.asset_language.deserialize_cbor(
                data["Language"]
            )
        )
    if data.get("StartOn") is not None:
        out["start_on"] = data["StartOn"]
    if data.get("EndOn") is not None:
        out["end_on"] = data["EndOn"]
    if data.get("CreatedAt") is not None:
        import capo_partnercentral_marketing.types.timestamp

        out["created_at"] = (
            capo_partnercentral_marketing.types.timestamp.deserialize_cbor(
                data["CreatedAt"]
            )
        )
    if data.get("UpdatedAt") is not None:
        import capo_partnercentral_marketing.types.timestamp

        out["updated_at"] = (
            capo_partnercentral_marketing.types.timestamp.deserialize_cbor(
                data["UpdatedAt"]
            )
        )
    return out
