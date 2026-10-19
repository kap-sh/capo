"""Generated from Smithy shape ``com.amazonaws.partnercentralaccount#GetConnectionPreferencesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_account.types.catalog


class GetConnectionPreferencesRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_account.types.catalog.Catalog"
    """<p>The catalog identifier for the partner account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetConnectionPreferencesRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetConnectionPreferencesRequest:
    out: GetConnectionPreferencesRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    return out
