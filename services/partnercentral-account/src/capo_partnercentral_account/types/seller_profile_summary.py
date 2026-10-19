"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#SellerProfileSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.seller_profile_id
    import capo_partnercentral_account.types.unicode_string


class SellerProfileSummary(TypedDict, closed=True):
    id: "capo_partnercentral_account.types.seller_profile_id.SellerProfileId"
    """<p>The unique identifier of the seller profile.</p>"""
    name: "capo_partnercentral_account.types.unicode_string.UnicodeString"
    """<p>The display name of the seller.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SellerProfileSummary) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SellerProfileSummary:
    out: SellerProfileSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
