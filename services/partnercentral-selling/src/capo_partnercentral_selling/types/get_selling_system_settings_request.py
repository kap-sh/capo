"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#GetSellingSystemSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier


class GetSellingSystemSettingsRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog in which the settings are defined. Acceptable values include <code>AWS</code> for production and <code>Sandbox</code> for testing environments.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetSellingSystemSettingsRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetSellingSystemSettingsRequest:
    out: GetSellingSystemSettingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    return out
