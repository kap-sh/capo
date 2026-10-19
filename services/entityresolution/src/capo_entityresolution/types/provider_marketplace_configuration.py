"""Generated from Smithy shape ``com.amazonaws.entityresolution#ProviderMarketplaceConfiguration``."""

from typing_extensions import TypedDict


class ProviderMarketplaceConfiguration(TypedDict, closed=True):
    data_set_id: "str"
    """<p>The dataset ID on Data Exchange.</p>"""
    revision_id: "str"
    """<p>The revision ID on Data Exchange.</p>"""
    asset_id: "str"
    """<p>The asset ID on Data Exchange.</p>"""
    listing_id: "str"
    """<p>The listing ID on Data Exchange.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProviderMarketplaceConfiguration) -> dict:
    out: dict = {}
    out["dataSetId"] = value["data_set_id"]
    out["revisionId"] = value["revision_id"]
    out["assetId"] = value["asset_id"]
    out["listingId"] = value["listing_id"]
    return out


def deserialize_json(data: dict) -> ProviderMarketplaceConfiguration:
    out: ProviderMarketplaceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("dataSetId") is not None:
        out["data_set_id"] = data["dataSetId"]
    else:
        out["data_set_id"] = ""
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    else:
        out["revision_id"] = ""
    if data.get("assetId") is not None:
        out["asset_id"] = data["assetId"]
    else:
        out["asset_id"] = ""
    if data.get("listingId") is not None:
        out["listing_id"] = data["listingId"]
    else:
        out["listing_id"] = ""
    return out
