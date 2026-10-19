"""Generated from Smithy shape ``com.amazonaws.marketplacediscovery#SellerInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_discovery.types.non_empty_string
    import capo_marketplace_discovery.types.seller_profile_id


class SellerInformation(TypedDict, closed=True):
    seller_profile_id: (
        "capo_marketplace_discovery.types.seller_profile_id.SellerProfileId"
    )
    """<p>The unique identifier of the seller profile.</p>"""
    display_name: "capo_marketplace_discovery.types.non_empty_string.NonEmptyString"
    """<p>The human-readable name of the seller.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SellerInformation) -> dict:
    out: dict = {}
    out["sellerProfileId"] = value["seller_profile_id"]
    out["displayName"] = value["display_name"]
    return out


def deserialize_json(data: dict) -> SellerInformation:
    out: SellerInformation = {}  # type: ignore[typeddict-item]
    if data.get("sellerProfileId") is not None:
        out["seller_profile_id"] = data["sellerProfileId"]
    else:
        out["seller_profile_id"] = ""
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    else:
        out["display_name"] = ""
    return out
