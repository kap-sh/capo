"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#StartCampaignAssetActivationTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_asset_identifiers
    import capo_partnercentral_marketing.types.campaign_identifier
    import capo_partnercentral_marketing.types.catalog
    import capo_partnercentral_marketing.types.client_token


class StartCampaignAssetActivationTaskRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_marketing.types.catalog.Catalog"
    """The catalog (AWS or Sandbox)."""
    campaign_identifier: (
        "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier"
    )
    """The campaign identifier, which also authorizes the call."""
    campaign_asset_identifiers: "capo_partnercentral_marketing.types.campaign_asset_identifiers.CampaignAssetIdentifiers"
    """The assets to activate, in any order — the service derives the dependency order and ignores the order given here."""
    client_token: NotRequired[
        "capo_partnercentral_marketing.types.client_token.ClientToken"
    ]
    """Idempotency token. Two requests carrying the same token are one request, and the second returns the first one's task rather than starting a second. The deduplication window is the **life of the task record**, not a fixed number of hours: replaying a token after the task has expired starts a new task. Stated because a caller would otherwise assume the usual few-hour guarantee."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartCampaignAssetActivationTaskRequest) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.catalog

    out["Catalog"] = capo_partnercentral_marketing.types.catalog.serialize_cbor(
        value["catalog"]
    )
    out["CampaignIdentifier"] = value["campaign_identifier"]
    import capo_partnercentral_marketing.types.campaign_asset_identifiers

    out["CampaignAssetIdentifiers"] = (
        capo_partnercentral_marketing.types.campaign_asset_identifiers.serialize_cbor(
            value["campaign_asset_identifiers"]
        )
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_cbor(data: dict) -> StartCampaignAssetActivationTaskRequest:
    out: StartCampaignAssetActivationTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        import capo_partnercentral_marketing.types.catalog

        out["catalog"] = capo_partnercentral_marketing.types.catalog.deserialize_cbor(
            data["Catalog"]
        )
    else:
        import typing

        out["catalog"] = typing.cast(
            "capo_partnercentral_marketing.types.catalog.Catalog", ""
        )
    if data.get("CampaignIdentifier") is not None:
        out["campaign_identifier"] = data["CampaignIdentifier"]
    else:
        out["campaign_identifier"] = ""
    if data.get("CampaignAssetIdentifiers") is not None:
        import capo_partnercentral_marketing.types.campaign_asset_identifiers

        out["campaign_asset_identifiers"] = (
            capo_partnercentral_marketing.types.campaign_asset_identifiers.deserialize_cbor(
                data["CampaignAssetIdentifiers"]
            )
        )
    else:
        out["campaign_asset_identifiers"] = []
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
