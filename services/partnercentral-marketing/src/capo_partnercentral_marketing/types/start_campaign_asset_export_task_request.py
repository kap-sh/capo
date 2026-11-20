"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#StartCampaignAssetExportTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.campaign_identifier
    import capo_partnercentral_marketing.types.catalog
    import capo_partnercentral_marketing.types.client_token


class StartCampaignAssetExportTaskRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_marketing.types.catalog.Catalog"
    """The catalog (AWS or Sandbox)."""
    campaign_identifier: (
        "capo_partnercentral_marketing.types.campaign_identifier.CampaignIdentifier"
    )
    """The campaign whose assets are exported. Accepts the campaign id or ARN."""
    client_token: NotRequired[
        "capo_partnercentral_marketing.types.client_token.ClientToken"
    ]
    """Idempotency token. Two requests carrying the same token within the dedup window are one request and return the same task id."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StartCampaignAssetExportTaskRequest) -> dict:
    out: dict = {}
    import capo_partnercentral_marketing.types.catalog

    out["Catalog"] = capo_partnercentral_marketing.types.catalog.serialize_cbor(
        value["catalog"]
    )
    out["CampaignIdentifier"] = value["campaign_identifier"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_cbor(data: dict) -> StartCampaignAssetExportTaskRequest:
    out: StartCampaignAssetExportTaskRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
