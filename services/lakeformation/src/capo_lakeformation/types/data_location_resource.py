"""Generated from Smithy shape ``com.amazonaws.lakeformation#DataLocationResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.catalog_id_string
    import capo_lakeformation.types.resource_arn_string


class DataLocationResource(TypedDict, closed=True):
    catalog_id: NotRequired[
        "capo_lakeformation.types.catalog_id_string.CatalogIdString"
    ]
    """<p>The identifier for the Data Catalog where the location is registered with Lake Formation. By default, it is the account ID of the caller.</p>"""
    resource_arn: "capo_lakeformation.types.resource_arn_string.ResourceArnString"
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the data location resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataLocationResource) -> dict:
    out: dict = {}
    if "catalog_id" in value:
        out["CatalogId"] = value["catalog_id"]
    out["ResourceArn"] = value["resource_arn"]
    return out


def deserialize_json(data: dict) -> DataLocationResource:
    out: DataLocationResource = {}  # type: ignore[typeddict-item]
    if data.get("CatalogId") is not None:
        out["catalog_id"] = data["CatalogId"]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    return out
